from authors_api.settings.base import *
import os
from dotenv import load_dotenv

load_dotenv(ROOT_DIR / 'authors_api/settings/.env')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
        'rest_framework.renderers.BrowsableAPIRenderer',
)

# DOMAIN_NAME = 'http://127.0.0.1:8000'
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL = True if os.getenv('EMAIL_USE_SSL') == 'True' else False

STATIC_ROOT = str(ROOT_DIR / 'static/')
MEDIA_ROOT = str(ROOT_DIR / 'media/')
