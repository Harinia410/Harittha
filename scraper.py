# scraper.py
import requests

def fetch_coin_data(coin):
    url = f'https://coinmarketcap.com/currencies/{coin.lower()}/'
    requests.get(url)
    # Here you should parse the response content and extract required data
    # This is just a placeholder, replace it with actual scraping logic
    data = {
        "coin": coin,
        "price": 0.003913,
        "price_change": -5.44,
        "market_cap": 37814377,
        "market_cap_rank": 740,
        "volume": 4583151,
        "volume_rank": 627,
        "volume_change": 12.21,
        "circulating_supply": 9663955990,
        "total_supply": 9999609598,
        "diluted_market_cap": 39127766,
        "contracts": [
            {
                "name": "solana",
                "address": "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
            }
        ],
        "official_links": [
            {
                "name": "website",
                "link": "https://dukocoin.com"
            }
        ],
        "socials": [
            {
                "name": "twitter",
                "url": "https://twitter.com/dukocoin"
            },
            {
                "name": "telegram",
                "url": "https://t.me/+jlScZmFrQ8g2MDg8"
            }
        ]
    }
    return data
