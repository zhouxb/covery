# -*- coding:utf8 -*-

from contrib.shortcuts import render
#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from broker.tasks import add

def index(request):
    add.delay(4, 4)
    return HttpResponseRedirect('/')
