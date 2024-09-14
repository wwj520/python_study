from functools import lru_cache, wraps
from datetime import datetime, timedelta


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


import time

@timed_lru_cache(seconds=5)
def expensive_function(n):
    print(f"Calculating for {n}...")
    time.sleep(2)  # Simulate an expensive computation
    return n * n

# 第一次调用，计算并缓存结果
print(expensive_function(5))

# 在缓存有效期内再次调用，直接返回缓存结果
print(expensive_function(5))

# 等待缓存过期
time.sleep(7)

# 缓存过期后再次调用，重新计算
print(expensive_function(5))