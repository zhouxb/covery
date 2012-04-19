# -*- coding:utf8 -*-

from django import template

register = template.Library()

def operator(device):
    survey = device.devicesurvey_set.all()[0].survey

    return survey.operator

register.filter('operator', operator)

