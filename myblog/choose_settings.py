# choose settings between Developement and Deploy
import os
import platform

node = platform.node()
dev_machines = ('syuu-PC', 'syuu.local',)

if node in dev_machines:
    # folder My_Blog
    myblog = os.path.dirname(os.path.dirname(__file__))
    # project dir, contains static and media folder under DEV environment
    PROJECT_DIR = os.path.dirname(myblog)
    DEBUG = False
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
    TEMPLATE_DIRS = [os.path.join(My_Blog, 'templates')]
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = False
    PROJECT_DIR = '/home/laike9m/Envs/blog/My_Blog/'
    MEDIA_ROOT = '/project/myblog/media/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/project/myblog/static/'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '.laike9m.com',
    ]

    # cache entire site
    MIDDLEWARE_CLASSES_ADDITION_FIRST = (
        'django.middleware.cache.UpdateCacheMiddleware',
    )

    MIDDLEWARE_CLASSES_ADDITION_LAST = (
        'django.middleware.cache.FetchFromCacheMiddleware',
    )

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
