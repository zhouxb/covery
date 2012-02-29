from coffin.conf.urls.defaults import *

urlpatterns = patterns('account.views.profile',
    url(r'^$', 'index', name='index'),
    url(r'^profile$', 'index', name='profile_index'),
    url(r'^profile/update$', 'update', name='profile_update'),
)

urlpatterns += patterns('',
    (r'^device/', include('device.urls')),
)
