from celery import Celery

from . import celery_config

app = Celery('distributed_celery')
app.config_from_object(celery_config)