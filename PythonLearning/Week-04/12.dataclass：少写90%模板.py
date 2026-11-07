# dataclass是一种专门为数据设计的类，它自带__init__\__repr__\__eq__等魔法方法
# 同样在类前用@注明就可以，但需要导入


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int = 0          # 注明x, y的类型，并为y设默认值

p1 = Point(1, 2)
p2 = Point(1, 2)            # 二者自动调用__init__
print(p1)               # Point(x=1, y=2)   自动调用__repr__ 注意这里输出会关键字注明值            
print(p1 == p2)     # True   自动调用__eq__


# @dataclass(frozen=True) 会使实例对象的属性不可变
# 但是属性可变那这样依旧不能阻止（如属性是list，那么它其中的元素依然可变）


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "CNY"
    
@dataclass(frozen=True)
class Demo:
    nums: list     # 注意这里不能赋默认值[]，这个[]是创建类是就创建好的，所有对象共用一个列表就会报错
    # 如果一定要默认值是空列表，可以用filed()
    # nums: list = filed(default_factory=list)   # 这样每个实例对象都有个独立的列表

d = Demo([1, 2, 3])
# d.nums = [4, 5, 6]        #报错
d.nums.append(4)