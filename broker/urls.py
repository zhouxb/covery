from coffin.conf.urls.defaults import *

urlpatterns = patterns('broker.views',
    url(r'^$', 'index', name='index'),
)

