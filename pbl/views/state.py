# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
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

    if type == 'ip':
        IP_state_data = state.IP_state_data()

        categories = []
        series = []
        avg = []
        max = []
        for item in IP_state_data:
            if item['rate'] != 1:
                categories.append(item['ip'])
                avg.append(item['avg'])
                max.append(item['max'])
        series = [{'name':'avg', 'data':avg}, {'name':'max', 'data':max}]


    if type == 'domain':
        domain_state_data = state.domain_state_data()
        categories = []
        time = []
        series = []

        for item in domain_state_data:
            categories.append(item['domain'])
            time.append(item['time'])
        series = [{'name':'time', 'data':time}]

    if type == 'url':
        URL_state_data = state.URL_state_data()
        categories = []
        speed = []
        series = []

        for item in URL_state_data:
            categories.append(item['url'])
            speed.append(item['speed'])
        series = [{'name':'time', 'data':speed}]

    return json_response({'categories':categories, 'series':series})

