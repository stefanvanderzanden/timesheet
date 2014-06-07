import os
from settings import BASE_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# sqlite is the quick an easy development db
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'timesheet',
      'USER': 'timesheet',             # Not used with sqlite3.
      'PASSWORD': 'timesheet',         # Not used with sqlite3.
      'HOST': '',             # Not used with sqlite3.
      'PORT': '',             # Not used with sqlite3.
  }
}
