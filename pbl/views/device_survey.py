# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from covery.isp.models import Province
from pbl.forms import StateForm
from pbl.models import Survey, State
from pbl.helpers import build_device_survey
import anyjson

def index(request, province_id, template_name='pbl/device_survey/index.html'):
    province = Province.objects.get(id=province_id)

    survey_devices = build_device_survey(province)

    return render(request, template_name, {'province':province, 'survey_devices':survey_devices})

def update(request, province_id, template_name='pbl/device_survey/update.html'):
    province = Province.objects.get(id=province_id)
    survey_devices = build_device_survey(province)

    return render(request, template_name, {'province':province, 'survey_devices':survey_devices})

