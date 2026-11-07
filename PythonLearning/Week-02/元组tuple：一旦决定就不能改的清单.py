# 元组就像一张已经打印出来的清单，上面的内容不可更改，但是可以被查询
# 由此可知，元组是有序的、不可变的、可重复的
# 同列表一样，元组也可以通过下标索引查找元素
# 一般在数据不变且有意义（坐标、日期等）的时候使用元组


# 1.元组的定义
# 形式：元组名 = ()，同列表一样元组中的元素类型可以是任意的
point = (3, 4)
print(point[0], point[1])       # 3, 4  根据下标索引输出元素
# point[0] = 10         # 报错TypeError，元组是不可变的
# 注意当元组中只有一个元素时，也必须要有','，如果没有，这个变量的类型就是元素的类型而不是tuple
a = ()          # 空元组
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>


# 2.解包（很常用，也很重要）
# 也就是多个变量依次接收元组中的元素,注意元素数量一定要与变量数量对应
x, y = point
print(x, y)         # 3, 4
# 打包操作就是解包的逆过程
num1 = 1, 10, 100
print(type(num1))       # <class 'tuple'>
print(num1)         # (1, 10, 100)
# 可以用‘*’解决元素数量和变量数量的不对应，但‘*’只可以出现一次，‘*’也可以运用在其他序列中
num2 = 1, 10, 100, 1000
i, j, *k = num2
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = num2
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = num2
print(i, j, k)        # [1, 10] 100 1000
*i, j = num2
print(i, j)           # [1, 10, 100] 1000
i, *j = num2
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = num2
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = num2
print(i, j, k, l, m)  # 1 10 100 1000 []



# 3.一行交换两个变量（多个变量对应位置接收元素）与解包类似
a, b = 1, 2
a, b = b, a
print(a, b)         # 2, 1


# 4. namedtuple：给位置起名字（元组中的位置起别名），起到代替下标更易读的作用
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])         # 模板 = namedtuple(类型，[从下标0开始的位置别名])
p  = Point(3, 4)        # 元组名 = 模板(元素)
print(p.x, p.y)         # 3, 4  等效于p[0], p[1]


# 5.1元组也可使用切片(切片依然为列表)
t1 = (35, 12, 98, 100)
print(t1[:2])       # (35, 12)
print(t1[::3])      # (35, 100) 

# 5.2可以使用循环遍历元组中的元素
for elem in t1:
    print(elem)         # 35, 12, 98, 100

# 5.3可以使用成员运算
print(12 in t1)         # True
print(99 in t1)         # False

# 5.4可以使用拼接运算
t2 = (10)
t3 = t1 + t2
print(t3)               # (35, 12, 98, 100, 10)

# 5.4可以使用比较运算
print(t1 == t2)         # False
print(t1 != t2)         # True
print(t1 <= (32, 11, 99))       # False

