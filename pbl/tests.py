# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import anyjson
from pbl.models import Survey, State

class PblTest(TestCase):
    fixtures = ['survey_testdata.json']
    def setUp(self):
        self.c = Client()

    def test_survey_show_on_success(self):
        response = self.c.get(
                    reverse('pbl:survey_show'),
                )

        result = anyjson.loads(response.content)
        expect = {
                    'operator':'CT',
                    'IP':['127.0.0.1', '192.168.0.1'],
                    'domain':['localhost', 'www.qq.com'],
                    'URL':['http://www.baidu.com/mm.mp3']
                }

        assert result == expect
        #self.assertDictEqual(result, expect)

    def test_state_create_on_success(self):
        id = State.objects.create(survey=Survey.objects.all()[0]).id
        response = self.c.post(
                    reverse('pbl:state_create', args=(id,)),
                        {
                            'IP_state':'ok',
                            'domain_state':'ok',
                            'URL_state':'ok',
                        }
                    )

        result = anyjson.loads(response.content)
        state = State.objects.values('IP_state', 'domain_state', 'URL_state')[0]
        expect = {'domain_state': u'ok', 'URL_state': u'ok', 'IP_state': u'ok'}

        assert result['status'] == 'success'
        assert state == expect

    def test_state_scheduel_create_on_success(self):
        response = self.c.post(
                    reverse('pbl:state_schedule_create'),
                        {
                            'IP_state':'ok',
                            'domain_state':'ok',
                            'URL_state':'ok',
                            }
                        )

        result = anyjson.loads(response.content)
        state = State.objects.values('IP_state', 'domain_state', 'URL_state')[0]
        expect = {'domain_state': u'ok', 'URL_state': u'ok', 'IP_state': u'ok'}

        assert result['status'] == 'success'
        assert state == expect

