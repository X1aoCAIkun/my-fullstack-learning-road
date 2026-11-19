# 不仅函数可以被装饰器修饰，类也可以被装饰器修饰，比如之前的@dataclass

from functools import wraps


# CountCalls就是类装饰器
class CountCalls:
    def __init__(self, fn):
        wraps(fn)(self)         # 把fn的__name__、__doc__复制到self上
        self.fn = fn
        self.n = 0      # n就像闭包里的外部变量

    # 类装饰器就靠__call__让实例“像函数一样”被调用
    def __call__(self, *args, **kwargs):
        self.n += 1
        print(f"{self.__name__} 被调用第 {self.n} 次")
        return self.fn(*args, **kwargs) 

@CountCalls             # greet函数变成了一个CountCalls的实例对象
def greet(name):
    print(f"hi, {name}")

greet("a"); greet("b")