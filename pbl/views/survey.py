# -*- coding:utf8 -*-

from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from pbl.models import Survey, State
from pbl.helpers import listr_to_textarea, build_survey, MINUTE, HOUR
from plugins.pbl import tasks

def index(request, template_name='pbl/survey/index.html'):
    tab_pane = request.GET.get('tab_pane', 'IP')
    survey = Survey.objects.get(id=1)
    result = listr_to_textarea(survey)
    result['tab_pane'] = tab_pane
    return render(request, template_name, result)

def update(request):
    IP = request.POST.get('IP', '')
    domain = request.POST.get('domain', '')
    URL = request.POST.get('URL', '')
    operator = request.POST.get('operator', '')

    survey = Survey.objects.get(id=1)
    tab_pane = build_survey(survey, IP, domain, operator, URL)
    messages.success(request, '修改成功!')

    return HttpResponseRedirect('%s?tab_pane=%s' % (reverse('pbl:survey_index'), tab_pane))

def show(request):
    response = Survey.objects.values('IP', 'domain', 'operator', 'URL')[0]
    response['IP'] = response['IP'].split('|')
    response['domain'] = response['domain'].split('|')
    response['URL'] = response['URL'].split('|')

    return json_response(response)

def set(request, template_name='pbl/survey/set.html'):
    #state = State.objects.create(survey=Survey.objects.all()[0])
    #id = state.id

    #tasks.probe.apply_async(args=[
        #'http://192.168.10.84:8000/pbl/survey/show',
        #'http://192.168.10.84:8000/pbl/state/%s/create' % id
    #])
    survey = Survey.objects.all()[0]
    try:
        minute, hour = survey.schedule.split('|')
        return render(request, template_name, {'minute':minute, 'hour':hour})
    except:
        pass

    return render(request, template_name)

def run_now(request):
    state = State.objects.create(survey=Survey.objects.all()[0])
    id = state.id

    tasks.probe.apply_async(args=[
        'http://192.168.10.84:8000/pbl/survey/show',
        'http://192.168.10.84:8000/pbl/state/%s/create' % id
    ])

    return json_response({'message':'任务已经下发', 'type':'success'})

def run_time(request):
    minute = request.POST.get('minute', '')
    hour = request.POST.get('hour', '')

    if minute in MINUTE and hour in HOUR:
        survey = Survey.objects.all()[0]
        survey.schedule = '%s|%s' % (minute, hour)
        survey.save()
        response = {'message':'周期任务已下发', 'type':'success'}
    else:
        response = {'message':'输入时间格式有误,请检测!', 'type':'error'}

    return json_response(response)

