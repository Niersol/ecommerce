from .common import *
import os 
import dj_databse_url

DEBUG = False
ALLOWED_HOSTS = ['niersol-prod-89f81abaa275.herokuapp.com']
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_databse_url.config()
}
REDIS_URL = os.environ['REDIS_URL']
CELERY_BROKER_URL = REDIS_URL
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        'TIMEOUT':10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
