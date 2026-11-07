# 一些函数的函数体只有一两行，为了简化代码，同时提高速度美化代码
# 一般使用lambda匿名函数处理，lanmbda函数只写一行表达式

# 1.lambda 参数: 函数体（），返回值就是参数
square = lambda x: x * x
print(square(5))         # 25


# 2.常和sort/map/filter配合
nums = [(1, 2), (3, 1), (2, 5)]
nums.sort(key=lambda t: t[1])
print(nums)             # [(3, 1), (1, 2), (2, 5)]