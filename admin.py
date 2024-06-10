from django.contrib import admin
from .models import CryptoCurrency, MarketData, SocialLink

admin.site.register(CryptoCurrency)
admin.site.register(MarketData)
admin.site.register(SocialLink)
