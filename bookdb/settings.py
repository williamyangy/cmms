# -*- coding: utf-8 -*-
"""
Django settings for bookdb project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

AUTHENTICATION_BACKENDS = (
    'bookdb.backends.LDAPBackend',
    ('django.contrib.auth.backends.ModelBackend'),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S3_DIR = "https://etp-tms.s3.amazonaws.com/"
#print ("base dir path:%s" % BASE_DIR)
IMG_UPLOAD = os.path.join(BASE_DIR, 'uploads')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hm!apphplhw3dfnz7#%+m2b_s+oegrp##5l3&d!c-#%dmr2ido'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*"]
#ALLOWED_HOSTS = ['10.152.28.16', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'simpleui',
    'bms.apps.BmsConfig',
    'dal',
    'dal_select2',  # must be before admin and grappelli, to override jquery.init.js

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # for template filter like intcomma
    'rest_framework',
    'debug_toolbar',
    # 'widget_tweaks',    # to remove
    'crispy_forms',  #
    'reversion',
    # 'dynamic_rest',     # to remove
    'notifications',
    'django.contrib.admin',
]

AUTH_USER_MODEL = 'bms.User'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    #'DEFAULT_PAGINATION_CLASS': 'base.pagination.CustomPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # rest_framework.pagination.PageNumberPagination - will have page as param
    # LimitOffsetPagination - will have offset and limit params
    'PAGE_SIZE': 5000
}

DJANGO_NOTIFICATIONS_CONFIG = {'SOFT_DELETE': True}

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.middleware.BaseMiddleware',
]

ROOT_URLCONF = 'bookdb.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookdb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {


'default': {
    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'TMS_local',  # Or path to database file if using sqlite3.
    'USER': 'root',  # Not used with sqlite3.
    'PASSWORD': 'root',  # Not used with sqlite3.
    'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '3308',  # Set to empty string for default. Not used with sqlite3.
    }



}



'''
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'TMS_PROD',
    'HOST': 'tmsprod.cl8czkqyfcpi.ap-southeast-1.rds.amazonaws.com',
    'PORT': '3306',
    'USER': 'williamyangy',
    'PASSWORD': '(mYE1M-9W[7a',
}
'''

'''
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}'''













'''
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'TMS_UAT',
    'HOST': 'tmsdev.cl8czkqyfcpi.ap-southeast-1.rds.amazonaws.com',
    'PORT': '3306',
    'USER': 'williamyangy',
    'PASSWORD': '(mYE1M-9W[7a1',
}
'''



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

# USE_TZ = True     # this will enable timezone aware

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'


INTERNAL_IPS = [
    '127.0.0.1',
]

MEDIA_ROOT = os.path.join(BASE_DIR, '')  # this path to point to media file
MEDIA_URL = '/media/'  # this will appear as url

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1200
SESSION_SAVE_EVERY_REQUEST = True