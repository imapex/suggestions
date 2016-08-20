# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from django_suggestions.settings.common import *  # noqa

# # DEBUG
# # ------------------------------------------------------------------------------
# DEBUG = env.bool('DJANGO_DEBUG', default=True)
# TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
#
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')
ALLOWED_HOSTS = '*'
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

#
#
# # CACHING
# # ------------------------------------------------------------------------------
# CACHES = {
#     'default': {
#         'BACKEND' : 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': ''
#     }
# }
#
# # TESTING
# # ------------------------------------------------------------------------------
# TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# # Your local stuff: Below this line define 3rd party library settings
