from coffin.conf.urls.defaults import *

urlpatterns = patterns('account.views.profile',
    (r'^$', 'index'),
    (r'^profile$', 'index'),
    (r'^profile/update$', 'update'),

    (r'^device/', include('device.urls')),

)

