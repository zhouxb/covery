# -*- coding:utf8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contrib.shortcuts import json_response
from django.conf import settings

def send_mail(fromAdd, toAdd, subject, htmlText):
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

    smtp = smtplib.SMTP(settings.SMTP_HOST)
    smtp.set_debuglevel(0)

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

