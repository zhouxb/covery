# -*- coding:utf8 -*-

import datetime
from django.db import models

class Province(models.Model):

    name = models.CharField('名称', max_length=200, unique=True, blank=False)
    schedule = models.CharField('周期', max_length=5, null=True, blank=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

class Device(models.Model):

    province = models.ForeignKey(Province, null=True)
    name = models.CharField('名称', max_length=200)
    sn = models.CharField('SN', max_length=16, unique=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

