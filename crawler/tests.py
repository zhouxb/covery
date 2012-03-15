# -*- coding:utf8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from crawler.tasks import crawl
from crawler.models import Crawler
import anyjson

class CrawlerTest(TestCase):
    fixtures = ['crawler_testdata.json']
    def setUp(self):
        self.c = Client()

    #def test_crawl_task_on_success(self):
        #crawl.apply_async(args=[1, 'http://127.0.0.1:8000'])
        #crawler = Crawler.objects.get(id=1)

        #assert crawler.jobid != None

    #def test_crawl_task_on_failure(self):
        #crawl.apply_async(args=[1, 'http://127.0.0.1:8000'])
        #crawler = Crawler.objects.get(id=1)
        #status = crawler.status.split(':')[0]

        #assert status == 'failure'

    def test_update_on_success(self):
        response = self.c.post(
                reverse('crawler:update', args=[1]),
                {
                    'status':'START:start'
                }
        )

        status = anyjson.loads(response.content)['status']

        assert status == 'ok'

