
"""
周期性任务

"""
from celery_chuji_1 import app
from celery.schedules import crontab


# 1.这个装饰器用于连接一个函数到Celery应用的配置完成事件。当Celery应用配置完成后，这个函数会被调用。
@app.on_after_configure.connect
# 2. add_periodic_task: 这个函数用于设置周期性任务。sender 参数是Celery应用实例，**kwargs 是额外的关键字参数。
def setup_periodic_tasks(sender, **kwargs):

    # 3. 这行代码添加了一个每5秒执行一次的周期性任务。
    # to_string.s("celery task") 是一个任务签名，.s() 是 si() 方法的简写形式，表示一个非阻塞的（non-blocking）任务签名。它允许你传递任务参数，并创建一个可以立即执行或稍后执行的任务签名对象。
    # 表示要执行的任务和传递给任务的参数。to_string 是任务的名称，"celery task" 是传递给任务的参数。
    sender.add_periodic_task(5.0, to_string.s("celery task"), name='to_string')

    # 4. 每10分钟执行一次
    sender.add_periodic_task(crontab(minute='*/10'), send_mail.s('send mail'), name='send_mail')


@app.task
def to_string(text):
    return 'this is a %s' % text


@app.task
def send_mail(content):
    print('send mail, content is %s' % content)