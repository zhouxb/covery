from coffin.conf.urls.defaults import *

urlpatterns = patterns('pbl.views.isp',
    url(r'^isp$', 'index', name='isp_index'),
)

urlpatterns += patterns('pbl.views.survey',
    url(r'^isp/(?P<province_id>\d+)/survey$', 'index', name='survey_index'),
    url(r'^isp/(?P<province_id>\d+)/survey/update$', 'update', name='survey_update'),
    url(r'^isp/(?P<province_id>\d+)/survey/show$', 'show', name='survey_show'),
    url(r'^isp/(?P<province_id>\d+)/survey/set$', 'set', name='survey_set'),
    url(r'^isp/(?P<province_id>\d+)/survey/set/run_now$', 'run_now', name='survey_set_run_now'),
    url(r'^isp/(?P<province_id>\d+)/survey/set/run_time$', 'run_time', name='survey_set_run_time'),
)

urlpatterns += patterns('pbl.views.state',
    url(r'^isp/(?P<province_id>\d+)/state$', 'index', name='state_index'),
    url(r'^isp/(?P<province_id>\d+)/state/(?P<device_id>\d+)/show$', 'show', name='state_show'),
    url(r'^state/schedule/create$', 'schedule_create', name='state_schedule_create'),
    url(r'^isp/state/(?P<id>\d+)/create$', 'create', name='state_create'),
    url(r'^isp/state/(?P<id>\d+)/show_json$', 'show_json', name='state_show_json'),
    url(r'^isp/state/(?P<id>\d+)/delete$', 'delete', name='state_delete'),
)

