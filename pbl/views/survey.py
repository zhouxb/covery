# -*- coding:utf8 -*-

from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from covery.isp.models import Province, Device
from pbl.models import Survey, State, DeviceSurvey
from pbl.helpers import listr_to_textarea, build_survey, MINUTE, HOUR
from plugins.pbl import tasks
from django.conf import settings

def index(request, province_id, template_name='pbl/survey/index.html'):
    province = Province.objects.get(id=province_id)
    surveys = province.survey_set.all()
    return render(request, template_name, {'province':province, 'surveys':surveys})

def new(request, province_id, template_name='pbl/survey/new.html'):
    province = Province.objects.get(id=province_id)
    return render(request, template_name, {'province':province})

def create(request, province_id):
    IP = request.POST.get('IP', '')
    domain = request.POST.get('domain', '')
    URL = request.POST.get('URL', '')
    operator = request.POST.get('operator', '')

    province = Province.objects.get(id=province_id)
    survey = Survey()
    survey.province = province

    try:
        build_survey(survey, IP, domain, operator, URL)
        messages.success(request, '添加成功!')
    except:
        messages.error(request, '出口策略已经存在')

    return HttpResponseRedirect(reverse('pbl:device_survey_index', args=(province_id,)))

def show(request, province_id, id, template_name='pbl/survey/show.html'):
    province = Province.objects.get(id=province_id)
    survey = Survey.objects.get(id=id)
    result = listr_to_textarea(survey)
    result['province'] = province
    result['survey'] = survey

    return render(request, template_name, result)

def update(request, province_id, id):
    IP = request.POST.get('IP', '')
    domain = request.POST.get('domain', '')
    URL = request.POST.get('URL', '')
    operator = request.POST.get('operator', '')

    survey = Survey.objects.get(id=id)
    try:
        build_survey(survey, IP, domain, operator, URL)
        messages.success(request, '修改成功!')
    except:
        messages.error(request, '修改失败')

    return HttpResponseRedirect(reverse('pbl:device_survey_index', args=(province_id,)))

def delete(request, province_id, id):
    try:
        Survey.objects.get(id=id).delete()
        response = {'result':'success'}
    except:
        response = {'result':'failure'}

    return json_response(response)

# 下任务接口
def show_json(request, province_id):
    sn = request.GET.get('sn', '')
    device = Device.objects.get(sn=sn)
    device_survey = DeviceSurvey.objects.get(device=device)
    survey = device_survey.survey

    response = {}
    response['operator'] = survey.operator
    response['IP'] = survey.IP.split('|')
    response['domain'] = survey.domain.split('|')
    response['URL'] = survey.URL.split('|')

    return json_response(response)

def run_now(request, province_id, device_id):
    device = Device.objects.get(id=device_id)

    try:
        device_survey = DeviceSurvey.objects.get(device=device)
        state = State.objects.create(device=device, operator=device_survey.survey.operator)
    except:
        return json_response({'message':'该设备没有指定出口策略,任务下发失败', 'type':'error'})

    pbl_survey_show_url = '%s%s?sn=%s' % (
            settings.API_ADDRESS,
            reverse('pbl:survey_show_json', args=(province_id,)),
            device.sn
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
        province.schedule = '%s' % minute
        province.save()

        pbl_survey_show_url = '%s%s' % (
                settings.API_ADDRESS,
                reverse('pbl:survey_show_json', args=(province.id,))
        )

        pbl_state_schedule_create_url = '%s%s' % (
                settings.API_ADDRESS,
                reverse('pbl:state_schedule_create')
        )

        mail_create_url = '%s%s' % (
                settings.API_ADDRESS,
                reverse('mail:create')
        )

        print pbl_survey_show_url
        print pbl_state_schedule_create_url
        print mail_create_url

        tasks.schedule.apply_async(
            args=
                [
                    pbl_survey_show_url,
                    pbl_state_schedule_create_url,
                    mail_create_url,
                    minute
                ],
            routing_key="pbl.scheduel.%s" % province.name,
            exchange=province.name,
            exchange_type='fanout'
        )

        response = {'message':'周期任务已下发', 'type':'success'}
    else:
        response = {'message':'输入时间格式有误,请检测!', 'type':'error'}

    return json_response(response)

