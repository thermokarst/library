from .shared import (
    BASE_DIR,
    PROJ_DIR,
    SECRET_KEY,
    DEBUG,
    ALLOWED_HOSTS,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    WSGI_APPLICATION,
    DATABASES,
    AUTH_PASSWORD_VALIDATORS,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    STATIC_URL,
    STATICFILES_DIRS,
    STATIC_ROOT,
    APPEND_SLASH,
    LOGIN_URL,
    LOGOUT_REDIRECT_URL,
    EMAIL_BACKEND,
    ADMINS,
    AUTH_USER_MODEL,
    RABBITMQ_URL,
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    CELERY_RESULT_SERIALIZER,
    CELERY_TASK_ROUTES,
    GITHUB_TOKEN,
)


__all__ = [
    'BASE_DIR',
    'PROJ_DIR',
    'SECRET_KEY',
    'DEBUG',
    'ALLOWED_HOSTS',
    'INSTALLED_APPS',
    'MIDDLEWARE',
    'ROOT_URLCONF',
    'TEMPLATES',
    'WSGI_APPLICATION',
    'DATABASES',
    'AUTH_PASSWORD_VALIDATORS',
    'LANGUAGE_CODE',
    'TIME_ZONE',
    'USE_I18N',
    'USE_L10N',
    'USE_TZ',
    'STATIC_URL',
    'STATICFILES_DIRS',
    'STATIC_ROOT',
    'APPEND_SLASH',
    'INTERNAL_IPS',
    'LOGIN_URL',
    'LOGOUT_REDIRECT_URL',
    'EMAIL_BACKEND',
    'ADMINS',
    'AUTH_USER_MODEL',
    'RABBITMQ_URL',
    'CELERY_BROKER_URL',
    'CELERY_RESULT_BACKEND',
    'CELERY_RESULT_SERIALIZER',
    'CELERY_TASK_ROUTES',
    'GITHUB_TOKEN',
]

MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware'
])
INTERNAL_IPS = ['127.0.0.1', 'localhost']
INSTALLED_APPS = ['whitenoise.runserver_nostatic', *INSTALLED_APPS, 'debug_toolbar']
