import time
from functools import wraps

# 计算一个函数的运行时间
def timer(fn):
    @wraps(fn)                      # 保留原函数的名字 / 文档
    def wrapper(*args, **kwargs):   # 通用：接收任何参数
        start = time.perf_counter()     # 返回一个时间戳
        result = fn(*args, **kwargs)        # 调用原函数
        cost = time.perf_counter() - start
        print(f"{fn.__name__} 用时 {cost:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))
# slow_sum 用时 0.0055s
# 499999500000

# 注意这里的@wraps(fn)删除不影响结果，但是在复杂的调试中不加的话就会出现找不到
# 函数的情况，因为被装饰的函数会“丢名字”