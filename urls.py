from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_PATH

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discovery.views.home', name='home'),
    # url(r'^discovery/', include('discovery.foo.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_PATH}),

    (r'^sample/', include('sample.urls')),

    (r'^csp/', include('csp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

