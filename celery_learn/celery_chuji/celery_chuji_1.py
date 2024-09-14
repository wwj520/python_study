# -*- coding: utf-8 -*
"""
celery 初始化
"""
from celery import Celery

# 创建celery实例
app = Celery('wedo')

# 加载配置
app.config_from_object("config")  # noqa




