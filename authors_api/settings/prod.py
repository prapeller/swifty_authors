from authors_api.settings.base import *
import os
from dotenv import load_dotenv

load_dotenv(ROOT_DIR / 'authors_api/settings/.env')

DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('SECRET_KEY')

DOMAIN_NAME = "https://blackemployer.com"
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True if os.getenv('EMAIL_USE_SSL') == 'True' else False

STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/static/media'

CSRF_TRUSTED_ORIGINS = [
    "https://127.0.0.1",
    "http://127.0.0.1",
    "https://0.0.0.0",
    "http://0.0.0.0",
    "https://blackemployer.com",
    "https://www.blackemployer.com"
]
