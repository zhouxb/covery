from celery.task import task

@task(max_retries=2, queue='pbls', routing_key='pbl.probe', name='pbl.tasks.probe')
def probe(x, y):
    return x + y

