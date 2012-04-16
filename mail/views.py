# -*- coding:utf8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from contrib.shortcuts import json_response
from mail.models import Mail
from mail.forms import MailForm
from mail.helpers import send_mail

import anyjson

def index(request, template_name='mail/index.html'):
    page = int(request.GET.get('page', '1'))

    mails = Mail.objects.all()
    paginator = Paginator(mails, 20)

    try:
        mails = paginator.page(page)
    except (EmptyPage, InvalidPage):
        mails = paginator.page(paginator.num_pages)

    print mails.paginator.page_range[1:3]
    return render(request, template_name, {'mails':mails})

def delete(request, id):
    response = {'result':'failure'}
    try:
        Mail.objects.get(id=id).delete()
        response = {'result':'success'}
    except:
        pass

    return json_response(response)

@csrf_exempt
def create(request):
    from_email = request.POST.get('from_email', '')
    recipient_list = request.POST.get('to_email', '').split(',')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    response = {'result':'success'}
    try:
        send_mail(from_email, recipient_list, subject, message)
    except:
        response = {'result':'failure'}

    form = MailForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
        if response['result'] == 'failure':
            form.is_sended = False
        form.save()

    return json_response(response)

