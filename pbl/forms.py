# -*- coding:utf8 -*-

from django import forms
from pbl.models import State

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        exclude = ('survey', 'date_joined')
