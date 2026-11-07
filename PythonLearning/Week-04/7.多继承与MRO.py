# 在继承的过程中，我们可能会遇到一个类继承了两个父类的情况
# 此时子类调用方法由MRO（方法解析顺序），由C3算法决定
# 注意：多继承容易混乱，能不用就不用。可以用mixin(专门提供一组方法的小类)来组合


class A:
    def hi(self):
        print("A")

class B(A):
    def hi(self):
        print("B")
        

class C(A):
    def hi(self):
        print("C")

class D(B, C):
    pass

D().hi()            # B 按MRO找到第一个hi方法
print(D.__mro__)    # C3的合并顺序(D, B, C, A, object)