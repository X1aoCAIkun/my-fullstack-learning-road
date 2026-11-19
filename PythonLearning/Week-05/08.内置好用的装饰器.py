# @lru_cache自动缓存装饰器
from functools import lru_cache

# 如果没cache这个程序根本跑不完
@lru_cache(maxsize=None)        # 这就可以看出lru_cache是带参数的装饰器
# 斐波那契数列
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))


# partial固定部分参数
from functools import partial


def power(base, exp):
    return base ** exp

# 可以看出partial是个类，但是它是一个偏函数，提前固定一部分参数，生成一个新函数
square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5), cube(2))       # 25 8
