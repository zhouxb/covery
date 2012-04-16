# -*- coding:utf8 -*-

from django import forms
from mail.models import Mail

class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        exclude = ('is_readed', 'is_sended', 'date_joined')

