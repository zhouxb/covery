from coffin.conf.urls.defaults import *

urlpatterns = patterns('isp.views.province',
    url(r'^provinces$', 'index', name='province_index'),
    url(r'^province/create$', 'create', name='province_create'),
    url(r'^province/(?P<id>\d+)/delete$', 'delete', name='province_delete'),
    url(r'^province/(?P<id>\d+)/show$', 'show', name='province_show'),
)

urlpatterns += patterns('isp.views.device',
    url(r'^province/(?P<province_id>\d+)/devices$', 'index', name='device_index'),
    url(r'^province/(?P<province_id>\d+)/create$', 'create', name='device_create'),
    url(r'^province/(?P<province_id>\d+)/device/(?P<id>\d+)/delete$', 'delete', name='device_delete'),
    url(r'^province/(?P<province_id>\d+)/show$', 'show', name='device_show'),
)
