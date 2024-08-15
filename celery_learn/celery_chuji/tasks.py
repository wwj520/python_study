"""
简单任务
"""

import time

from celery_chuji_1 import app
from celery.utils.log import get_task_logger


@app.task
def sum(x, y):
    return x + y


@app.task
def mul(x, y):
    time.sleep(5)
    return x * y