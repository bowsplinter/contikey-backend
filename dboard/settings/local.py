from .base import *
from env import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': settings['RDS_DB_NAME'],
        'USER': settings['RDS_USERNAME'],
        'PASSWORD': settings['RDS_PASSWORD'],
        'HOST': settings['RDS_HOSTNAME'],
        'PORT': settings['RDS_PORT']
    }
}