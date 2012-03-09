from celery.decorators import task
from celery.task import Task
from djcelery.views import task_webhook

@task
def add(x, y):
    return x + y

#@task_webhook
#def t(x, y):
    #return x + y

#class UpdateStatus(Task):
    #name = 'task.updatestatus'
    #rounting_key = 'task.updatestatus'
    #ignore_result = True

    #default_retry_delay = 5 * 60
    #max_retries = 12
    #rate_limit = '10/s'

    #def run(self, name):
        #print name

