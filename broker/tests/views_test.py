from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from broker.tasks import add, t, UpdateStatus


class SimpleTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_basic_addition(self):
        response = self.c.get(reverse('broker:index'))

        assert response.status_code == 302

    def test_no_error(self):
        result = add.delay(8, 8)

        response = t(5, 5)
        print response.content

        UpdateStatus.delay('Bod')


        assert result.get() == 16
        assert result.successful()

