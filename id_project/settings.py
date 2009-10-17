#import socket

#if socket.gethostname() == 'macmini.local':
    #DEBUG = TEMPLATE_DEBUG = True
#else:
    #DEBUG = TEMPLATE_DEBUG = False

DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''
DATABASE_NAME = ''

TIME_ZONE = 'Australia/Brisbane'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v04#ky__^2refuj&j*)7d1m%^ue9)0+l-mt%n7+jq#1&u)2+or'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'id_project.urls'

#TEMPLATE_DIRS = ('/home/slark/webapps/integraldiagrams/id_project/id_app'
TEMPLATE_DIRS = ('/Users/stephenlark/python/integraldiagrams/id_project/id_app'
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'id_project.id_app'
)
