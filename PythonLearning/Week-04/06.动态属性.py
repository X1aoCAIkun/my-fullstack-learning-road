# Python作为一种动态语言，在实例化对象时不仅可以为实例属性进行传值
# 还可以为对象添加新属性


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student("张三", 18)
stu.sex = "男"          # 动态性的体现

# 但是如果想限制这种动态性，可以使用__slots__魔法方法，限定类的对象的属性
class Course:
    __slots__ = ("name")

    def __init__(self, name):
        self.name = name

cor = Course("python程序设计")
# AttributeError: 'Course' object has no attribute 'times'
# cor.times = 2