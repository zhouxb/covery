# -*- coding:utf8 -*-

from django import template

register = template.Library()

def operator(device):
    try:
        survey = device.devicesurvey_set.all()[0].survey

        return survey.operator
    except:
        return 'Unknow'

register.filter('operator', operator)

