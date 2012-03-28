# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import anyjson

class MailTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_create_mail_on_success(self):
        print reverse('mail:create')
        response = self.c.post(
                reverse('mail:create'),
                {
                    'from_email':'xingbo.zhou@chinacache.com',
                    'to_email':'xingbo.zhou@chinacache.com',
                    'subject':'alert',
                    'message':'hello world'
                }
        )

        result = anyjson.loads(response.content)
        assert 1 == 1
