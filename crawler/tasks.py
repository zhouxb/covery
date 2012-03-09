from celery.task import Task

class Crawler(Task):
    #name = 'task.crawler'
    #rounting_key = 'task.crawler'

    def run(self, name):
        print name

