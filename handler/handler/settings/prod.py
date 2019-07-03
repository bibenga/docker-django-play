from .base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'handler-db',
        'PORT': '5432',
    },

    'sensor': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'sensor-db',
        'PORT': '5432',
    },
}


CELERY_BROKER_URL = 'redis://handler-redis:6379/2'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
