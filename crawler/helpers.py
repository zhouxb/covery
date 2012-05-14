import pycurl
import urllib
import StringIO

from crawler.models import Crawler
import anyjson
from django.conf import settings

def crawl(id, hostname, scrapyd_url='http://localhost:6800/schedule.json'):
    scrapyd_url = settings.SCRAPYD_URL

    crawler = Crawler.objects.get(id=id)
    post_data_dic = {
            'project':'covery_crawler',
            'spider':'common',
            'setting':'DEPTH_LIMIT=%s' % crawler.depth_limit,
            'covery_args':'%s|%s|%s|%s' % (
                    crawler.start_url,
                    crawler.allowed_domain,
                    hostname,
                    id
                )
            }

    try:
        print post_data_dic
        crl = pycurl.Curl()
        crl.fp = StringIO.StringIO()
        crl.setopt(crl.POSTFIELDS, urllib.urlencode(post_data_dic))
        crl.setopt(pycurl.URL, scrapyd_url)
        crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
        crl.perform()

        spider = anyjson.loads(crl.fp.getvalue())
        print spider

        if spider['status'] == 'ok':
            crawler.jobid = spider['jobid']
            crawler.status = 'START:start'
            crawler.save()
        else:
            crawler.status = 'ERROR:%s' % spider['message']
            crawler.save()

    except Exception, exc:
        crawler.status = 'ERROR:%s' % exc[1]
        crawler.save()

