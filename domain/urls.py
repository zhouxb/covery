from coffin.conf.urls.defaults import *

urlpatterns = patterns('domain.views',
    url(r'^$', 'index', name='index'),
    url(r'^create$', 'create', name='create'),
    url(r'^(?P<id>\d+)/delete$', 'delete', name='delete'),
    url(r'^(?P<task_id>\d+)/show$', 'show', name='show'),
)
