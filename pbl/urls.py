from coffin.conf.urls.defaults import *

urlpatterns = patterns('pbl.views.isp',
    url(r'^$', 'index', name='isp_index'),
)

urlpatterns += patterns('pbl.views.survey',
    url(r'^(?P<province_id>\d+)/survey$', 'index', name='survey_index'),
    url(r'^(?P<province_id>\d+)/survey/new$', 'new', name='survey_new'),
    url(r'^(?P<province_id>\d+)/survey/create$', 'create', name='survey_create'),
    url(r'^(?P<province_id>\d+)/survey/(?P<id>\d+)/show$', 'show', name='survey_show'),
    url(r'^(?P<province_id>\d+)/survey/(?P<id>\d+)/update$', 'update', name='survey_update'),
    #url(r'^(?P<province_id>\d+)/survey/_show$', '_show', name='survey__show'),
    url(r'^(?P<province_id>\d+)/survey/(?P<id>\d+)/delete$', 'delete', name='survey_delete'),

    url(r'^(?P<province_id>\d+)/survey/set/device/(?P<device_id>\d+)/run_now$', 'run_now', name='survey_set_run_now'),
    url(r'^(?P<province_id>\d+)/survey/set/run_time$', 'run_time', name='survey_set_run_time'),
)

urlpatterns += patterns('pbl.views.device_survey',
    url(r'^province/(?P<province_id>\d+)/device_survey$', 'index', name='device_survey_index'),
    url(r'^province/(?P<province_id>\d+)/device_survey/update$', 'update', name='device_survey_update'),
)

urlpatterns += patterns('pbl.views.state',
    url(r'^(?P<province_id>\d+)/state$', 'index', name='state_index'),
    url(r'^(?P<province_id>\d+)/device/(?P<device_id>\d+)/state/show$', 'show', name='state_show'),
    url(r'^state/(?P<id>\d+)/delete$', 'delete', name='state_delete'),
    url(r'^state/schedule/create$', 'schedule_create', name='state_schedule_create'),
    url(r'^state/(?P<id>\d+)/create$', 'create', name='state_create'),
)

urlpatterns += patterns('pbl.views.report',
    url(r'^(?P<province_id>\d+)/device/(?P<device_id>\d+)/report/(?P<id>\d+)$', 'show_chart', name='report_show_chart'),
    url(r'^report/(?P<id>\d+)/show_chart_json$', 'show_chart_json', name='report_show_chart_json'),
)

