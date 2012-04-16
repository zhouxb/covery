from coffin.conf.urls.defaults import *

urlpatterns = patterns('mail.views',
    url(r'^index$', 'index', name='index'),
    url(r'^(?P<id>\d+)/delete$', 'delete', name='delete'),
    url(r'^create$', 'create', name='create'),
)
