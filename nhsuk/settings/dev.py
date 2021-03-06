from __future__ import absolute_import, unicode_literals

import sys

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-rpg5bvu3c7%azqqt0nr=g2#6x^*4=1eowymoear!ad#c1*kum'
IMAGE_SIGNATURE_KEY = 'z7G3uULhCY~/TN,fP4sAK_xzUsYPn]tLY(}9FH84YSFC1>3OJ`'
PREVIEW_SIGNATURE_KEY = 'mxwtt97p8[)89+Qm8xwMWTXK](Qc&MhdT=dW72bfhL/du4({sR'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILAPI_BASE_URL = "http://localhost:8000"


# importing test settings file if necessary
if sys.argv[1:2] == ['test']:
    from .testing import *  # noqa


try:
    from .local import *  # noqa
except ImportError:
    pass
