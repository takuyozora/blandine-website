"""
Django settings for BlandineWebSite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6u85sltma2kz_px&64y4)knxq*4-me2l_pey27pj6@87=r!s2@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'tinymce',
    'ckeditor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'main.middleware.AdminLocaleMiddleware',
)

ROOT_URLCONF = 'BlandineWebSite.urls'

WSGI_APPLICATION = 'BlandineWebSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'
ADMIN_LANGUAGE_CODE = 'fr-FR'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)


## CKEDIT
STATIC_ROOT = os.path.join(BASE_DIR,"static")
MEDIA_ROOT = os.path.join(BASE_DIR,"static/media")
MEDIA_URL = "/media/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND='pillow'

CKEDITOR_CONFIGS = {

    "default": {
        # "removePlugins": "stylesheetparser",
        'toolbar': 'Full',

    }

}


## TINYMCE
# STATIC_ROOT = os.path.join(BASE_DIR,"static")
# print(STATIC_ROOT)
TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_JS_ROOT = '/media/tiny_mce/'
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce_src.js")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
}
TINYMCE_SPELLCHECKER = True

