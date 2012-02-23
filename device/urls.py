from coffin.conf.urls.defaults import *

urlpatterns = patterns('device.views.itself',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)/delete', 'delete'),
    (r'^new$', 'new'),
    (r'^create$', 'create'),
    (r'^(?P<id>\d+)/show$', 'show'),
    (r'^(?P<id>\d+)/update$', 'update'),
    (r'^update_status', 'update_status'),
)

urlpatterns += patterns('device.views.order',
    (r'^order$', 'index'),
    (r'^order/new$', 'new'),
    (r'^order/create$', 'create'),
    (r'^(?P<id>\d+)/order/delete', 'delete'),
)

urlpatterns += patterns('device.views.statis',
    (r'^statis$', 'index'),
)
