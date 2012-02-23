# -*- coding:utf8 -*-

from django import forms

class UserProfile(forms.Form):
    name = forms.CharField(
            label='姓名',
            widget=forms.TextInput(attrs={'class':'input-xlarge'}),
            max_length=30,
            required=False
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input-xlarge'}))
    #address = forms.TextField()

