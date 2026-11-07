# 第一节练习
def fire_ball(x):
    return x * 2
def ice_arrow(x):
    return x + 10
def heal(x):
    return x + 5
def thunder(x):
    return x ** 2

# 函数可以被装进变量
spells = [fire_ball, ice_arrow, heal, thunder]
for skill in spells:
    print(skill(3))

# 函数可以作为参数
def cast(fn, x):
    return fn(x)
print(cast(fire_ball, 10))
print(cast(thunder, 5))

# 函数可以作为返回值
def spell_factory(kind: str):
    for skill in spells:
        if kind in skill.__name__:
            return skill
fire = spell_factory("fire")
print(fire(5))


# 第二节练习
def make_mana_tracker(initial_total: int):
    total = initial_total
    def spend(x):
        nonlocal total
        total -= x
        return total
    return spend
mana = make_mana_tracker(100)
print(mana(30))
print(mana(20))
print(mana(80))

def make_enchant(n):
    def enchant(x):
        return n + x
    return enchant
enchant5 = make_enchant(5)
enchant10 = make_enchant(10)
print(enchant5(3), enchant10(3))



# 第三节练习
def shout(fn):
    def wrapper(name):
        return fn(name).upper() + "!!!"
    return wrapper
# 不用@版
def announce(name: str):
    return f"{name} 释放了火球术"
announce = shout(announce)
print(announce("simon"))
# 带@版本
@shout
def declare(name: str):
    return f"{name} 释放了雷霆术"
print(declare("sc"))
print(declare.__name__)         # wrapper



# 第四节练习
from functools import wraps
import time

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fn.__name__} 用时 {end - start:.4f}s")
        return result
    return wrapper
@timer
def big_chart(n):
    return sum(range(n))
print(big_chart(1_000_000))
print(big_chart.__name__)



# 第五节练习
def repeat(n):
    def decorate(fn):
        def wrapper():
            for _ in range(n):
                fn()
        return wrapper
    return decorate
@repeat(3)
def cast_spell():
    print("火球术")
cast_spell()



# 综合练习

def cooldown(n):
    def decorate(fn):
        start = 0
        @wraps(fn)
        def wrapper(*args, **kwargs):
            nonlocal start
            end = time.perf_counter()
            if end - start >= n:
                start = time.perf_counter()
                return fn(*args, **kwargs)
            else:
                print(f"{fn.__name__} 冷却中，请稍候...")
        return wrapper
    return decorate

@cooldown(2)
def big_spell():
    print("究极魔法，释放")

big_spell()
big_spell()
time.sleep(2)
big_spell()            