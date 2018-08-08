import os


DEBUG = True

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'inline_static',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_ROOT,
)
