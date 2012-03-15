# -*- coding:utf8 -*-

from django import forms
from crawler.models import Crawler

class CrawlerForm(forms.ModelForm):

    class Meta:
        model = Crawler
        exclude = ('task_id', 'periodic_task_id', 'jobid', 'status', 'date_joined')

