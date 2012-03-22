from celery.task import task
import json
import urllib2

@task(max_retries=2, queue='pbls', routing_key='pbl.probe', name='pbl.tasks.probe')
def probe(survey_show_url, state_create_url):
    task = json.load(urllib2.urlopen(survey_show_url))
    print task


