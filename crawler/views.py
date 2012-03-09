# -*- coding:utf8 -*-

#from contrib.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from crawler import tasks
from djcelery.models import TaskMeta
from crawler.models import Crawler
from crawler.forms import CrawlerForm

def index(request):
    page = int(request.GET.get('page', '1'))

    crawlers = Crawler.objects.all()

    paginator = Paginator(crawlers, 5)

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

        task_id = tasks.Crawler.delay('crawler').task_id
        crawler.task_id = task_id
        crawler.save()

        messages.success(request, '添加成功!')
    else:
        messages.error(request, '添加失败!')

    return HttpResponseRedirect(reverse('crawler:index'))


def show(request, id):
    crawler = Crawler.objects.get(id=id)

    task = TaskMeta.objects.get(task_id=crawler.task_id)
    print dir(task)

    return HttpResponseRedirect(reverse('crawler:index'))

def delete(request):
    TaskMeta.objects.all()

    return HttpResponseRedirect('/')


