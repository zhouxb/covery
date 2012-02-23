# -*- coding:utf8 -*-

from contrib.shortcuts import render as c_render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from device.forms import OrderForm
from device.models import Device

def index(request):
    devices = request.user.device_set.all()
    devices = devices.filter(status__in = ['3', '4', '5'])

    return render(request, 'device/order/index.html', {'devices':devices})

def new(request):
    form = OrderForm()

    return render(request, 'device/order/new.html', {'form':form})

def create(request):
    print 'here'
    form = OrderForm(request.POST)

    if form.is_valid():
        device = form.save()
        device.status = '3'
        device.save()
        device.user.add(request.user)
        messages.info(request, '申请成功!')

    return HttpResponseRedirect('/account/device/order')

def delete(request, id):
    Device.objects.get(id=id).delete()
    messages.info(request, '删除成功!')

    return HttpResponseRedirect('/account/device/order')

