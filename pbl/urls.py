from coffin.conf.urls.defaults import *

urlpatterns = patterns('pbl.views.survey',
    url(r'^survey$', 'index', name='survey_index'),
    url(r'^survey/set$', 'set', name='survey_set'),
    url(r'^survey/update$', 'update', name='survey_update'),
    url(r'^survey/show$', 'show', name='survey_show'),
)

urlpatterns += patterns('pbl.views.state',
    url(r'^state$', 'index', name='state_index'),
    url(r'^state/(?P<id>\d+)/create$', 'create', name='state_create'),
)
