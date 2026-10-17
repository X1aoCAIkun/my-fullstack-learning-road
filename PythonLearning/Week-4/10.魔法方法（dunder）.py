# 所谓魔法方法就像内置函数的底层逻辑，是自动隐式调用的，
# 开头接尾会加上双下划线，写完魔法方法，类就像内置函数一样自然


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector{self.x}, {self.y}"

    # other是另一个实例化对象
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __len__(self):
        return 2

    def __getitem__(self, i):
        return (self.x, self.y)[i]          # ()就像tuple，[]就像下标

    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)

v1 = Vector(1, 2); v2 = Vector(3, 4)
print(v1 + v2)          # Vector(4, 6) 这里的+会自动隐式调用__add__
print(v1 == Vector(1, 2))       # True 这里的==会自动隐式调用__eq__
print(len(v1))          # 2 len()会自动隐式调用__len__
print(v1[0], v1[1])         # 1 2  这里会自动隐式调用__getitem__
print(v1(10))        # Vector(10, 20)  这里会隐式调用__call__ 