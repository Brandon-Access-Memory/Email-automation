"""
Django settings for email_automation project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import base64
import environ
from pathlib import Path
from email.headerregistry import Address


env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value('SECRET_KEY', default='django-insecure-ksg!i&r49#t+x6*f^v#glkvhg_nfb^24r%l7im#ti-(it!5(y6')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(env('DEBUG')))

ALLOWED_HOSTS = []


if DEBUG:
    DOMAIN = 'http://localhost:8000'

else:
    DOMAIN = env('DOMAIN')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #3rd party
    'encrypted_model_fields',
    'tailwind',
    'theme',
    'corsheaders',
    'django_celery_beat',
    'django_browser_reload',

    # my apps
    'automail',
    'user'

]

FIELD_ENCRYPTION_KEY = env.get_value('FIELD_ENCRYPTION_KE', default="-0YzXZeaLwOzaR0NYym4UmZurjhZDlaccMc7sbAhi0w=")
# FIELD_ENCRYPTION_KEY = "-0YzXZeaLwOzaR0NYym4UmZurjhZDlaccMc7sbAhi0w="# env('FIELD_ENCRYPTION_KEY', default="-0YzXZeaLwOzaR0NYym4UmZurjhZDlaccMc7sbAhi0w=")

# # Decode the base64-encoded string to bytes with UTF-8 encoding
# # FIELD_ENCRYPTION_KEY = base64.b64decode(FIELD_ENCRYPTION_KEY_str)

LOGIN_URL = '/user/login/'

AUTH_USER_MODEL = "user.User" 

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'

else: 
    CELERY_BROKER_URL = env('REDIS_PROD_HOST')


CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "django_browser_reload.middleware.BrowserReloadMiddleware", # reload

    'email_automation.middlewares.FileUploadMiddleware',

]

ROOT_URLCONF = 'email_automation.urls'


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # This is only for development
    # EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # for production

    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = 465

    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

    DEFAULT_FROM_EMAIL = Address(display_name="AdoStrings - Creators", addr_spec=EMAIL_HOST_USER)

    # EMAIL_USE_TLS = True
    EMAIL_USE_SSL = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath("templates"),
            BASE_DIR.joinpath("templates", "html", ),
            BASE_DIR.joinpath("templates", "html", "authentication"),
            BASE_DIR.joinpath("templates", "html", "email-product"),
            BASE_DIR.joinpath("templates", "html", "email-product", "templates"),
            BASE_DIR.joinpath("templates", "html", "email-product", "campaign"),
        ],
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

WSGI_APPLICATION = 'email_automation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR.joinpath("templates"),
]


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles', 'static')

MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
