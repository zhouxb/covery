import os, sys
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(CURRENT_PATH, 'templates')

# Django settings for covery project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

#EMAIL_HOST = 'smtp.yoursite.com'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'your_account'
#EMAIL_HOST_PASSWORD = 's3cret'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'covery',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

if DEBUG and 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'covery.db',                      # Or path to database file if using sqlite3.
        }
    }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/tmp/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(CURRENT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=j_ui5-kb(*z%!h7zs9=m&ftgkb)*)1+18nkr1vr3yp4e0ox(('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'contrib.context_processors.current_user',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'contrib.auth.middleware.RequireLoginMiddleware',
)

import ldap
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_SERVER_URI = "ldap://ccldap.chinacache.com"
AUTH_LDAP_BIND_DN = 'cn=2,cn=Users,dc=chinacache,dc=local'
AUTH_LDAP_BIND_PASSWORD = 'qwer1234!'
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=chinacache,dc=chinacache,dc=local", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
    "email": "mail"
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_ldap.backend.LDAPBackend',
)

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/account'

LOGIN_REQUIRED_URLS = (
        r'/account/',
        r'/csp/',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = ()

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admindocs',
    'django.contrib.admin',

    'south',
    'coffin',
    #'haystack',
    'djcelery',

    'account',
    'crawler',
    'domain',
    'pbl',
    'mail',
    'isp',
    'util',
)

if DEBUG:

    INSTALLED_APPS += (
        'django_nose',
    )
    #if 'crawler' in sys.argv:

        #TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'

#TEST_APPS = ('broker',)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(CURRENT_PATH, 'whoosh_index')
    }
}


AUTH_PROFILE_MODULE = 'account.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#JINJA2_FILTERS = (
    #'path.to.myfilter',
#)

#JINJA2_TESTS = {
    #'test_name': 'path.to.mytest',
#}

#JINJA2_EXTENSIONS = (
    #'jinja2.ext.do',
#)


import djcelery
djcelery.setup_loader()

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

#CELERY_QUEUES = {
    #"default": {
        #"binding_key": "task.#",
    #},
    #"crawlers": {
        #"binding_key": "crawler.#",
    #},
    #"pbls": {
        #"binding_key": "pbl.#",
    #},
#}

#CELERY_DEFAULT_QUEUE = "default"
#CELERY_DEFAULT_EXCHANGE = "tasks"
#CELERY_DEFAULT_EXCHANGE_TYPE = "topic"
#CELERY_DEFAULT_ROUTING_KEY = "task.default"

#CELERY_ROUTES = {
    #'crawler.tasks.crawl':
    #{
        #'queue': 'crawlers',
        #'routing_key':'crawler.crawl',
    #},
    #'pbl.tasks.probe':
    #{
        #'queue': 'pbls',
        #'routing_key':'pbl.probe',
    #},
#}

# Mail config
SMTP_HOST = 'corp.chinacache.com'

# Native address
ip = os.popen("/sbin/ifconfig | grep 'inet addr' | grep -v '127.0.0.1' | awk '{print $2}'").read()
IP= ip[ip.find(':')+1:ip.find('\n')]
PORT = 8000
API_ADDRESS = 'http://%s:%s' % (IP, PORT)

