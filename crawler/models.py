# -*- coding:utf8 -*-

import datetime
from django.db import models

class Crawler(models.Model):

    task_id = models.CharField('task id', max_length=255, unique=True)
    name = models.CharField('名称', max_length=30, unique=True, help_text='唯一')
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

