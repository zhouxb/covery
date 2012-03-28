from coffin.conf.urls.defaults import *

urlpatterns = patterns('mail.views',
    url(r'^create$', 'create', name='create'),
)
