# 写父类`Animal`

# - 实例属性：名字 name
# - 实例方法`speak()`：打印 “动物发出声音”

# 写子类`Dog`继承 Animal

# - 新增实例属性：品种 breed
# - 重写构造方法，同时调用父类构造
# - 重写`speak()`：打印 “汪汪”

# 写子类`Cat`继承 Animal

# - 重写`speak()`：打印 “喵喵”

# 测试：创建 Dog、Cat 实例，调用 speak ()

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


d = Dog("旺财", "柴犬")
c = Cat("大橘")
d.speak()           # 汪汪
c.speak()           # 喵喵
Animal.speak(c)         # 动物发出声音
Animal.speak(d)         # 动物发出声音