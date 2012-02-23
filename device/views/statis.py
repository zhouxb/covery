# -*- coding:utf8 -*-

from contrib.shortcuts import render as c_render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from device.models import Device

def index(request):
    devices = request.user.device_set.all()
    enable = devices.filter(status=1).count()
    disable = devices.filter(status=2).count()
    unknow = devices.filter(status=0).count()
    apply = devices.filter(status=3).count()
    pass_count = devices.filter(status=4).count()
    unpass = devices.filter(status=5).count()
    data = {
            'enable':enable,
            'disable':disable,
            'unknow':unknow,
            'apply':apply,
            'pass_count':pass_count,
            'unpass':unpass
            }

    return render(request, 'device/statis/index.html', {'data':data})

