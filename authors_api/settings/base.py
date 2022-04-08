from datetime import timedelta
from pathlib import Path
import environ

env = environ.Env()

# swifty_authors/
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# swifty_authors/core_apps
APPS_DIR = ROOT_DIR / 'core_apps'

DEBUG = env.bool('DEBUG', False)

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

SITE_ID = 1
ADMIN_URL = 'supersecretadminurl/'
ADMINS = [("""Pavel Mirosh""", 'pavelmirosh@gmail.com')]
MANAGERS = ADMINS

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    'drf_yasg',
    'corsheaders',
]

LOCAL_APPS = [
    'core_apps.common',
    'core_apps.users',
    'core_apps.profiles',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authors_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authors_api.wsgi.application'

#export DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/authors_db
DATABASES = {"default": env.db("DATABASE_URL",)}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],
    # 'DEFAULT_PARSER_CLASSES': (
    # If you use MultiPartFormParser or FormParser, we also have a camel case version
    # 'djangorestframework_camel_case.parser.CamelCaseFormParser',
    # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    # 'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,

    'DEFAULT_PERMISSION_CLASSES': [
        # permissions to makeOperations/toViewOnly for authenticated users in current session
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',

        # permissions according to auth_permission
        'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

        # for making own permissions
        # 'rest_framework.permissions.BasePermission',
    ],

    'DEFAULT_VERSIONING_CLASS':
    # http://127.0.0.1:8000/api/v2/users/
        'rest_framework.versioning.URLPathVersioning',

    # path('api/v1/users/', include('userapp.urls', namespace='v1')),
    # 'rest_framework.versioning.NamespaceVersioning',

    # http://v1.example.com/bookings/
    # 'rest_framework.versioning.HostNameVersioning',

    # http://127.0.0.1:8000/api/users/?version=v1/
    # 'rest_framework.versioning.QueryParameterVersioning',

    # requests.get('http://127.0.0.1:8000/api/users/', headers={'Accept': 'application/json; version=v2'})
    # 'rest_framework.versioning.AcceptHeaderVersioning',

    "EXCEPTION_HANDLER": "core_apps.common.exceptions.common_exception_handler",
    "NON_FIELD_ERRORS_KEY": "error",

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # passing session id (for debugging in browser)
        # 'rest_framework.authentication.SessionAuthentication',

        # passing login/password in request.args (http authentification)
        # 'rest_framework.authentication.BasicAuthentication',

        # passing token in headers
        # 'rest_framework.authentication.TokenAuthentication',

        # jwt-based authentication
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # "SIGNING_KEY": env("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create": "core_apps.users.serializers.CreateUserSerializer",
        "user": "core_apps.users.serializers.UserSerializer",
        "current_user": "core_apps.users.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

STATIC_URL = '/staticfiles/'
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = str(ROOT_DIR / 'mediafiles')

CORS_URLS_REGEX = r'^/api/.*$'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'root': {
        'level': 'INFO', 'handlers': ['console']}
}
