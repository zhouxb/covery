# -*- coding:utf8 -*-

#from contrib.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
#from device.forms import DeviceForm
from discovery.device.models import Device

def index(request):
    devices = Device.objects.filter(status__in=['0', '1', '2', '4'])

    return render(request, 'csp/device/index.html', {'devices':devices})

