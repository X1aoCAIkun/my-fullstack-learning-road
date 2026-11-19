# 类由class关键字标识，后面加"类名:"（命名规则:大驼峰）
class Pet:          # 类名约定首字母大写
    # 构造函数，实例化对象的“摸具”
    def __init__(self, name: str, age: int):     
        self.name = name            # self = 当前实例
        self.age = age

    # 实例方法，就是实例对象可以用"."调用的功能函数
    def bark(self):
        print(f"{self.name}在叫！")

# 实例化对象：变量 = 类名(属性)
dog = Pet("旺财", 3)        # 这里会调用构造方法__init__，“不用写new！”
dog.bark()          # 旺财在叫！，调用实例方法
print(dog.name, dog.age)        # 旺财 3  对象属性也可以调用

# 注意： __init__是初始化方法，对象一造出来就调用，给对像“装属性”
# self永远是类中函数的第一个参数，代表“对象自己这个实例”


# 练习：写一个Circle类，属性radius，方法area()返回面积
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{pi * self.radius ** 2:.2f}"       # 结果保留两位小数

c1 = Circle(2)
print(c1.radius)        # 2
print(c1.area())        # 12.57
# 也可以不实例化对象，直接用
print(Circle(2).area())         # 12.57