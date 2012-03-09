from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from crawler.tasks import Crawler
from djcelery.models import TaskMeta

class CrawlerTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_no_error(self):
        response = self.c.get(reverse('crawler:index'))

        assert response.status_code == 302

