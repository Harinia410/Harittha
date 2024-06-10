from django.db import models

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'scraper'

class MarketData(models.Model):
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        app_label = 'scraper'

class SocialLink(models.Model):
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        app_label = 'scraper'
