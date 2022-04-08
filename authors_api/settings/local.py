from .base import *
from .base import env

DEBUG = True
SECRET_KEY = env('SECRET_KEY', default='keyiftheresntanyinenvironment')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
        'rest_framework.renderers.BrowsableAPIRenderer',
)

