# -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    DEPARTMENT = (
            ('0', 'SSR'),
            ('1', 'COP'),
            ('2', 'GSP'),
            )

    STATUS = (
            ('0', '未确认'),
            ('1', '可用'),
            ('2', '不可用'),
            ('3', '申请中'),
            ('4', '通过'),
            ('5', '未通过'),
            )

    user = models.ManyToManyField(User, verbose_name='用户')
    department = models.CharField('部门', max_length=1, choices=DEPARTMENT)
    intranet_ip = models.IPAddressField('内网IP', blank=True)
    external_ip = models.IPAddressField('外网IP', blank=True)
    sn = models.CharField('资源编号', max_length=100, blank=True)
    type = models.CharField('类型', max_length=100, blank=True)
    description = models.CharField('用途', max_length=100, blank=True)
    os = models.CharField('系统', max_length=100, blank=True)
    safe = models.CharField('安全措施', max_length=100, blank=True)
    location = models.CharField('位置', max_length=100, blank=True)
    remark = models.CharField('备注', max_length=100, blank=True)
    status = models.CharField('状态', max_length=1, choices=STATUS, default='0')
    info = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.remark

    class Meta:
        verbose_name_plural = '设备'



