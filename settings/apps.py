DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'gunicorn',
    'spurl',
    'django_extensions',
    'sorl.thumbnail',
    'social.apps.django_app.default',
)

PROJECT_APPS = (
    'common',
    'profiles',
    'posts',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
