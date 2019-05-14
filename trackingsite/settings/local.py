# -*- coding:utf-8 -*-
from .base import *

DEBUG = False
"""	'default':{
	 'ENGINE': 'django.db.backends.mysql',
	 'USER': 'root',
	 'PASSWORD': 'fy911phutys',
	 'NAME': 'trackingsite'
	}"""
DATABASES = {
	'default':{
	 'ENGINE':'django.db.backends.postgresql_psycopg2',
	 'NAME':'trackingsite',
	 'USER':'fingeruser',
	 'PASSWORD':'fingerechoroot123',
	 'HOST':'va.fyping.cn',
	 'PORT':'5444'
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




