import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath('/usr/local/lib/python2.6/site-packages'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'covery.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
