from coffin.conf.urls.defaults import *

urlpatterns = patterns('crawler.views',
    url(r'^$', 'index', name='index'),
    url(r'^create$', 'create', name='create'),
    url(r'^(?P<id>\d+)/run$', 'run', name='run'),
    url(r'^(?P<id>\d+)/delete$', 'delete', name='delete'),
    url(r'^(?P<id>\d+)/show$', 'show', name='show'),
    url(r'^(?P<id>\d+)/status$', 'status', name='status'),
)
