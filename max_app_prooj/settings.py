"""
Django settings for max_app_prooj project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=&d(1-t@ed44$s0agslv&p=b$z2a5yxr&k9ky69#(kld29)y4a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["django.casualfootwears.com", "www.django.casualfootwears.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #created apps,
    "business",
    "rest_framework",
    "corsheaders"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Use the correct import path
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ]
}

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'max_app_prooj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'max_app_prooj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lighbgsz_django2',
        'USER': 'lighbgsz_max_user',
        'PASSWORD': '?_RVb@AmPDxA',
        'HOST': 'localhost',
        'PORT': '3306',
     'OPTIONS': {
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
    'init_command': "SET sql_mode='';",
}
    }
}
# asa
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_ROOT = "/home/lighbgsz/django.casualfootwears.com/static"
MEDIA_ROOT = "/home/lighbgsz/django.casualfootwears.com/media"

# MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_URL = '/uploads/'

WHATSAPP_URL = 'https://graph.facebook.com/v17.0/128538200341271/messages'
WHATSAPP_TOKEN =  "Bearer EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880