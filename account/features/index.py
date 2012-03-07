# -*- coding: utf8 -*-

from lettuce import *
from lettuce.django import django_url
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(u'给定 我访问url"([^"]*)"')
def access_url(step, url):
    full_url = django_url(url)
    response = world.browser.get(full_url)
    world.dom = html.fromstring(response.content)

@step(u'那么 我可以看到"([^"]*)"')
def see_header(step, text):
    header = world.dom.cssselect('h2')[0]
    assert header.text == text

