# ============================================================
# 13. 第7~11节练习
# 每道题的主体照第7~11节的例题来(先练熟套路),
# 但都留了一个需要想一想的小改动,注意看"想一想"
# 答案写在对应题目的注释下方
# ============================================================


# ---------- 第7节:类装饰器 ----------
# 题目1:照第7节的 CountCalls 写一个类装饰器 CallLogger:
#   1. 定义一个函数 say_hi(name),打印 "hi, {name}"
#   2. 用 @CallLogger 装饰它:每次调用打印 "say_hi 第X次被调用",
#      并把本次的参数(元组 args)存进 self.calls 列表
#   3. 调用三次,然后直接打印 say_hi.calls 查看记录
# 想一想:装饰之后 say_hi 变成了 CallLogger 的实例对象,
#        所以能像普通对象一样访问它的属性

from functools import wraps

class CallLogger:
    def __init__(self, fn):
        wraps(fn)(self)
        self.fn = fn
        self.calls = []
        self.n = 0

    def __call__(self, *args, **kwds):
        self.n += 1
        print(f"{self.__name__} 第 {self.n} 次调用")
        self.calls.append(args)
        return self.fn(*args)

@CallLogger
def say_hi(name):
    print(f"hi {name}")

say_hi("a")
say_hi("b")
say_hi("c")
print(say_hi.calls)

# ---------- 第8节:lru_cache 与 partial ----------
# 题目2:爬楼梯问题——一次能爬 1 级或 2 级,爬到第 n 级有多少种方法?
#   1. 写递归函数 climb(n),用 @lru_cache(maxsize=None) 装饰
#   2. 打印 climb(30) 的结果,再打印 climb.cache_info()
# 想一想:这个递归和斐波那契几乎一样,但"台阶"的边界条件怎么写?
#        (爬到第 0 级、第 1 级各有几种方法?)

from functools import lru_cache

@lru_cache(maxsize=None)
def climb(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    return climb(n-1) + climb(n-2)

print(climb(30))
print(climb.cache_info())

# 题目3:照第8节的例子用 partial 做两个工具:
#   1. 定义 power(base, exp) = base ** exp,
#      固定 exp 做出 square 和 cube,测试 square(5)、cube(2)
#   2. 固定 int 的 base=2,做一个"二进制字符串转十进制"的工具,
#      试试 parse_bin("101") 是不是 5
# 想一想:partial 固定过的参数,调用时还能覆盖吗?     可以覆盖（直接位置传参也可以）
#        试试 square(5, exp=3) 看看结果

from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5), cube(2))
parse_bin = partial(int, base=2)
print(parse_bin("101"))
print(square(5, exp=3))

# ---------- 第9节:上下文管理器类 ----------
# 题目4:照第9节的 Timer 写一个类上下文管理器,并加一点新东西:
#   1. __enter__ 记录开始时间
#   2. __exit__ 打印 "耗时 X.XXXXs",并且:
#      - 如果块内没异常(exc_type 是 None),打印 "顺利完成"
#      - 如果块内有异常,打印 "块内出错: {异常类型名}",但不要吞掉异常
#   3. 先正常测一次 sum(range(10_000_000));
#      再用 try 包住一个会报错的 with 块,观察输出
# 想一想:__exit__ 的三个参数什么时候是 None?  没有异常的时候就都是None

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"耗时 {time.perf_counter() - self.start:.4f}s")
        if exc_type == None:
            print("顺利完成")
        else:
            print(f"块内出错：{exc_type.__name__}")

with Timer() as t:
    sum(range(10_000_000))

try:
    with Timer() as t:
        1 / 0
except ZeroDivisionError as e:
    print(e)


# ---------- 第10节:@contextmanager ----------
# 题目5:用 @contextmanager 重写题目4的计时器,要求:
#   1. 带 label 参数,用法:with timer("求和"):
#   2. yield 前开始计时,yield 后打印 "{label} 耗时 X.XXXXs"
#   3. 块内抛异常时:耗时照样打印,异常还要继续向外抛(不能吞掉)
# 想一想:为什么把打印放进 finally 里,异常时耗时也照样打印?     无论是否异常finally块都会执行
#        如果放在 yield 后面普通位置会怎样?试试     这样出错了yield会直接打断程序

from contextlib import contextmanager

@contextmanager
def timer(label=None):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label} 耗时 {time.perf_counter() - start:.4f}s")

with timer("求和"):
    sum(range(10_000_000))

try:
    with timer("测试出错"):
        1 / 0
except Exception as e:
    print(e)

