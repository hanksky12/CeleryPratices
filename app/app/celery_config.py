env = 'dev'

broker_url = 'amqp://root:1234@localhost:5672' if env == "docker" else 'amqp://root:1234@rabbitmq:5672'

result_backend = 'redis://localhost:6379/0' if env == "docker" else 'redis://redis:6379/0'

include = ['app.app.tasks.tasks', 'app.app.tasks.cron_tasks']

broker_connection_retry_on_startup = True

beat_schedule = {
    'distributed_add_task': {
        'task': 'distributed_add_task',
        'schedule': 20.0,
    },
    'distributed_sub_task': {
        'task': 'distributed_sub_task',
        'schedule': 30.0,
    },
}

task_routes = {'distributed_sub_task': {'queue': 'queue1'}, 'sub': {'queue': 'queue1'}}
