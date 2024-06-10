# tasks.py
from celery import shared_task
from .scraper import fetch_coin_data
from .models import CryptoCurrency, MarketData, SocialLink

@shared_task
def scrape_coin_data(coin):
    data = fetch_coin_data(coin)
    
    coin_instance, created = CryptoCurrency.objects.get_or_create(symbol=coin, defaults={'name': coin})
    MarketData.objects.create(
        coin=coin_instance,
        price=data['price'],
        price_change=data['price_change'],
        market_cap=data['market_cap'],
        market_cap_rank=data['market_cap_rank'],
        volume=data['volume'],
        volume_rank=data['volume_rank'],
        volume_change=data['volume_change'],
        circulating_supply=data['circulating_supply'],
        total_supply=data['total_supply'],
        diluted_market_cap=data['diluted_market_cap']
    )
    for social in data['socials']:
        SocialLink.objects.create(
            coin=coin_instance,
            name=social['name'],
            link=social['url']
        )
    
    return data

@shared_task
def start_scraping(coin_acronyms):
    tasks = []
    for coin in coin_acronyms:
        result = scrape_coin_data.delay(coin)
        tasks.append(result.id)
    return tasks

@shared_task
def get_scraping_status(job_id):
    from celery.result import AsyncResult
    task_result = AsyncResult(job_id)
    if task_result.ready():
        return task_result.result
    else:
        return {'status': 'In progress'}
