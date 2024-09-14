## 1. 在Docker中使用Supervisor
```textmate

运用过程管理工具，Supervisor，在容器中管理更多个进程。
利用Supervisor可以让我们更好的控制，管理，并重新启动，我们要运行的过程。
为了证明这一点我们要安装和管理一个SSH守护进程和一个Apache进程。

```

### 1.1 Docker文件配置
```Dockerfile
FROM harbor.hgj.net/library/hgj-python3.8:1.0
# 构建默认值
ARG SERVICE_NAME
ARG BUILD_ENV
# 服务名称
ENV APP_NAME $SERVICE_NAME
# 当前运行环境
ENV SERVER_ENV $BUILD_ENV
ADD . $APP_NAME
WORKDIR /$APP_NAME
ENV PYTHONPATH /$APP_NAME

RUN  mkdir logs && pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# Supervisor 配置文件
COPY ./scripts/supervisord_node.conf /etc/supervisor/conf.d/

# 配置 Supervisor 启动和管理 Gunicorn
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord_node.conf"]

```

### 1.2 Supervisor 配置文件
- 标准格式
```conf
[supervisord]
nodaemon=true

[program:sshd]
command=/usr/sbin/sshd -D

[program:apache2]
command=/bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 -DFOREGROUND"
-----------------------------------------
   supervisord.conf配置文件包含配置Supervisor 的指令和它管理的进程。第一个方括号[supervisord]提供了Supervisor 本身的配置。我们使用一个指令nodaemon ，
来告知Supervisor交互运行而不是守护化。
   接下来的两个方括号，管理我们希望控制的服务。每个方括号控制一个分离的进程。方括号包含一个单指令，command，该指令指定一条命令来运行启动每个进程。
```
- 示例demo
```textmate
[supervisord]
nodaemon=true
logfile=logs/supervisord.log  # 使用相对路径
pidfile=supervisord.pid
logfile_maxbytes=50MB
logfile_backups=1             # 保留 1 个备份日志文件。

[program:gunicorn]
command=gunicorn main:app     # 启动命令
directory=/%(ENV_APP_NAME)s   # %(ENV_APP_NAME)s 是一个环境变量占位符，表示使用环境变量 ENV_APP_NAME 的值作为
stdout_logfile=/dev/stderr    # 标准输出日志文件
stderr_logfile=/dev/stderr    # 错误输出日志文件
stdout_logfile_maxbytes=0 # 禁用标准输出日志文件的自动轮转
stderr_logfile_maxbytes=0 # 禁用错误输出日志文件的自动轮转
autostart=true            # 启动时自动启动
autorestart=true          # 程序在意外退出时自动重启。  

# cma爬虫
[program:celery_worker_cma]
command=celery worker --without-gossip --without-mingle --heartbeat-interval 60 -A tasks.cma.task -c 5 -E -Q cma_queue -l info -n cma.%%h -Ofair
directory=/%(ENV_APP_NAME)s
stdout_logfile=/dev/stderr
stderr_logfile=/dev/stderr
stdout_logfile_maxbytes=0 # 禁用标准输出日志文件的自动轮转
stderr_logfile_maxbytes=0 # 禁用错误输出日志文件的自动轮转
autostart=true
autorestart=true



```

