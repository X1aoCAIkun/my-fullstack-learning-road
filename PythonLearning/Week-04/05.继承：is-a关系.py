# 在前面我们讲到，类就像一个模板，但模板之间也存在相似性，类与类之间的“父子关系”
# 就可以是由继承这个“is-a关系”实现
# 子类可以继承父类的属性和方法，也可以有自己的属性和方法


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃饭")

# Dog也是一种Animal，所以Dog模板就可以继承Animal模板
# 形式：class 类名(继承的类名):，括号里默认是object类————意味着所有的类都是object的子类
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)          # 这里会调用父类Animal的__init__方法
        self.breed = breed

    def bark(self):
        print(f"{self.name}（{self.breed}）汪汪汪")


d = Dog("旺财", "柴犬")
d.eat()             # 旺财 在吃饭    Dog类的eat方法是继承父类Animal来的
d.bark()            # 旺财（柴犬）汪汪汪

# 注意super()是“找父类的快捷方式”，避免硬编码父类民名