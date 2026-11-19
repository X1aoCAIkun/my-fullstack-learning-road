# 沿用第 2 题的 Animal、Dog、Cat

# 1. 写一个函数 `animal_talk(animal_obj)`，接收动物对象，
# 直接调用`animal_obj.speak()`
# 2. 分别传入 Dog 实例、Cat 实例，观察调用结果
# 3. 新增一个`Bird`类，继承 Animal，speak 输出 “叽叽”，同样传入 animal_talk 测试


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("动物发出声音")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("汪汪")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("喵喵")

class Bird(Animal):
    def speak(self):
        print("叽叽")


def animal_talk(animal_obj):
    animal_obj.speak()

d = Dog("旺财", "柴犬")
c = Cat("大橘")
b = Bird("乐迪")
animal_talk(d)
animal_talk(c)
animal_talk(b)