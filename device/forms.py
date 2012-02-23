# -*- coding:utf8 -*-

from django import forms
from device.models import Device

class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        exclude = ('user', 'info')
        widgets = {
                'remark':forms.Textarea(attrs={'rows':'3'}),
        }

class OrderForm(forms.ModelForm):

    class Meta:
        model = Device
        exclude = ('user', 'info', 'status')
        widgets = {
                'remark':forms.Textarea(attrs={'rows':'3'}),
        }

