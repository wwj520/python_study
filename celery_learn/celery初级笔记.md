# 1 celery 入门
- celery是一个简单，灵活、可靠的分布式任务执行框架，可以支持大量任务的并发执行。celery采用典型生产者和消费者模型。生产者提交任务到任务队列，众多消费者从任务队列中取任务执行。
### 1.1 celery架构
-    Celery由以下三部分构成：消息中间件(Broker)、任务执行单元Worker、结果存储(Backend)
    ![img.png](celery_chuji/img.png)
-  执行流程
   ```
    任务调用提交任务执行请求给Broker队列
    如果是异步任务，worker会立即从队列中取出任务并执行，执行结果保存在Backend中
    如果是定时任务，任务由Celery Beat进程周期性地将任务发往Broker队列，Worker实时监视消息队列获取队列中的任务执行

   ```
# 2. Celeryd简单开发实例
- celery的应用开发涉及四个部分
  ```
    celery 实例初始化
    任务的定义（定时和实时任务）
    任务worker的启动
    任务的调用
  ```
### 2.1 项目目录demo
```textmate
# 项目目录
wedo
.
├── config.py
├── __init__.py
├── period_task.py
└── tasks.py
```
### 2.2 celery 实例初始化
    celery的实例化，主要包括执行Broker和backend的访问方式，任务模块的申明等

```python
# celery 实例初始化 
# __init__.py
from celery import Celery
app = Celery('wedo')  # 创建 Celery 实例
app.config_from_object('wedo.config') 

# 配置config
# config.py
BROKER_URL = 'redis://10.8.238.2:6379/0' # Broker配置，使用Redis作为消息中间件
CELERY_RESULT_BACKEND = 'redis://10.8.238.2:6379/0' # BACKEND配置，这里使用redis
CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间
CELERY_TIMEZONE='Asia/Shanghai'   # 时区配置
CELERY_IMPORTS = (     # 指定导入的任务模块,可以指定多个
    'wedo.tasks',
    'wedo.period_task'
)
````
### 2.3 任务的定义
- celery中通过@task的装饰器来进行申明celery任务，其他操作无任何差别
- 定时任务和实时任务的区别主要是要申明何时执行任务，任务本身也是通过task装饰器来申明 何时执行任务有2种
    ```textmate
        指定频率执行：sender.add_periodic_task(时间频率单位s, 任务函数, name='to_string')
        crontab方式：分钟/小时/天/月/周粒度， 可以支持多种调度
    ```
   
    



