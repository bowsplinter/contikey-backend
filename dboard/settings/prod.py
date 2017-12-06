from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dboard',
        'USER': 'dboard',
        'PASSWORD': 'db1234567',
        'HOST': 'mycontikey.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
