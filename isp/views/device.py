# -*- coding:utf8 -*-

from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from isp.models import Province, Device
import anyjson

def index(request, province_id, template_name='isp/device/index.html'):
    province = Province.objects.get(id=province_id)
    devices = province.device_set.all()

    return render(request, template_name, {'province':province, 'devices':devices})

def new(request, province_id):
    pass

def create(request, province_id):
    name = request.POST.get('name', '')
    sn = request.POST.get('sn', '')

    try:
        province = Province.objects.get(id=province_id)
        Device.objects.create(name=name, sn=sn, province=province)
        messages.success(request, '添加成功!')
    except IntegrityError, e:
        messages.error(request, '添加失败,设备sn重复!')

    return HttpResponseRedirect(reverse('pbl:device_survey_index', args=(province_id,)))

def show(request, province_id, id):
    pass

def update(request, province_id, id):
    pass

def delete(request, province_id, id):

    try:
        Device.objects.get(id=id).delete()
        response = {'result':'success'}
    except ObjectDoesNotExist, e:
        response = {'result':'failure'}

    return json_response(response)

