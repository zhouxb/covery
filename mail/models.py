# -*- coding:utf8 -*-

import datetime
from django.db import models

class Mail(models.Model):

    from_email = models.CharField('From', max_length=200)
    to_email = models.CharField('To', max_length=1000)
    subject = models.CharField('主题', max_length=200)
    message = models.TextField('内容')
    is_readed = models.BooleanField(default=False)
    is_sended = models.BooleanField(default=True)
    date_joined = models.DateTimeField('添加时间', default=datetime.datetime.now)

    class Meta:
        ordering = ('-date_joined',)

