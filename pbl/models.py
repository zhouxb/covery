# -*- coding:utf8 -*-

import datetime
from django.db import models

class Survey(models.Model):
    OPERATOR = (
            ('CNC', '中国网通'),
            ('CT', '中国电信'),
            ('CMCC', '中国移动'),
    )

    operator = models.CharField('运营商', max_length=4, choices=OPERATOR)
    IP = models.TextField('IP列表')
    domain = models.TextField('域名列表')
    URL = models.TextField('URL列表')
    schedule = models.CharField('周期', max_length=5, null=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

class State(models.Model):
    survey = models.ForeignKey(Survey, null=True)
    IP_state = models.TextField('IP探测状态', null=True)
    domain_state = models.TextField('解析探测状态', null=True)
    URL_state = models.TextField('URL探测状态', null=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

