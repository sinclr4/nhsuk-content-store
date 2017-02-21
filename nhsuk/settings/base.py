"""
Django settings for nhsuk project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'core',
    'api',
    'home',
    'search',
    'pages',
    'images',
    'wagtailmarkdown',
    'nhs_wagtailadmin',
    'corsheaders',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'modelcluster',
    'taggit',
    'oauth2_provider',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bakery',
    'exporter',
    'importer',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'nhsuk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
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

WSGI_APPLICATION = 'nhsuk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'nhsuk'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# API

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope'}
}

# Wagtail settings

WAGTAIL_SITE_NAME = "NHS.UK"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = os.getenv('BASE_URL', 'http://example.com')

WAGTAILIMAGES_IMAGE_MODEL = 'images.Image'

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtailmarkdown.rich_text.SimpleMDETextArea',
        'OPTIONS': {
            'spellChecker': False,
            'placeholder': ' ',
            'toolbar': [
                "bold", "italic", "heading", "|",
                "quote", "unordered-list", "ordered-list", "|",
                "link", "|",
                "guide"
            ],
            'status': False,
        }
    },
}

# base url to the frontend app
# e.g. 'http://localhost:3000'
FRONTEND_BASE_URL = os.environ.get('FRONTEND_BASE_URL', '')

# frontend url that renders the preview data using python format
# e.g. 'http://localhost:3000/preview/{signature}/{page_id}/{revision_id}'
FRONTEND_PREVIEW_URL = os.environ.get('FRONTEND_PREVIEW_URL', '')  #

# IMAGE_SIGNATURE_KEY = None
# PREVIEW_SIGNATURE_KEY = None

# import from github settings
IMPORT_URL_FORMAT = os.environ.get(
    'IMPORT_URL_FORMAT',
    'https://api.github.com/repos/nhsuk/betahealth/contents{url_part}'
)
GITHUB_OAUTH_TOKEN = os.environ.get('GITHUB_OAUTH_TOKEN', '')
