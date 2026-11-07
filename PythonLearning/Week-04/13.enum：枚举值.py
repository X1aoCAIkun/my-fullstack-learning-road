# 枚举就是固定一组常量集合

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

c = Color.RED       # 这里c是引用了枚举成员RED
print(c, c.name, c.value)           # Color.RED RED 1
print(Color(1))             # Color.RED  这里是按值查找枚举成员
print(Color["BLUE"])        # 3  按枚举成员名查找枚举成员
print(Color.RED == Color.RED)           # True 枚举对象是唯一的

# 注意不允许在类外添加枚举成员
Color.YELLOW = 4          # 不报错，因为这只是给类新增了一个普通类属性
# print(Color(4))    # 报错