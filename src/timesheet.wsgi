import os,sys
import site

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")

sys.path.append(os.path.join(PROJECT_ROOT,'src/'))
sys.path.append(os.path.join(PROJECT_ROOT,'src/data_apps/'))

sys.path.insert(0, os.path.join(PROJECT_ROOT,'src/venv/lib/python2.6/site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

#on_worker_thread_startup()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
