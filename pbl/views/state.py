# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from pbl.forms import StateForm
from pbl.models import Survey, State
import anyjson

def index(request, template_name='pbl/state/index.html'):
    states = State.objects.all()[:10]

    return render(request, template_name, {'states':states})

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

def show(request, id, template_name='pbl/state/show.html'):
    return render(request, template_name, {'id':id})

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
