from .base import *
SECRET_KEY = 'onl-j-cwq=^y+4k!7d0w-i%g_!wro7s91p3bw-hn!9uxve^ury'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True





ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'sushpalikhe85@gmail.com'
    EMAIL_HOST_PASSWORD = 'hjyxawbugjxtucge'
    EMAIL_PORT = '587'
    EMAIL_USE_TLS = 'True'
    DEFAULT_FROM_EMAIL = 'Remote Pharmacy Team <noreply@iwproject.com>'


MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'
