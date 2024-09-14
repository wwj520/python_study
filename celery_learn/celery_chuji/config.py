broker_url = 'redis://:123456@dev-middle.hgj.net:6379/0'            # Broker配置，使用Redis作为消息中间件
result_backend = 'redis://:123456@dev-middle.hgj.net:6379/0'  # BACKEND配置，这里使用redis密码的设置

result_serializer = 'json'                  # 结果序列化方案
task_result_expires = 60 * 60 * 24            # 任务过期时间
timezone = 'Asia/Shanghai'                    # 时区配置
broker_connection_retry_on_startup = True     # 添加此配置项：决定是否在启动时重试 broker 连接
worker_concurrency = 3                        # 并发数

imports = (     # 指定导入的任务模块,可以指定多个
    'tasks',
)
