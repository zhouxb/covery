from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discovery.views.home', name='home'),
    # url(r'^discovery/', include('discovery.foo.urls')),

    (r'^$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

    (r'^account/', include('account.urls')),
    (r'^sample/', include('sample.urls')),
    (r'^csp/', include('csp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
)

urlpatterns += staticfiles_urlpatterns()

