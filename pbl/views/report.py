# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from covery.isp.models import Province, Device
from pbl.forms import StateForm
from pbl.models import Survey, State
import anyjson


def show_chart(request, province_id, device_id, id, template_name='pbl/report/chart.html'):
    province = Province.objects.get(id=province_id)
    device = Device.objects.get(id=device_id)
    state = State.objects.get(id=id)

    return render(request, template_name, {'province':province, 'device':device, 'state':state, 'id':id})

def show_chart_json(request, id):
    type = request.GET.get('type', '')

    state = State.objects.get(id=id)
    response = state.build_data(type)

    return json_response(response)

