# 所谓带参数的装饰器就好像给装饰器套上了一层外壳，函数则被套上了两层外壳
# 其实这种结构就是：装饰器带参数 = 三层函数。retry(参数列表)返回真正的装饰器decorator

# 要求：让@retry(times=3)自动重试三次

import time, random
from functools import wraps

# retry装饰器(第一层外壳)
def retry(times=3, delay=0.5):
    # 第二层外壳
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:                    # 这里的try-except是异常处理机制
                    return fn(*args, **kwargs)
                except Exception as e:
                    print(f"第 {i + 1} 次失败：{e}")
                    time.sleep(delay)
            raise RuntimeError(f"{fn.__name__} 重试 {times} 次仍失败")
        return wrapper
    return decorator

@retry(times=3, delay=0.2)
def maybe_fail():
    if random.random() < 0.7:
        raise ValueError("network error")
    return "ok"

print(maybe_fail())