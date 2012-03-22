
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
    "pbls": {
        "binding_key": "pbl.#",
    },
}

CELERY_DEFAULT_QUEUE = "default"
CELERY_DEFAULT_EXCHANGE = "tasks"
CELERY_DEFAULT_EXCHANGE_TYPE = "topic"
CELERY_DEFAULT_ROUTING_KEY = "task.default"

CELERY_ROUTES = {
    'pbl.tasks.probe':
    {
        'queue': 'pbls',
        'routing_key':'pbl.probe',
    },
}

