# -*- coding:utf8 -*-

from celery.result import AsyncResult
#from contrib.shortcuts import render
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

def index(request):
    page = int(request.GET.get('page', '1'))

    crawlers = Crawler.objects.all()

    paginator = Paginator(crawlers, 10)

    try:
        crawlers = paginator.page(page)
    except (EmptyPage, InvalidPage):
        crawlers = paginator.page(paginator.num_pages)

    form = CrawlerForm()

    return render(request, 'crawler/index.html', {'crawlers':crawlers, 'form':form})

def create(request):
    form = CrawlerForm(request.POST)
    task = TaskMeta.objects.all()[1]

    if form.is_valid():
        crawler = form.save(commit=False)
        crawler.save()

        messages.success(request, '添加成功!')
    else:
        messages.error(request, '添加失败!')

    return HttpResponseRedirect(reverse('crawler:index'))

def run(request, id):
    crawler = Crawler.objects.get(id=id)
    task_id = tasks.Crawler.delay('crawler').task_id
    crawler.task_id = task_id
    crawler.save()

    return json_response({'id':id})

def delete(request, id):
    Crawler.objects.get(id=id).delete()
    return json_response({'id':id})

def show(request, id):
    crawler = Crawler.objects.get(id=id)
    print dir(crawler)
    #print crawler.__class__._meta.get_field_by_name('name')[0].verbose_name

    return render(request, 'crawler/show.html', {'crawler':crawler})

def status(request, id):
    crawler = Crawler.objects.get(id=id)

    task = AsyncResult(crawler.task_id)

    print dir(task)
    print task.ready()
    print task.state

    return json_response({'id':id})

