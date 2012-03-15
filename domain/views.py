# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
#from contrib.shortcuts import render
from contrib.shortcuts import json_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from domain.models import Domain
from domain.forms import DomainForm

def index(request, template_name='domain/index.html'):
    page = int(request.GET.get('page', '1'))

    domains = Domain.objects.all()

    paginator = Paginator(domains, 10)

    try:
        domains = paginator.page(page)
    except (EmptyPage, InvalidPage):
        domains = paginator.page(paginator.num_pages)

    return render(request, template_name, {'domains':domains})

@csrf_exempt
def create(request):
    form = DomainForm(request.POST)

    status = 'failure'
    if form.is_valid():
        form.save()
        status = 'success'

    return json_response({'status':status})

def delete(request):
    pass

def show(request, task_id, template_name='domain/show.html'):
    domains = Domain.objects.filter(task_id=task_id).order_by('-date_joined')

    return render(request, template_name, {'domains':domains})

