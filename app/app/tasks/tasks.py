import time

from ..celery_app import app


@app.task(name='add')
def add(x, y):
    value = x + y
    time.sleep(3)
    print(value)
    return value


@app.task(name='sub')
def sub(x, y):
    value = x - y
    time.sleep(4)
    print(value)
    return value


@app.task(name='tsum')
def tsum(numbers):
    value = sum(numbers)
    print(value)
    return value