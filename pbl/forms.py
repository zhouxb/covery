# -*- coding:utf8 -*-

from django import forms
from pbl.models import Survey, State

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        exclude = ('survey', 'device', 'date_joined')

