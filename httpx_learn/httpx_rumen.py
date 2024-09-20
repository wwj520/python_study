# -*- coding:utf-8 -*-
# @FileName  :httpx_rumen.py
# @Time      :2024/9/14
# @Author    :Jack

import httpx
r = httpx.get('http://github.com/')
print(r.status_code)
print(r.history)  # 查看重定向的记录
print(r.next_request)  # 获取到重定向以后的请求对象
resp = httpx.Client().send(r.next_request) # 对请求对象发送请求
print(resp.text)