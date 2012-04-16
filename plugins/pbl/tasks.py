from celery.task import task
import json
import urllib2

#@task(max_retries=2, queue='pbls', routing_key='pbl.probe', name='pbl.tasks.batch_probe')
#def probe(survey_show_url, state_create_url, mail_create_url):
    #task = json.load(urllib2.urlopen(survey_show_url))
    #print task

#@task(max_retries=2, queue='pbls', routing_key='pbl.schedule', name='pbl.tasks.schedule')
#def schedule(survey_show_url, state_create_url, mail_create_url, minute):
    #task = json.load(urllib2.urlopen(survey_show_url))
    #print task

@task(name='pbl.tasks.probe')
def probe(survey_show_url, state_create_url, mail_create_url):
    pass

@task(name='pbl.tasks.schedule')
def schedule(survey_show_url, state_create_url, mail_create_url, minute):
    pass
