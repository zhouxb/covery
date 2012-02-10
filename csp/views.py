# -*- coding:utf8 -*-

from coffin.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from csp.models import Device
# Create your views here.

def index(request):
    info = request.GET.get('info', '').strip()
    if info:
        devices = Device.objects.filter(info__contains=info).order_by('group')
    else:
        devices = Device.objects.all().order_by('group')
    return render_to_response('csp/device/index.html', {'devices':devices, 'info':info}, context_instance=RequestContext(request))

def new(request):
    return render_to_response('csp/device/new.html',  context_instance=RequestContext(request))

def create(request):
    group = request.POST.get('group', '')
    owner = request.POST.get('owner', '')
    intranet_ip = request.POST.get('intranet_ip', '')
    external_ip= request.POST.get('external_ip', '')
    sn = request.POST.get('sn', '')
    type = request.POST.get('type', '')
    description = request.POST.get('description', '')
    os = request.POST.get('os', '')
    safe = request.POST.get('safe', '')
    location = request.POST.get('location', '')
    remark = request.POST.get('remark', '')

    device = Device(
            group = group,
            owner = owner,
            intranet_ip = intranet_ip,
            external_ip = external_ip,
            sn = sn,
            type = type,
            description = description,
            os = os,
            safe = safe,
            location = location,
            remark = remark,
            info = '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (group, owner, intranet_ip, external_ip, sn, type, description, os, safe, location, remark)
        )

    device.save()

    return HttpResponseRedirect('/csp/devices')


def show(request, id):

    device = Device.objects.get(id=id)

    return render_to_response('csp/device/show.html', {'device':device}, context_instance=RequestContext(request))

def update(request, id):
    group = request.POST.get('group', '')
    owner = request.POST.get('owner', '')
    intranet_ip = request.POST.get('intranet_ip', '')
    external_ip= request.POST.get('external_ip', '')
    sn = request.POST.get('sn', '')
    type = request.POST.get('type', '')
    description = request.POST.get('description', '')
    os = request.POST.get('os', '')
    safe = request.POST.get('safe', '')
    location = request.POST.get('location', '')
    remark = request.POST.get('remark', '')

    device = Device.objects.get(id=id)

    device.group = group
    device.owner = owner
    device.intranet_ip = intranet_ip
    device.external_ip = external_ip
    device.sn = sn
    device.type = type
    device.description = description
    device.os = os
    device.safe = safe
    device.location = location
    device.remark = remark
    device.info = '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (group, owner, intranet_ip, external_ip, sn, type, description, os, safe, location, remark)

    device.save()

    return HttpResponseRedirect('/csp/devices')

def delete(request, id):
    info = request.GET.get('info', '')
    Device.objects.get(id=id).delete()
    return HttpResponseRedirect('/csp/devices?info=%s' % info)

def batch(request):
    return render_to_response('csp/device/batch.html',  context_instance=RequestContext(request))

def batch_create(request):
    devices = request.POST.get('devices', '')
    devices = filter(lambda x:x!='', devices.split('\r\n'))

    for item in devices:
        device = item.split('|')

        device = Device(
                group = device[0],
                owner = device[1],
                intranet_ip = device[2],
                external_ip = device[3],
                sn = device[4],
                type = device[5],
                description = device[6],
                os = device[7],
                safe = device[8],
                location = device[9],
                remark = device[10],
                info = item
            )

        device.save()

    return HttpResponseRedirect('/csp/devices')

def about(request):
    cop = Device.objects.filter(group='COP').count()
    gsp = Device.objects.filter(group='GSP').count()
    ssr = Device.objects.filter(group='SSR').count()
    return render_to_response('csp/device/about.html', {'cop':cop, 'gsp':gsp, 'ssr':ssr}, context_instance=RequestContext(request))
