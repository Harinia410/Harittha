from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CryptoCurrencyViewSet, MarketDataViewSet, SocialLinkViewSet

router = DefaultRouter()
router.register(r'cryptocurrencies', CryptoCurrencyViewSet)
router.register(r'marketdata', MarketDataViewSet)
router.register(r'sociallinks', SocialLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
