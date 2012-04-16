import os
import sys

workpath = "%s/../" % os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(workpath))
sys.path.append(os.path.abspath('/usr/local/lib/python2.6/site-packages'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
