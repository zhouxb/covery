from django.db import models

# Create your models here.

#class Person(models.Model):
    #name = models.CharField(max_length=200)

class Device(models.Model):
    group = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    intranet_ip = models.IPAddressField()
    external_ip = models.IPAddressField()
    sn = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    safe = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    info = models.CharField(max_length=1000)

