from .base import *
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True





ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = '587'
    EMAIL_USE_TLS = 'True'
    DEFAULT_FROM_EMAIL = 'Remote Pharmacy Team <noreply@iwproject.com>'
