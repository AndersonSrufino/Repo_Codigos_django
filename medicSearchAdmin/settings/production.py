from .settings import *
from decouple import config


DEBUG = False

#cria a secret key do ambiente de desenvolvimento
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': config('DB_NAME'),
'USER': config('DB_USER'),
'PASSWORD': config('DB_PASSWORD'),
'HOST': config('DB_HOST', default='127.0.0.1'),
'PORT': config('DB_PORT', default=('5432')),
    }
}