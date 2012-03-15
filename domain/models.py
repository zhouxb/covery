# -*- coding:utf8 -*-

import datetime
from django.db import models

class Domain(models.Model):

    name = models.CharField('域名', max_length=200)
    port = models.IntegerField('端口', null=True)
    task_id = models.IntegerField('task_id', null=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

    class Meta:
        unique_together = (('name', 'task_id'),)
