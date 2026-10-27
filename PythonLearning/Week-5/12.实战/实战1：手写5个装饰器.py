import json, time
from functools import wraps


# 1. timer装饰器（计算函数运行时间）
def timer(fn):
    @wraps(fn)
    def wrapper(*arg, **kwargs):
        s = time.perf_counter()
        r = fn(*arg, **kwargs)
        print(f"[timer] {fn.__name__} {time.perf_counter() - s:.4f}s")
        return r
    return wrapper

# 2. retry装饰器（带参数）（统计函数times次运行出现问题的次数）
def retry(times=3):
    def deco(fn):
        @wraps(fn)
        def wrapper(*arg, **kwargs):
            for i in range(times):
                try:
                    return fn(*arg, **kwargs)
                except Exception as e:
                    print(f"第{i + 1}次失败 {e}")
            raise       # 防止times次运行都失败而使得wrapper没有返回值
        return wrapper
    return deco

# 3. cache装饰器（缓存）相当于lru_cache装饰器
def cache(fn):
    store = {}
    @ wraps(fn)
    def wrapper(*arg):
        key = json.dumps(arg, default=str)
        if key not in store:
            store[key] = fn(*arg)
        return store[key]
    return wrapper

# 4. deprecated装饰器（带参数）
def deprecated(reason=""):
    def deco(fn):
        @wraps(fn)
        def wrapper(*arg, **kwargs):
            print(f"[弃用] {fn.__name__} {reason}")
            return fn(*arg, **kwargs)
        return wrapper
    return deco

# 5. validate装饰器（带参数）（参数校验）
def validate(**rules):
    def deco(fn):
        @wraps(fn)
        def wrapper(*arg, **kwargs):
            for k, t in rules.items():
                if k in kwargs and not isinstance(kwargs[k], t):
                    raise TypeError(f"{k} 必须是 {t.__name__}")
            return fn(*arg, **kwargs)
        return wrapper
    return deco

# 这里fib先被cache包装，再被timer包装
@timer
@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

@validate(s=int)
def square(*, s):
    return s * s

print(fib(20))          # 计算 + 缓存，fib再次调用即从cache读
print(square(s=5))
print(square(s="x"))        # 抛出异常