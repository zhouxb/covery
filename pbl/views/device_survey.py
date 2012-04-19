# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from covery.isp.models import Province
from pbl.forms import StateForm
from pbl.models import Survey, State, DeviceSurvey
from pbl.helpers import build_device_survey
from covery.isp.models import Device
import anyjson

def index(request, province_id, template_name='pbl/device_survey/index.html'):
    province = Province.objects.get(id=province_id)
    minute = province.schedule

    survey_devices = build_device_survey(province)

    return render(request, template_name, {'province':province, 'survey_devices':survey_devices, 'minute':minute})

def update(request, province_id, template_name='pbl/device_survey/update.html'):
    province = Province.objects.get(id=province_id)
    survey_devices = build_device_survey(province)

    return render(request, template_name, {'province':province, 'survey_devices':survey_devices})

@csrf_exempt
def update_json(request, province_id):
    survey_id = request.POST.get('survey_id', '')
    device_id = request.POST.get('device_id', '')

    device = Device.objects.get(id=device_id)
    device_survey, state = DeviceSurvey.objects.get_or_create(device=device)

    if survey_id:
        survey = Survey.objects.get(id=survey_id)
        device_survey.survey = survey
        device_survey.save()
    else:
        device_survey.delete()

    response = {'result':'success'}

    return json_response(response)

