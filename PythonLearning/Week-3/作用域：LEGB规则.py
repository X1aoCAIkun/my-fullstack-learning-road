# Python函数寻找变量遵顼LEGB规则
# L(Local)函数的局部变量->E(Enclosing)外部函数的变量（嵌套函数）->
# G(Global)模块变量（全局变量）->B(Built-in)print/len/range这些python自带的


x = 'global'        # 模块变量

def outer():
    x = 'outer'         # outer函数的局部变量，inner函数的外部函数变量
    def inner():
        # x = 'inner'       # inner函数的局部变量，取消注释会变inner
        print(x)        # 找不到inner，往上找outer
    inner()
outer()             # outer

# 修改全局变量（使用global关键字）
count = 0
def incr():
    global count            # 不用global就会变成incr函数的局部变量
    count += 1
incr()
print(count)        # 1