from coffin.conf.urls.defaults import *

urlpatterns = patterns('csp.views.device_statis',
    (r'^devices$', 'index'),
    (r'^device/search/', include('haystack.urls')),
    #(r'^devices/about$', 'about'),
)

