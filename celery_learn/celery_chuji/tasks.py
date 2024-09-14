"""
简单任务
"""

import time

from celery_chuji_1 import app
from celery.utils.log import get_task_logger
celery_logger = get_task_logger(__name__)

@app.task(bind=True)
def sum_test(self, x, y):
    celery_logger.info("sum_test: {} {}".format(x,y))
    print(self.request.hostname, self.request.headers)
    return x + y


@app.task
def mul(x, y):
    time.sleep(5)
    return x * y