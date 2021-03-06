import os
from configparser import RawConfigParser

from .base import *

# https://stackoverflow.com/questions/44693485/where-do-i-set-environment-variables-for-django (Braden Holt)
config = RawConfigParser()
config['DEFAULT'] = {'ALLOWED_HOSTS': '*'}
config.read('/etc/django/magyarfurdo/env.ini')

DEBUG = False

SECRET_KEY = os.environ.get('MZ_SECRET_KEY') or config.get('main', 'SECRET_KEY')

ALLOWED_HOSTS = (os.environ.get('MZ_ALLOWED_HOSTS') or config.get('main', 'ALLOWED_HOSTS')
                 ).replace(',', ' ').replace(';', ' ').split()

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
