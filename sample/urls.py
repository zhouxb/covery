from coffin.conf.urls.defaults import *

urlpatterns = patterns('sample.views',
    (r'^$', 'index'),
    url(r'^demo$', 'demo', name='demo'),
    url(r'^demo1$', 'demo1', name='demo1'),
)

