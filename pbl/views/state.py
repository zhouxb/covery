# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from pbl.forms import StateForm
from pbl.models import Survey, State

def index(request, template_name='pbl/state/index.html'):
    states = State.objects.all()

    return render(request, template_name, {'states':states})

@csrf_exempt
def create(request, id):
    form = StateForm(request.POST, instance=State.objects.get(id=id))

    status = 'failure'
    if form.is_valid():
        form.save()
        status = 'success'

    return json_response({'status':status})

