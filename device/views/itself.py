# -*- coding:utf8 -*-

from contrib.shortcuts import render as c_render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from device.forms import DeviceForm
from device.models import Device
from csp.models import Device as Old_device

DEPARTMENT = {
        'SSR':0,
        'COP':1,
        'GSP':2
}

def index(request):
    name = '%s%s' % (request.user.first_name, request.user.last_name)
    print name
    devices = Old_device.objects.filter(owner=name)

    for device in devices:
        device, created = Device.objects.get_or_create(
                department=DEPARTMENT[device.group],
                intranet_ip=device.intranet_ip,
                external_ip=device.external_ip,
                sn=device.sn,
                type=device.type,
                description=device.description,
                os=device.os,
                safe=device.safe,
                location=device.location,
                remark=device.remark,
        )

        if created:
            device.user.add(request.user)

    devices = request.user.device_set.all()
    devices = devices.filter(status__in = ['0', '1', '2', '4'])

    Old_device.objects.filter(owner=name).delete()

    return render(request, 'device/index.html', {'devices':devices})

def new(request):
    form = DeviceForm()

    return render(request, 'device/new.html', {'form':form})

def create(request):
    form = DeviceForm(request.POST)

    if form.is_valid():
        device = form.save()
        device.user.add(request.user)
        messages.info(request, '添加成功!')

    return HttpResponseRedirect('/account/device')

def show(request, id):
    form = DeviceForm(instance=Device.objects.get(id=id))

    return render(request, 'device/show.html', {'form':form, 'id':id})

def update(request, id):
    form = DeviceForm(request.POST, instance=Device.objects.get(id=id))
    form.save()
    messages.info(request, '更新成功!')

    return HttpResponseRedirect('/account/device')

def delete(request, id):
    Device.objects.get(id=id).delete()
    messages.info(request, '删除成功!')

    return HttpResponseRedirect('/account/device')

def update_status(request):
    status = request.GET.get('status', '0')
    device_ids = request.GET.get('device_ids', None).split('|')

    devices = Device.objects.filter(id__in=device_ids)

    for device in devices:
        device.status = status
        device.save()

    messages.info(request, '更新成功!')

    return HttpResponseRedirect('/account/device')

