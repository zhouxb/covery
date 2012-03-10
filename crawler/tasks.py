from datetime import timedelta
from celery.task import Task, PeriodicTask

class Crawler(Task):
    #name = 'task.crawler'
    #rounting_key = 'task.crawler'

    def run(self, name):
        print name

class Say(Task):
    def run(self):
        print 'say'

class PeriodicCrawler(PeriodicTask):
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info('Running full name task')

        return 100

#from djcelery.models import IntervalSchedule
#from celery.schedules import schedule
#from datetime import timedelta

#sched = IntervalSchedule.from_schedule(schedule(timedelta(hours=3)

