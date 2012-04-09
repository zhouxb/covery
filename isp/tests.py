# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
import anyjson

class ProvinceTest(TestCase):
    fixtures = ['province_testdata.json']
    def setUp(self):
        self.c = Client()

    def test_create_province_on_success(self):
        response = self.c.post(
                reverse('isp:province_create'),
                {
                    'name':'安徽',
                }
        )

        assert response.status_code == 302

    def test_create_repeat_province_on_failure(self):
        response = self.c.post(
                reverse('isp:province_create'),
                {
                    'name':'海南',
                }
        )

        assert response.status_code == 302

    def test_delete_province_on_success(self):
        response = self.c.get(
                reverse('isp:province_delete', args=(2,))
        )

        result = anyjson.loads(response.content)

        assert result['result'] == 'success'

    def test_delete_not_exist_province_on_failure(self):
        response = self.c.get(
                reverse('isp:province_delete', args=(3,))
        )

        result = anyjson.loads(response.content)

        assert result['result'] == 'failure'

class DeviceTest(TestCase):
    fixtures = ['province_testdata.json', 'device_testdata.json']
    def setUp(self):
        self.c = Client()

    def test_create_device_on_success(self):
        response = self.c.post(
                reverse('isp:device_create', args=(1,)),
                {
                    'name':'FC设备02',
                    'sn':'sn02',
                }
        )

        assert response.status_code == 302

    def test_create_repeat_device_on_failure(self):
        response = self.c.post(
                reverse('isp:device_create', args=(1,)),
                {
                    'name':'FC设备01',
                    'sn':'sn01',
                }
        )

        assert response.status_code == 302

    def test_delete_device_on_success(self):
        response = self.c.get(
                reverse('isp:device_delete', args=(1, 1,))
        )

        result = anyjson.loads(response.content)

        assert result['result'] == 'success'

    def test_delete_not_exist_cdevice_on_failure(self):
        response = self.c.get(
                reverse('isp:device_delete', args=(1, 3,))
        )

        result = anyjson.loads(response.content)

        assert result['result'] == 'failure'

