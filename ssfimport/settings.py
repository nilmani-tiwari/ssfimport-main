"""
Django settings for ssfimport project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os


import socket

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'

def get_env_setting(setting, default=None):
    setting_value = os.environ.get(setting, default)
    if setting_value is None:
        return None
        # raise ImproperlyConfigured("Set the %s env variable" % setting)
    else:
        return setting_value

print()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '2qe*9kw(!2p60$-65zx&eoe0(*mcxj-b=^hkji(=h8qe6&#2mo'


# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = '2qe*9kw(!2p60$-65zx&eoe0(*mcxj-b=^hkji(=h8qe6&#2mo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*',"159.89.175.153","54.146.148.119","ec2-54-146-148-119.compute-1.amazonaws.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    #  'login',

    'ssftemp',
    # 'localwp',
    'storages',
    'ssf',
    'hitcount',
    'posts',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'paypal.standard.ipn',
    "paypal_payment",
    'django_cron',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



CRON_CLASSES = [
    "paypal_payment.cron.MyCronJob",
    # ...
]


CRONJOBS = [
    ('0 0 * * *', 'paypal_payment.cron.my_cron_job')
]

ROOT_URLCONF = 'ssfimport.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')]
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'ssfimport.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'UTC'  # use this, whenever possible
TIME_ZONE = 'Europe/Berlin'
# TIME_ZONE = 'Etc/GMT+1'
# USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/




SSF_LOCAL_DB = {
    'host': '52.71.134.206',
    'port': 3306,
    'username': 'root',
    'password': 'GsFYX8zX3vUt',
    'db_name': 'bitnami_wordpress'
}

# DB_URL = get_env_setting('DB_URL', 'postgres://postgres:postgres@localhost:5432/ssf')
# # DB_URL = get_env_setting('DATABASE_URL')


# DB_USER = DB_URL.split('postgres://')[1].split(':')[0]
# DB_PASS = DB_URL.split('postgres://')[1].split(':')[1].split('@')[0]
# DB_HOST = DB_URL.split('postgres://')[1].split(':')[1].split('@')[1]
# DB_PORT = DB_URL.split('postgres://')[1].split(':')[2].split('/')[0]
# DB_NAME = DB_URL.split('postgres://')[1].split(':')[2].split('/')[1]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # 'NAME': 'ssf',
#         # 'USER': 'postgres',
#         # 'PASSWORD': 'postgres',
#         # 'HOST': 'localhost',
#         # 'PORT': 5432,
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASS,
#         'HOST': DB_HOST,
#         'PORT': DB_PORT,
#     },
#     'wp': {
#         'NAME': SSF_LOCAL_DB.get('db_name'),
#         'ENGINE': 'django.db.backends.mysql',
#         'USER': SSF_LOCAL_DB.get('username'),
#         'PASSWORD': SSF_LOCAL_DB.get('password'),
#         'HOST': SSF_LOCAL_DB.get('host'),
#         'PORT': SSF_LOCAL_DB.get('port')
#     }
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },

    },
]

# SSF_DB = {
#     'host': 'sexsmartfilms.com',
#     'port': 3306,
#     'username': 'sexsmartopen',
#     'password': 'sEZfdeWqFF2r6tGA',
#     'db_name': 'sexsmart_portal'
# }

VIDEO_BASE = 'https://s3.amazonaws.com/wp-ssf/vids/'
THUMB_BASE = 'https://s3.amazonaws.com/wp-ssf/thumbs/'
WORDPRESS_BASE = 'http://127.0.0.1/'

# TODO: Change ratings to 1-to-5 instead of 1-to-10
# TODO: VOD Access is one day


# Done: Find missing comments
#       This is because 355 comments are on videos which don't exist anymore or by subscribers which have been deleted.


# Done: Find old rating DB
#       The old system instead of storing individual ratings, is only storing aggregate. So we can show those, but calculation of next ratings would break. This is a side-effect of a badly designed system so we'll have to live with this loss.

# Review: Download videos
#       Done. 85GB. So will take time if we want to reupload. If we want to serve them from the same folder, that's great.




# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]



# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles'), ]


FIXTURE_DIRS = (
      os.path.join(BASE_DIR, "fixtures",),
)

STATIC_URL = '/static/'
STATICFILES_DIRS=[STATIC_DIR,]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'





# PAYPAL_RECEIVER_EMAIL = 'nilmani085@mail.com' #testing
PAYPAL_RECEIVER_EMAIL = 'mark@sexsmartfilms.com'
PAYPAL_TEST = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1
LOGIN_REDIRECT_URL = 'login:profile'

# AWS_QUERYSTRING_AUTH = False
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




# AWS_ACCESS_KEY_ID = 'AKIAYG3K3RBCXEQU4TVP'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_ENDPOINT_URL = 'http://website.s3-website.us-east-1.amazonaws.com'
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = 'us-east-1'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'AKIAZO42BYDA4YRD4R77'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_ENDPOINT_URL = 'https://s3.us-east-1.amazonaws.com/'
AWS_STORAGE_BUCKET_NAME = 'new-ssf'


S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        # 'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    },
}


S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        # "key" [required] The location to upload file
        #       1. String: folder path to upload to
        #       2. Function: generate folder path + filename using a function  
        'key': 'uploads/images',

        # "auth" [optional] Limit to specfic Django users
        #        Function: ACL function
        'auth': lambda u: u.is_staff,

        # "allowed" [optional] Limit to specific mime types
        #           List: list of mime types
        'allowed': ['image/jpeg', 'image/png', 'video/mp4'],
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],

        # "bucket" [optional] Bucket if different from AWS_STORAGE_BUCKET_NAME
        #          String: bucket name
        'bucket': 'new-ssf',

        # "endpoint" [optional] Endpoint if different from AWS_S3_ENDPOINT_URL
        #            String: endpoint URL
        'endpoint': 'https://s3.us-east-1.amazonaws.com/',

        # "region" [optional] Region if different from AWS_S3_REGION_NAME
        #          String: region name
        'region': 'us-east-1', # Default is 'AWS_S3_REGION_NAME'

        # "acl" [optional] Custom ACL for object, default is 'public-read'
        #       String: ACL
        'acl': 'private',

        # "cache_control" [optional] Custom cache control header
        #                 String: header
        'cache_control': 'max-age=2592000',

        # "content_disposition" [optional] Custom content disposition header
        #                       String: header
        'content_disposition': lambda x: 'attachment; filename="{}"'.format(x),

        # "content_length_range" [optional] Limit file size
        #                        Tuple: (from, to) in bytes
        'content_length_range': (5000, 20000000),

        # "server_side_encryption" [optional] Use serverside encryption
        #                          String: encrytion standard
        'server_side_encryption': 'AES256',

        # "allow_existence_optimization" [optional] Checks to see if file already exists,
        #                                returns the URL to the object if so (no upload)
        #                                Boolean: True, False
        'allow_existence_optimization': False,
    },
    'example_destination_two': {
        'key': lambda filename, args: args + '/' + filename,
    	'key_args': 'uploads/images',
    }
}
