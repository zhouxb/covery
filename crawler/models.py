# -*- coding:utf8 -*-

import datetime
from django.db import models

class Crawler(models.Model):

    #task_id = models.CharField('task id', max_length=255, unique=True, null=True)
    #periodic_task_id = models.IntegerField('periodic_task_id', unique=True, null=True)
    jobid = models.CharField('jobid', max_length=255, unique=True, null=True)
    name = models.CharField('任务名称', max_length=30, unique=True, help_text='任务名称必须唯一')
    allowed_domain = models.CharField('检测域名', max_length=200, help_text='爬取时要检测的域名')
    start_url = models.URLField('起始地址', verify_exists=True, help_text='爬取网站的起始地址,并确保该地址可以访问')
    depth_limit = models.IntegerField('层级', help_text='爬取的层数')
    status = models.CharField('状态', max_length=255, null=True)
    date_update = models.DateTimeField('更新时间', default=datetime.datetime.now)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

    class Meta:
        ordering = ('-date_joined',)
