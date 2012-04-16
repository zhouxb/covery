# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from mail.models import Mail
import anyjson

class MailTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_create_mail_on_success(self):
        response = self.c.post(
                reverse('mail:create'),
                {
                    'from_email':'xingbo.zhou@chinacache.com',
                    'to_email':'xingbo.zhou@chinacache.com',
                    'subject':'alert',
                    'message':'hello world'
                }
        )

        response = anyjson.loads(response.content)
        mail = Mail.objects.all()[0]

        assert response['result'] == 'success'
        assert mail.subject == 'alert'
