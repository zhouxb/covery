# -*- coding:utf8 -*-

from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from covery.isp.models import Province, Device
from pbl.models import Survey, State
from pbl.helpers import listr_to_textarea, build_survey, MINUTE, HOUR
from plugins.pbl import tasks
from django.conf import settings

def index(request, province_id, template_name='pbl/survey/index.html'):
    province = Province.objects.get(id=province_id)

    tab_pane = request.GET.get('tab_pane', 'IP')

    survey, state = Survey.objects.get_or_create(province=province)

    result = listr_to_textarea(survey)
    result['tab_pane'] = tab_pane
    result['province'] = province

    return render(request, template_name, result)

def update(request, province_id):
    IP = request.POST.get('IP', '')
    domain = request.POST.get('domain', '')
    URL = request.POST.get('URL', '')
    operator = request.POST.get('operator', '')

    survey = Survey.objects.get(province=province_id)
    tab_pane = build_survey(survey, IP, domain, operator, URL)
    messages.success(request, '修改成功!')

    return HttpResponseRedirect('%s?tab_pane=%s' % (reverse('pbl:survey_index', args=(province_id,)), tab_pane))

def show(request, province_id):
    province = Province.objects.get(id=province_id)
    response = Survey.objects.filter(province=province).values('IP', 'domain', 'operator', 'URL')[0]
    response['IP'] = response['IP'].split('|')
    response['domain'] = response['domain'].split('|')
    response['URL'] = response['URL'].split('|')

    return json_response(response)

#def set(request, template_name='pbl/survey/set.html'):
    #survey = Survey.objects.all()[0]
    #try:
        #minute = survey.schedule
        #return render(request, template_name, {'minute':minute})
    #except:
        #pass

    #return render(request, template_name)

def run_now(request, province_id, device_id):
    device = Device.objects.get(id=device_id)
    state = State.objects.create(device=device)

    pbl_survey_show_url = '%s%s' % (
            settings.API_ADDRESS,
            reverse('pbl:survey_show', args=(province_id,))
    )

    pbl_state_create_url = '%s%s' % (
            settings.API_ADDRESS,
            reverse('pbl:state_create', args=(state.id,))
    )

    mail_create_url = '%s%s' % (
            settings.API_ADDRESS,
            reverse('mail:create')
    )

    tasks.probe.apply_async(
            args=
                [
                    pbl_survey_show_url,
                    pbl_state_create_url,
                    mail_create_url,
                ],
            routing_key='pbl.probe.%s' % device.sn,
            exchange=device.sn,
            exchange_type='direct'
    )

    return json_response({'message':'任务已经下发', 'type':'success'})

def run_time(request, province_id):
    minute = request.POST.get('minute', '')

    if minute in MINUTE:
        province = Province.objects.get(id=province_id)
        survey = Survey.objects.get(province=province)
        survey.schedule = '%s' % minute
        survey.save()

        pbl_survey_show_url = '%s/%s' % (
                settings.API_ADDRESS,
                reverse('pbl:survey_show', args=(province.id,))
        )

        pbl_state_schedule_create_url = '%s/%s' % (
                settings.API_ADDRESS,
                reverse('pbl:state_schedule_create')
        )

        mail_create_url = '%s/%s' % (
                settings.API_ADDRESS,
                reverse('mail:create')
        )

        tasks.schedule.apply_async(
            args=
                [
                    pbl_survey_show_url,
                    pbl_state_schedule_create_url,
                    mail_create_url,
                    minute
                ],
            routing_key="pbl.probe.%s" % province.name
        )

        response = {'message':'周期任务已下发', 'type':'success'}
    else:
        response = {'message':'输入时间格式有误,请检测!', 'type':'error'}

    return json_response(response)

