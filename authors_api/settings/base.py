from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env()

# swifty_authors/
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# swifty_authors/core_apps
APPS_DIR = ROOT_DIR / "core_apps"

DEBUG = env.bool("DEBUG", False)

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]

SITE_ID = 1
ADMIN_URL = "supersecret/"
ADMINS = [("""Pavel Mirosh""", "pavelmirosh@gmail.com")]
MANAGERS = ADMINS

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders",
    "djcelery_email",
    "djoser",
    "rest_framework_simplejwt",
    "haystack",
    "drf_haystack",
]

LOCAL_APPS = [
    "core_apps.common",
    "core_apps.users",
    "core_apps.profiles",
    "core_apps.articles",
    "core_apps.comments",
    "core_apps.favorites",
    "core_apps.ratings",
    "core_apps.reactions",
    "core_apps.search",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "authors_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "authors_api.wsgi.application"

# export DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/authors_db
DATABASES = {"default": env.db("DATABASE_URL", )}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "core_apps.common.exceptions.common_exception_handler",
    "NON_FIELD_ERRORS_KEY": "error",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",

        # passing session id (for debugging in browser)
        # 'rest_framework.authentication.SessionAuthentication',

        # passing login/password in request.args (http authentification)
        # 'rest_framework.authentication.BasicAuthentication',

        # passing token in headers
        # 'rest_framework.authentication.TokenAuthentication',

        # jwt-based authentication
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],

    # "DEFAULT_RENDERER_CLASSES": [
    # "rest_framework.renderers.JSONRenderer",
    # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    # ],

    # 'DEFAULT_PARSER_CLASSES': (
    # If you use MultiPartFormParser or FormParser, we also have a camel case version
    # 'djangorestframework_camel_case.parser.CamelCaseFormParser',
    # 'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    # 'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    # ),

    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 100,

    # "DEFAULT_PERMISSION_CLASSES": [
    # permissions to makeOperations/toViewOnly for authenticated users in current session
    # "rest_framework.permissions.IsAuthenticated",
    # "rest_framework.permissions.IsAuthenticatedOrReadOnly",

    # permissions according to auth_permission
    # "rest_framework.permissions.DjangoModelPermissions",
    # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",

    # for making own permissions
    # "rest_framework.permissions.BasePermission",
    # ],

    # "DEFAULT_VERSIONING_CLASS":
    # http://127.0.0.1:8000/api/v2/users/
    #     "rest_framework.versioning.URLPathVersioning",

    # path('api/v1/users/', include('userapp.urls', namespace='v1')),
    # 'rest_framework.versioning.NamespaceVersioning',

    # http://v1.example.com/bookings/
    # 'rest_framework.versioning.HostNameVersioning',

    # http://127.0.0.1:8000/api/users/?version=v1/
    # 'rest_framework.versioning.QueryParameterVersioning',

    # requests.get('http://127.0.0.1:8000/api/users/', headers={'Accept': 'application/json; version=v2'})
    # 'rest_framework.versioning.AcceptHeaderVersioning',

}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    "SIGNING_KEY": env("SIGNING_KEY"),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
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

STATIC_URL = "/staticfiles/"
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = str(ROOT_DIR / "mediafiles")

CORS_URLS_REGEX = r"^/api/.*$"

AUTH_USER_MODEL = "users.User"

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": ROOT_DIR / "whoosh_index",
    }
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO", "handlers": ["console"]}
}

AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
