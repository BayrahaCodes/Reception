import os
from pathlib import Path
import dj_database_url

# -------------------------
# BASE DIR
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECURITY
# -------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
DEBUG = False  # Turn off in production!

ALLOWED_HOSTS = [
    'your-app-name.onrender.com',  # Replace with your Render app URL
    'localhost',
    '127.0.0.1',
]

# -------------------------
# INSTALLED APPS
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # your apps here
]

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- required for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
# URLS
# -------------------------
ROOT_URLCONF = 'receivetion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # adjust if you have templates
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

WSGI_APPLICATION = 'receivetion.wsgi.application'

# -------------------------
# DATABASE (Render PostgreSQL)
# -------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES
# -------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']  # optional if you have a local static folder
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------
# DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# SECURITY PROXY (HTTPS)
# -------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
