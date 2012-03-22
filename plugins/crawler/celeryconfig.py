
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("tasks", )

CELERY_QUEUES = {
    "default": {
        "binding_key": "task.#",
    },
    "crawlers": {
        "binding_key": "crawler.#",
    },
}

CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE = "tasks"
CELERY_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_DEFAULT_ROUTING_KEY = "task.default"

CELERY_ROUTES = {
    'crawler.tasks.crawl':
    {
        'queue': 'crawlers',
        'routing_key':'crawler.crawl',
    },
}

