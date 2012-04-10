# -*- coding:utf8 -*-

import datetime
from django.db import models
from isp.models import Province, Device
import anyjson

class Survey(models.Model):
    OPERATOR = (
            ('CNC', '中国网通'),
            ('CT', '中国电信'),
            ('CMCC', '中国移动'),
    )

    province = models.ForeignKey(Province, null=True)
    operator = models.CharField('运营商', max_length=4, choices=OPERATOR)
    IP = models.TextField('IP列表')
    domain = models.TextField('域名列表')
    URL = models.TextField('URL列表')
    schedule = models.CharField('周期', max_length=5, null=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

class State(models.Model):
    survey = models.ForeignKey(Survey, null=True)
    device = models.ForeignKey(Device, null=True)
    IP_state = models.TextField('IP探测状态', null=True)
    domain_state = models.TextField('解析探测状态', null=True)
    URL_state = models.TextField('URL探测状态', null=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

    class Meta:
        ordering = ('-date_joined',)

    def build_data(self, type):
        if type == "ip":
            categories, series, avg, max = [], [], [], []

            for item in anyjson.loads(self.IP_state):
                if item['rate'] != 1:
                    categories.append(item['ip'])
                    avg.append(item['avg'])
                    max.append(item['max'])
            series = [{'name':'avg', 'data':avg}, {'name':'max', 'data':max}]

        if type == 'domain':
            categories, time, series = [], [], []

            for item in anyjson.loads(self.domain_state):
                categories.append(item['domain'])
                time.append(item['time'])
            series = [{'name':'time', 'data':time}]

        if type == 'url':
            categories, speed, series = [], [], []

            for item in anyjson.loads(self.URL_state):
                categories.append(item['url'])
                speed.append(item['speed'])
            series = [{'name':'time', 'data':speed}]

        return {'categories':categories, 'series':series}

