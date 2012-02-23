from coffin.conf.urls.defaults import *

urlpatterns = patterns('csp.views',
    (r'^devices$', 'index'),
    (r'^device/new', 'new'),
    (r'^device/create', 'create'),
    (r'^device/(?P<id>\d+)/show$', 'show'),
    (r'^device/(?P<id>\d+)/update', 'update'),
    (r'^device/(?P<id>\d+)/delete', 'delete'),

    (r'^devices/batch$', 'batch'),
    (r'^devices/batch_create$', 'batch_create'),

    (r'^devices/about$', 'about'),
)

