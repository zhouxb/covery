# -*- coding:utf8 -*-

from django import forms
from domain.models import Domain

class DomainForm(forms.ModelForm):
    port = forms.IntegerField(required=False)

    class Meta:
        model = Domain
        exclude = ('date_joined')

