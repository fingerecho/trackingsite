# -*- coding:utf-8 -*-
from .base import *

DEBUG = False

DATABASES = {
	'default':{
	 'ENGINE': 'django.db.backends.mysql',
	 'USER': 'root',
	 'PASSWORD': 'fy911phutys',
	 'NAME': 'trackingsite'
	}
}
CACHES = {
    'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'unique-snowflake',
    'KEY_PREFIX': 'aumoo',
    'TIMEOUT': 3600
       }
}

ALLOWED_HOSTS=["*"]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'




