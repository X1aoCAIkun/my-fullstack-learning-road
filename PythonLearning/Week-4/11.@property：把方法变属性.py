# @property注明的函数可以在调用时不用写括号，就像调用属性一样


class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def radius(self):
        return self._r

    @radius.setter          # 注明是设值函数，与上面的函数做区分
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")        # 抛出异常
        else:
            self._r = value
            
    @property
    def area(self):
        return 3.14159 * self._r ** 2

c = Circle(3)
print(c.radius)         # 3 不用写括号
print(c.area)           # 28.27....
c.radius = 5            # 这里是设值，所以会进入第二个radius函数
print(c.radius)         # 5
# c.radius = -1         # ValueError 