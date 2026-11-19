# 为提高编码效率，Python内置一个语法糖：yield来生成迭代器
# 类比：yield就像电视的“暂停键”。普通函数在return后就结束了，内存释放；带yield
# 的函数遇到yield就会暂停，把值接"递"出去，函数的局部变量、行号都被冻结；下次
# next()时就会从那一行继续

def countdown(n):
    while n > 0:
        yield n         # 把 n 递出去，函数暂停在这里
        n -= 1          # 在下一次迭代时执行

for x in countdown(3):
    print(x)

# 注意：只要函数里出现了 yield，这个函数就"不普通"，调用它不会执行函数体，而是
# 返回一个生成器对象（一种迭代器）。函数体直到next()才会跑
g = countdown(3)
print(g)            # <generator object countdown at 0x...>
print(type(g))      # <class 'generator'>
print(next(g))      # 3

# 生成器函数与普通函数的区别
# 关键字：              yield    return
# 调用时执行函数体？：   返回generator    立即执行
# 局部变量保留？：       暂停时冻结      退出即销毁
# 内存占用：            用一个算一个    一次性算完