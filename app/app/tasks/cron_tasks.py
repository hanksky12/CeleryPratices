from celery import chord
from ..celery_app import app
from .tasks import add, tsum, sub


@app.task(name='distributed_add_task')
def distributed_add_task():
    print('Large task started')
    task_list = []
    for i in range(100):
        task = add.signature((i, 10), countdown=1)
        task_list.append(task)

    result = chord(task_list)(tsum.s()).get()
    print(result.get())
    print('Large task finished')


@app.task(name='distributed_sub_task')
def distributed_sub_task():
    print('task started')
    result = sub.s(100, 10).apply_async()
    print(result.get())
    print('task finished')
