from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^crawler/', include('crawler.urls', namespace='crawler', app_name='crawler')),
    url(r'^domain/', include('domain.urls', namespace='domain', app_name='domain')),

    url(r'^sample/', include('sample.urls', namespace='sample', app_name='sample')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
)

urlpatterns += staticfiles_urlpatterns()

