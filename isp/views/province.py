# -*- coding:utf8 -*-

from django.shortcuts import render
from contrib.shortcuts import json_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from isp.models import Province
from isp.helpers import province_helper
import anyjson

def index(request, template_name='isp/province/index.html'):

    provinces = Province.objects.all()

    return render(request, template_name, {'provinces':provinces})

def show(request, template_name='isp/province/show.html'):
    q = request.GET.get('q', '')

    if q:
        devices = province_helper.search(q)
        return render(request, template_name, {'devices':devices, 'q':q})
    else:
        return HttpResponseRedirect(reverse('isp:province_index'))

def create(request):
    name = request.POST.get('name', '')

    try:
        Province.objects.create(name=name)
        messages.success(request, '添加成功!')
    except IntegrityError, e:
        messages.error(request, '添加失败,运营商已经存在!')

    return HttpResponseRedirect(reverse('isp:province_index'))

def update(request, id):
    name = request.POST.get('name', '')
    province = Province.objects.get(id=id)
    province.name = name

    try:
        province.save()
        messages.success(request, '更新成功!')
    except IntegrityError, e:
        messages.error(request, '更新失败,运营商名称已经存在!')

    return HttpResponseRedirect(reverse('isp:province_index'))

def delete(request, id):
    try:
        Province.objects.get(id=id).delete()
        response = {'result':'success'}
    except ObjectDoesNotExist, e:
        response = {'result':'failure'}

    return json_response(response)

