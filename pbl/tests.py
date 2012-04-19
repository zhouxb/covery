# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import anyjson
from pbl.models import Survey, State
from covery.isp.models import Device

class PblTest(TestCase):
    fixtures = ['province_testdata.json', 'device_testdata.json', 'survey_testdata.json', 'device_survey_testdata']
    def setUp(self):
        self.c = Client()

    def test_survey_show_on_success(self):
        response = self.c.get(
                    reverse('pbl:survey_show_json', args=(1,)),
                    {'sn':'sn01'}
                )

        result = anyjson.loads(response.content)
        expect = {
                    'operator':'CT',
                    'IP':['127.0.0.1', '192.168.0.1'],
                    'domain':['localhost', 'www.qq.com'],
                    'URL':['http://www.baidu.com/mm.mp3']
                }

        assert result == expect

    def test_state_create_on_success(self):
        id = State.objects.create(device=Device.objects.get(id=1)).id
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
                            'sn':'sn01',
                            }
                        )

        result = anyjson.loads(response.content)
        state = State.objects.values('IP_state', 'domain_state', 'URL_state')[0]
        expect = {'domain_state': u'ok', 'URL_state': u'ok', 'IP_state': u'ok'}

        assert result['status'] == 'success'
        assert state == expect

class StateModelTest(TestCase):
    fixtures = ['province_testdata.json', 'device_testdata.json', 'state_testdata.json']
    def setUp(self):
        self.c = Client()

    def test_build_data_on_success(self):
        state = State.objects.get(id=1)

        response_ip = state.build_data('ip')
        response_domain = state.build_data('domain')
        response_url = state.build_data('url')

        expect_ip = {
                'series':
                    [
                        {'data': [0.050999999999999997], 'name': 'avg'},
                        {'data': [0.055], 'name': 'max'}
                    ],
                'categories': [u'127.0.0.1']
        }

        expect_domain ={
                'series': [{'data': [13.157], 'name': 'time'}],
                'categories': [u'www.baidu.com']
        }
        expect_url = {
                'series': [{'data': [22.420000000000002], 'name': 'time'}], 
                'categories': [u'http://qq.com']
        }

        assert response_ip == expect_ip
        assert response_domain == expect_domain
        assert response_url == expect_url
