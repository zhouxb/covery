# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import anyjson

class DomainViewTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_create_on_success(self):
        response = self.c.post(
                reverse('domain:create'),
                {
                    'name': 'http://www.a.com',
                    'port': 8080,
                    'task_id': 1
                }
        )

        status = anyjson.loads(response.content)['status']

        assert status == 'success'

    def test_create_on_success_by_https(self):
        response = self.c.post(
                reverse('domain:create'),
                {
                    'name': 'https://www.a.com',
                    'task_id': 1
                }
        )

        status = anyjson.loads(response.content)['status']

        assert status == 'success'

    def test_create_on_failure(self):
        response = self.c.post(
                reverse('domain:create'),
                {
                    'name': 'http://www.a.com',
                    'port': 'port',
                    'task_id': 1
                }
        )

        status = anyjson.loads(response.content)['status']

        assert status == 'failure'

