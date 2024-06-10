# crypto_scraper/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_scraper.settings')

app = Celery('scraper')

app.config_from_object('crypto_scraper.settings', namespace='CELERY')

app.autodiscover_tasks()
