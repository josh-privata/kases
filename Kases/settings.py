"""
Django settings for Kases.
"""

import posixpath
import raven
from sys import argv
import os
from os import environ, getenv
from os.path import abspath, dirname, join
import logging
import logging.config
from configurations import Configuration



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = 'Kases'
PROJECT_ENVIRONMENT_SLUG = '{}_{}'.format(PROJECT_NAME, environ.get('DJANGO_CONFIGURATION'))


class Common(Configuration):

    ADMINS = (
        ('Josh Cannons', 'josh.cannons@gmail.com'),
    )

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'd1307aaa-f585-475d-8567-ab6ab06ff5db'

    ALLOWED_HOSTS = ['*']
    
    # Redirect to home URL after login (Default redirects to /accounts/profile/)
    LOGIN_REDIRECT_URL = '/'

    # Application definition
    INSTALLED_APPS = [
        # Kases Apps
        'utils',
        'evidence',
        'case',
        'entity',
        'task',
        #'note',
        'inventory',
        'event',
        'user',
        'loan',
        # Django Apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Additional Apps
        'django_tables2',
        'django_filters',
        'raven.contrib.django.raven_compat',
        'debug_toolbar',
        'simple_history',
        'crispy_forms',
        'widget_tweaks',
        'bootstrap_datepicker_plus',

    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'simple_history.middleware.HistoryRequestMiddleware',
    ]

    ROOT_URLCONF = 'Kases.urls'

    DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap-responsive.html'
    CRISPY_TEMPLATE_PACK = "bootstrap4"
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'Kases.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.9/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    ROOT_PATH = os.path.dirname(__file__)
    #STATIC_URL = '/static/'
    #STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates'),]
    #STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))
    STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = ['static/',]
    

class LocalSQLite():
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


class LocalMySql():
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        #'default': {
        #    'ENGINE': 'django.db.backends.sqlite3',
        #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #}
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kases',
            'USER': 'root',
            'PASSWORD': 'coffee',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }


class RemoteMySql():
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kases',
            'USER': 'root',
            'PASSWORD': '21@coffee',
            'HOST': '192.168.2.32',
            'PORT': '3306',
        }
    }


class LocalPostgres():
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        #'default': {
        #    'ENGINE': 'django.db.backends.sqlite3',
        #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #}
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kases',
            'USER': 'root',
            'PASSWORD': 'coffee',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }


class RemotePostgres():
    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kases',
            'USER': 'root',
            'PASSWORD': '21@coffee',
            'HOST': '192.168.2.32',
            'PORT': '3306',
        }
    }


class RedisCache():
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'KEY_PREFIX': 'kases',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                # You may want this. See https://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
                # 'IGNORE_EXCEPTIONS': True, # see
            }
        }
    }
    CACHE_TTL = 60 * 15


class Log():
    RAVEN_CONFIG = {
                'dsn': 'https://b426ed2e887842ce83210c66c7d79c7c:2f4c7e06ce0b4e91be5fad1940821f81@sentry.io/1193654',
                # If you are using git, you can also automatically configure the
                # release based on the git info.
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            }
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }


class Dev(Common, Log):
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    #EMAIL_FILE_PATH = '/tmp/app-emails'
    INTERNAL_IPS = ['127.0.0.1',]

    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'kases',
            'USER': 'root',
            'PASSWORD': '21@coffee',
            'HOST': '192.168.2.32',
            'PORT': '3306',
        }
    }

        # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    #DATABASES = {
    #    'default': {
    #        'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #    }
    #}


class Deployed(Common):
    '''
    Settings which are for a non local deployment, served behind nginx.
    '''
    PUBLIC_ROOT = join(BASE_DIR, '../public/')
    STATIC_ROOT = join(PUBLIC_ROOT, 'static')
    MEDIA_ROOT = join(PUBLIC_ROOT, 'media')
    COMPRESS_OUTPUT_DIR = ''
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'josh.cannons#gmail.com'
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''
    SERVER_EMAIL = ''


class Staging():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getenv('POSTGRES_USER', ''),
            'USER': getenv('POSTGRES_USER', ''),
            'PASSWORD': getenv('POSTGRES_PASSWORD', 'password'),
            'HOST': getenv('POSTGRES_SERVICE_HOST', 'localhost'),
        }
    }


class Production():
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getenv('POSTGRES_USER', ''),
            'USER': getenv('POSTGRES_USER', ''),
            'PASSWORD': getenv('POSTGRES_PASSWORD', 'password'),
            'HOST': getenv('POSTGRES_SERVICE_HOST', 'localhost'),
        }
    }

    ALLOWED_HOSTS = ['.kases.com', ]  # add deployment domain here

    RAVEN_CONFIG = {
        'dsn': ''
    }