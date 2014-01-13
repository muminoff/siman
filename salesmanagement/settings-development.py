import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'mv4sz+4t*o7!r3mn+25=o87w^h6t@-wn#*ua*e0a7ebc*sx=ka'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
) 
ROOT_URLCONF = 'salesmanagement.urls' 
WSGI_APPLICATION = 'salesmanagement.wsgi.application' 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LANGUAGE_CODE = 'ko-kr' 
TIME_ZONE = 'UTC' 
_ = lambda s: s
LANGUAGES = (
    ('ko', _('Korean')),
    ('en', _('English')),
)
USE_I18N = True 
USE_L10N = True 
USE_TZ = True 
STATIC_URL = '/static/'
INSTALLED_APPS += ( 'core', )
INSTALLED_APPS += ( 'south', )
INSTALLED_APPS += ( 'rosetta', )
