from coffin.conf.urls.defaults import *
from sample.api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('sample.views',
    (r'^$', 'index'),
)

urlpatterns += patterns('',
    (r'^api/', include(entry_resource.urls)),
)

