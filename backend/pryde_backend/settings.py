"""
Django settings for pryde_backend project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from corsheaders.defaults import default_headers


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v-(ma7))q2xo4%)m^7=!90$7_087jp1!)2=j!u%)jxz+je=8p4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django app used by rest-auth
    'django.contrib.sites',

    # local
    'api.apps.ApiConfig',

    # 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'phonenumber_field',

    # for dealing with CORS (Cross Origin Resource Sharing... decoupled backend and frontend) related stuff
    'corsheaders',

    'django_mysql'
]




# Additional Settings


# CORS Settings
# this should be set to false in production... allows any server to hit our backend which is not okay... only our
# frontend server should be allowed to send requests to our backend
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://10.145.14.218:8000',
    'http://localhost:8081',
    'http://localhost:3000',
)
# whenever we create additional headers for our requests
# they need to go here!!!!
CORS_ALLOW_HEADERS = default_headers + (
    'Api-Token',
    'Api-Secret-Key',
    'xsrfheadername',
    'xsrfcookiename',
    'content-type',
     'X-CSRFTOKEN'
)
CORS_ALLOW_CREDENTIALS = True

# make all endpoints atomic
ATOMIC_REQUESTS = True


# set site_id to 1 for allauth/rest-auth
SITE_ID = 1

# set AUTH_USER_MODEL to our user model
AUTH_USER_MODEL = 'api.PUser'

# settings for rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework_api_key.permissions.HasAPIKey',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]}

# settings to override rest-auth and allow for additional registration fields
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'api.custom_register.serializers.CustomRegisterSerializer',
}
ACCOUNT_ADAPTER = 'api.custom_adapter.adapter.CustomAccountAdapter'


# allauth stuff
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SWAGGER_SETTINGS = {
#     'LOGIN_URL': 'rest_framework:login',
#     'LOGOUT_URL': 'rest_framework:logout',
#     'JSON_EDITOR': 'True',
#     'SHOW_REQUEST_HEADERS': 'True',
#     'SECURITY_DEFINITIONS': {
#             'api_key': {
#                 'type': 'apiKey',
#                 'in': 'header',
#                 'name': 'Authorization'
#             }
#         },
#
#
# }

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # middleware for django-cors-headers
]

ROOT_URLCONF = 'pryde_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pryde_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'pryde',
    #     'USER': 'postgres',
    #     'PASSWORD': 'password',
    #     'HOST': 'localhost',
    #     'PORT': '5432'
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pryde',
        'USER': 'pryde',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
        # Tell Django to build the test database with the 'utf8mb4' character set
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
