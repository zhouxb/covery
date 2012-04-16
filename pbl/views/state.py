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

def index(request, province_id, template_name='pbl/state/index.html'):
    province = Province.objects.get(id=province_id)
    devices = province.device_set.all()
    minute = province.survey_set.all()[0].schedule

    states = []
    for device in devices:
        try:
            states.append(State.objects.filter(device=device)[0])
        except:
            pass

    return render(request, template_name, {'province':province, 'states':states, 'minute':minute})

def show(request, province_id, device_id, template_name='pbl/state/show.html'):
    province = Province.objects.get(id=province_id)
    device = Device.objects.get(id=device_id)

    states = device.state_set.all()[:10]

    return render(request, template_name, {'province':province, 'device':device, 'states':states})

def delete(request, id):
    response = {'result':'failure'}
    try:
        State.objects.get(id=id).delete()
        response = {'result':'success'}
    except:
        pass

    return json_response(response)

@csrf_exempt
def create(request, id):
    form = StateForm(request.POST, instance=State.objects.get(id=id))

    status = 'failure'
    if form.is_valid():
        form.save()
        status = 'success'

    return json_response({'status':status})

@csrf_exempt
def schedule_create(request):
    sn = request.POST.get('sn', '')
    device = Device.objects.get(sn=sn)

    form = StateForm(request.POST)
    status = 'failure'
    if form.is_valid():
        state = form.save(commit=False)
        state.device = device
        state.save()
        status = 'success'

    return json_response({'status':status})

