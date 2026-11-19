# 在继承时父类和子类可能会有相同名字的方法，但方法体又不同，这就形成了方法重写
# 这也是OOP的三大特性之一————多态的表现
# 多态让代码“对接口编程，不对实现编程”，扩展性强

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃饭")

    def speak(self):
        print("动物叫")

class Cat(Animal):
    def speak(self):
        print("喵")

class Dog(Animal):
    def speak(self):
        print("汪")

for pet in [Cat("大橘"), Dog("旺财")]:
    pet.speak()             # 喵 / 汪 同样的speak()不同的输出

c = Cat("梨花")
c.speak()       # 喵
Animal.speak(c)     # 动物叫