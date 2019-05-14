# -*- coding:utf-8 -*-
from .base import *

DEBUG = True
SECRET_KEY = 'b@+hubyoi+fcwft^@7j3(sarqb=%jc#=ae4!hw$v&3utzkxph4'

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
DATABASES = {     
	'default': {         # 'ENGINE': 'django.db.backends.sqlite3',         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),         
	'ENGINE': 'django.db.backends.postgresql_psycopg2',         
	'NAME': 'trackingsite_test', #数据库名字         
	'USER': 'postgres', #用户名         
	"PASSWORD" : '', #自己的密码         
	"HOST":'vva.fyping.cn',         
	'PORT':5444,     
	} 
}
ALLOWED_HOSTS=["*"]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'




