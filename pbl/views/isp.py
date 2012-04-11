# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from covery.isp.models import Province
from pbl.forms import StateForm
from pbl.models import Survey, State
import anyjson

def index(request, template_name='pbl/isp/index.html'):
    provinces = Province.objects.all()

    return render(request, template_name, {'provinces':provinces})

