from .base import *
from .base import env

DEBUG = True
SECRET_KEY = env('SECRET_KEY', default='keyiftheresntanyinenvironment')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "pavelmirosh@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Swifty Authors"

SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"] = timedelta(minutes=720)

# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
#         'rest_framework.renderers.BrowsableAPIRenderer',
# )

