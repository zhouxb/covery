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
    survey = province.survey_set.all()[0]
    states = State.objects.filter(survey=survey)[:10]

    return render(request, template_name, {'province':province, 'states':states})

def show(request, province_id, device_id, template_name='pbl/state/show.html'):
    province = Province.objects.get(id=province_id)
    device = Device.objects.get(id=device_id)

    states = device.state_set.all()[:10]

    return render(request, template_name, {'province':province, 'device':device, 'states':states})

def show_json(request, id):
    type = request.GET.get('type', '')

    state = State.objects.get(id=id)
    response = state.build_data(type)

    return json_response(response)

def delete(request, id):
    response = {'result':'failure'}
    try:
        State.objects.get(id=id).delete()
        response = {'result':'success'}
    except:
        pass

    #return HttpResponseRedirect(reverse('pbl:state_index'))
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
    form = StateForm(request.POST)

    status = 'failure'
    if form.is_valid():
        state = form.save(commit=False)
        state.survey = Survey.objects.all()[0]
        state.save()
        status = 'success'

    return json_response({'status':status})

