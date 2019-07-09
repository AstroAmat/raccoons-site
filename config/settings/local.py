"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = env.bool('DJANGO_DEBUG', True)

# Security

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='4ra7dxrd(&tmw$b5s9--akuakuisreal0v4!!f_-h7i)b_96aw'
)

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Templates

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Development apps

INSTALLED_APPS += [
    'django_extensions',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

MIDDLEWARE += [
    
]

MEDIA_URL = '/media/'
MEDIA_ROOT = APPS_DIR / 'media'

# Security

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

# Email
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = env('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')