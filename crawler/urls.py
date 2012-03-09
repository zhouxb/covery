from coffin.conf.urls.defaults import *

urlpatterns = patterns('crawler.views',
    url(r'^$', 'index', name='index'),
    url(r'^create$', 'create', name='create'),
    url(r'^(?P<id>\d+)/show$', 'show', name='show'),
)
