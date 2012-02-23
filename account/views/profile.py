# -*- coding:utf8 -*-

#from contrib.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from account.forms import UserProfile

def index(request):
    user = User.objects.filter(id=request.user.id).values('first_name', 'last_name', 'email')[0]
    form = UserProfile({'name':'%s%s' % (user['first_name'], user['last_name']), 'email':user['email']})

    #return render(request, 'account/index.html', {'form':form})
    return render(request, 'account/index.html', {'form':form})

def update(request):
    form = UserProfile(request.POST)
    if form.is_valid():
        user = request.user
        try:
            name = form.cleaned_data['name'].strip()
            user.first_name=name[0]
            user.last_name=name[1:]
        except:
            user.first_name=''
            user.last_name=''
        user.email=form.cleaned_data['email']
        user.save()

    messages.info(request, '更新成功!')

    return HttpResponseRedirect('/account')