# ---------- 第11节:异常处理 ----------
# 题目6:写 safe_divide(a, b),返回 a / b:
#   1. 完整写出 try/except/else/finally:
#      - except ZeroDivisionError: 打印 "除数不能为0"
#      - except Exception as e:   打印 "其他错误 {e}"
#      - else:                    打印 "结果是 {结果}"
#      - finally:                 打印 "运算结束"
#   2. 分别用 (10, 2) 和 (10, 0) 测试

def safe_divide(a, b):
    return a / b
try:
    # result = safe_divide(10, 2)
    result = safe_divide(10, 0)
except ZeroDivisionError:
    print("除数不能为0")
except Exception as e:
    print(f"其他错误 {e}")
else:
    print(result)
finally:   
    print("运算结束")

# 题目7:照第11节写自定义异常 withdraw:
#   1. 定义 InsufficientFundsError(Exception),docstring 写 "余额不足"
#   2. 写 withdraw(balance, n):
#      - n <= 0 时,raise ValueError("取款金额必须为正数")
#      - n > balance 时,raise InsufficientFundsError
#      - 否则返回 balance - n
#   3. 外层 try 按顺序捕获:ValueError、InsufficientFundsError,
#      最后加 except Exception as e 兜底
# 想一想:except Exception 为什么必须放在最后?放最前面会怎样? 它会捕获所有异常，其他except不会执行，放最后就可以兜底

class InsufficientFundsError(Exception):
    """余额不足"""

def withdraw(balance, n):
    if n <= 0:
        raise ValueError("取款余额必须为正数")
    elif n > balance:
        raise InsufficientFundsError("余额不足")
    return balance - n

balance = 100

try:
    n = int(input("输入取钱数："))
    print(withdraw(balance, n))
except ValueError as v:
    print(v)
except InsufficientFundsError as i:
    print(i)
except Exception as e:
    print("其他错误", e)


# 题目8:异常链(和第11节一样):
#   1. 写 load_config(path),函数内部执行 int("abc") 触发 ValueError
#   2. 捕获它之后,raise RuntimeError("解析配置失败") from e
#   3. 外层捕获 RuntimeError,打印它和它的 __cause__
# 想一想:__cause__ 里装的是什么?(实验:临时去掉 from e 再跑一次,
#        报错信息有什么变化?记得外层用 try 接住)
# 有from e就是ValueError的起因，没有就是None

def load_config(path):
    try:
        int(path)
    except ValueError as e:
        raise RuntimeError("解析配置失败") from e

try:
    load_config("abc")
except RuntimeError as r:
    print(r, r.__cause__)

# ---------- 综合练习:魔法师施法 ----------
# 题目9:把第 7/10/11 节串起来,做一个小场景:
#   1. 用类装饰器 CountCalls 装饰 fireball(name):
#      每次调用打印 "fireball 第X次释放!",函数里打印 "{name} 被火球击中了"
#   2. 用 @contextmanager 写 timer(label)(题目5的样子)
#   3. 自定义异常 ManaError(Exception),docstring 写 "蓝量不足";
#      写 cast(mana, cost):
#      mana < cost 就 raise ManaError(f"蓝量不足:需要 {cost},只有 {mana}")
#      否则返回 mana - cost
#   4. 用 with timer("施法") 包住:先 fireball("小明"),再打印 cast(100, 30) 的结果
#   5. 外层用 try/except ManaError as e/else/finally 包住整个 with 块;
#      再把 cast(100, 30) 改成 cast(10, 30) 跑一次,观察输出顺序:
#      哪些打印先出现?"战斗结束"类的清理输出在 except 之前还是之后?
# yield后的内容先出现了；之后

class CountCalls:
    def __init__(self, fn):
        self.fn = fn
        self.n = 0

    def __call__(self, *args, **kwds):
        self.n += 1
        print(f"fireball 第 {self.n} 次释放")
        return self.fn(*args, **kwds)

@CountCalls
def fireball(name):
    print(f"{name} 被火球击中了")

@contextmanager
def timer(label="任务"):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label} 耗时 {time.perf_counter() - start:.4f}s")

class ManaError(Exception):
    """蓝量不足"""

def cast(mana, cost):
    if mana < cost:
        raise ManaError(f"蓝量不足:需要 {cost},只有 {mana}")
    return mana - cost


with timer("施法"):
    fireball("小明")
    print(f"剩余蓝量：{cast(100, 30)}")

try:
    with timer("施法"):
        fireball("小红")
        left = cast(10, 30)
except ManaError as m:
    print(m)
else:
    print("剩余蓝量：", left)
finally:
    print("战斗结束")