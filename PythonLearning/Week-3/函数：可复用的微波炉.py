# 函数也称为方法（在面向对象时），它时编码模块化的具体体现
# 函数=微波炉；输入（食材）->加热(处理) ->输出（熟食）
# 如果一个程序中的某一部分功能被反复使用，此时就可以将这个功能写成函数，使代码更简洁，可读性强


# 1.函数的定义与调用
# 形式：def 函数名(参数):，同样四格缩进区分函数体
def greet(name):        # def定义，name是参数
    return f"你好，{name}"      # return就是返回结果，将“熟食端出来”

msg = greet("小明")         # 函数的调用，msg变量接收结果
print(msg)                 # "你好，小明"

# 逐行解释
# def是关键字，告诉Python“下面这块是个函数”
# name是形式参数（站位的标签，后面会讲到实参），调用时把“小明”传给name
# return把结果交给外面；如果没有return，函数返回None


# 2.练习，写一个函数is_even(n)返回n是否为偶数
def is_even(n):
    if n % 2 == 0:
        return f"{n}是偶数"
    else:
        return f"{n}不是偶数"

# 函数调用
test1 = is_even(4)
print(test1)        # "4是偶数"