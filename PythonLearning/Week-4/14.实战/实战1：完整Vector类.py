import math
from dataclasses import dataclass


@dataclass
class Vec:
    x: float
    y: float

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vec(self.x * k, self.y * k)

    def length(self):
        return math.hypot(self.x, self.y)       # hypot()函数是计算(x**2 + y**2)**0.5

a = Vec(1, 2); b = Vec(3, 4)
print(a + b)            # Vec(x=3, y=6) 调用__add__()
print((b - a).length())         # 2.828...  调用__sub__()和length()
print(a * 3)        # Vec(x=3, y=6) 注意这里，__mul__()和__call__的调用方式不一样