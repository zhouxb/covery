# -*- coding:utf8 -*-

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from models import Entry

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authorization = Authorization()

