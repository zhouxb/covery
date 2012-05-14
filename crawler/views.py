# -*- coding:utf8 -*-

import datetime

from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
from contrib.shortcuts import json_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from djcelery.models import TaskMeta
from crawler.models import Crawler
from crawler.forms import CrawlerForm
from crawler import tasks

def index(request, template_name='crawler/index.html'):
    page = int(request.GET.get('page', '1'))

    crawlers = Crawler.objects.all().order_by('-date_joined')

    paginator = Paginator(crawlers, 10)

    try:
        crawlers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        crawlers = paginator.page(paginator.num_pages)

    form = CrawlerForm()

    return render(request, template_name, {'crawlers':crawlers, 'form':form})

def create(request):
    form = CrawlerForm(request.POST)

    if form.is_valid():
        crawler = form.save(commit=False)
        crawler.save()

        messages.success(request, '添加成功!')
    else:
        messages.error(request, '添加失败!')

    return HttpResponseRedirect(reverse('crawler:index'))

def run(request, id):
    crawler = Crawler.objects.get(id=id)
    if not crawler.task_id:
        task_id = tasks.crawl.apply_async(args=[id, 'http://localhost:8000']).task_id
        crawler.task_id = task_id
        crawler.status = 'INIT:init'
        crawler.save()

    return json_response({'id':id})

def delete(request, id):
    Crawler.objects.get(id=id).delete()

    return json_response({'id':id})

def show(request, id, template_name='crawler/show.html'):
    crawler = Crawler.objects.get(id=id)
    state, state_message = crawler.status.split(':')

    return render(request, template_name, {'crawler':crawler, 'state':state, 'state_message':state_message})

def status(request, id):
    crawler = Crawler.objects.get(id=id)

    if crawler.status == None or 'PENDING' in crawler.status:
        if not 'ERROR' in crawler.status:
            task = AsyncResult(crawler.task_id)
            crawler.status = '%s:%s' % (task.state, task.state.lower())
            crawler.save()

    state, state_message = crawler.status.split(':')

    return json_response({'id':id, 'state':state, 'state_message':state_message})

@csrf_exempt
def update(request, id):
    status = request.POST.get('status', '')

    crawler = Crawler.objects.get(id=id)
    crawler.status = status
    crawler.date_update = datetime.datetime.now()
    crawler.save()

    return json_response({'status':'ok'})

