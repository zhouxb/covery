# -*- coding:utf8 -*-

from django.core.exceptions import ObjectDoesNotExist
from isp.models import Device

def search(q):
    devices = []
    q_s = filter(lambda x:x!='', q.split(' '))

    for q_i in q_s:
        try:
            devices_tmp = Device.objects.filter(sn__contains=q_i)
            devices += devices_tmp
        except ObjectDoesNotExist, e:
            pass

    return devices

