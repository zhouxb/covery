# -*- coding:utf8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.conf import settings

import anyjson

@csrf_exempt
def create(request):
    from_email = request.POST.get('from_email', '')
    recipient_list = request.POST.get('to_email', '').split(',')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    send(from_email, recipient_list, subject, message)

    return json_response({'state':'ok'})

def send(fromAdd, toAdd, subject, htmlText):
    strFrom = fromAdd
    strTo =toAdd

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = strFrom
    msgRoot['To'] = ','.join(toAdd)
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(htmlText,'html','gb2312')
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP('corp.chinacache.com')
    smtp.set_debuglevel(0)

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

