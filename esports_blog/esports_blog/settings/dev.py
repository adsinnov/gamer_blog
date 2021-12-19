import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%_ai1!n#6qen$ml+ai5#@(7&*0vo(a)a31&zp0cgzai_h)c%)m'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    # 'debug_toolbar'
]

MIDDLEWARE = MIDDLEWARE + [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',

    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

# INTERNAL_IPS = (
#
#     '127.0.0.1', '172.17.0.1'
#
# )
cwd = os.getcwd()
CACHES = {
    "default": {
        # "BACKEND" : "django.core.cache.backends.filebased.FileBasedCache",
        # "LOCATION" : f"{cwd}/.cache"
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


try:
    from .local import *
except ImportError:
    pass
