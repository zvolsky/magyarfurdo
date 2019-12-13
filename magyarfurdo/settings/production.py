import os

from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('MZ_SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('MZ_ALLOWED_HOSTS', '*').replace(',', '').replace(';', '').split()

X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 300
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


try:
    from .local import *
except ImportError:
    pass
