from rest_framework import viewsets
from .models import CryptoCurrency, MarketData, SocialLink
from .serializers import CryptoCurrencySerializer, MarketDataSerializer, SocialLinkSerializer

class CryptoCurrencyViewSet(viewsets.ModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptoCurrencySerializer

class MarketDataViewSet(viewsets.ModelViewSet):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

# Existing views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import start_scraping, get_scraping_status

class StartScrapingView(APIView):
    def post(self, request, format=None):
        coin_acronyms = request.data.get('coin_acronyms', [])
        task_result = start_scraping.delay(coin_acronyms)
        return Response({'job_id': task_result.id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id, format=None):
        task_result = get_scraping_status.delay(job_id)
        if task_result.ready():
            scraping_status = task_result.result
            return Response(scraping_status, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'In progress'}, status=status.HTTP_202_ACCEPTED)
