"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+tnzpomyh3vk(0t@6uxn-@2%l7)+k20^t(!k@xwh10g97r$o7f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    'app',
    'corsheaders',
    "djoser",
    'rest_framework_simplejwt',
    "rest_framework_simplejwt.token_blacklist",
]
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]

}
SIMPLE_JWT = {
    # 'AUTH_HEADER_TYPES': ('JWT'),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=36325),   # Short access token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=36325),      # Refresh token expires and blacklists after 1 day
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,  # Ensure refresh tokens are blacklisted after expiration
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'bysalman5@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'zvsc nvjj issr wxej'  # Your Gmail app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DJOSER = {
    # 'PASSWORD_RESET_CONFIRM_URL': 'books/auth/users/reset_password_confirm/{uid}/{token}/',
   'PASSWORD_RESET_CONFIRM_URL': 'password-reset/confirm/{uid}/{token}/',
    # 'BASE_URL': 'http://localhost:5300',  # Optional
}
DOMAIN = 'kaamiltechnician.com'
SITE_NAME = 'kaamil;'
ROOT_URLCONF = 'api.urls'



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.parse(
#         "postgresql://goodir_user:AoO6gDX2pQCqEHGTQaR7hPLbkDABwCrL@dpg-ctcjbgtds78s739f2p40-a.oregon-postgres.render.com/goodir"
#     )
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'goodir',
        'USER': 'goodir_user',
        'PASSWORD': 'AoO6gDX2pQCqEHGTQaR7hPLbkDABwCrL',
        'HOST': 'dpg-ctcjbgtds78s739f2p40-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}
# DATABASES['default']=dj_database_url.parse("postgresql://goodir_user:AoO6gDX2pQCqEHGTQaR7hPLbkDABwCrL@dpg-ctcjbgtds78s739f2p40-a.oregon-postgres.render.com/goodir")
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static files storage for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Change this for production
    "https://kaamiltechnician.com","https://www.kaamiltechnician.com","https://test.goodirtechnology.com",
]
ALLOWED_HOSTS = [
    '51.20.127.111',  # Replace with your AWS public IP
    'localhost',      # For local access
    '127.0.0.1',      # For local development
    'api.kaamiltechnician.com',
    "goodir-samble.onrender.com"
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AUTH_USER_MODEL = 'app.CustomUser'
