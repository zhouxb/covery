from coffin.conf.urls.defaults import *

urlpatterns = patterns('pbl.views.survey',
    url(r'^survey$', 'index', name='survey_index'),
    url(r'^survey/update$', 'update', name='survey_update'),
    url(r'^survey/show$', 'show', name='survey_show'),
    url(r'^survey/set$', 'set', name='survey_set'),
    url(r'^survey/set/run_now$', 'run_now', name='survey_set_run_now'),
    url(r'^survey/set/run_time$', 'run_time', name='survey_set_run_time'),
)

urlpatterns += patterns('pbl.views.state',
    url(r'^state$', 'index', name='state_index'),
    url(r'^state/(?P<id>\d+)/create$', 'create', name='state_create'),
    url(r'^state/show$', 'show', name='state_show'),
)
