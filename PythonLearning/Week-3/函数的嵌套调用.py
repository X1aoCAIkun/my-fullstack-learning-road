# 下面这个函数可以做到输入任意多个参数，对其int和float类型数据的求和运算
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result

# 可以使用函数的嵌套，使上面这个函数可以实现任意二元运算
def new_calc(init_result, op_func, *args, **kwargs):
    """
    init_result:运算的初始值
    op_func:二元运算函数
    """
    items = list(args) + list(kwargs.values())
    result = init_result
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

# 定义这里的op_func
def add(x, y):
    return x + y
def mul(x, y):
    return x * y

# 对new_calc的调用
print(new_calc(0, add, 1, 2, 3, 4, 5))      # 15
print(new_calc(1, mul, 1, 2, 3, 4, 5))          # 120

# 当然op_func也可以使用模块中的函数,在其他时候学会使用内置函数会快得多
import operator
print(new_calc(0, operator.add, 1, 2, 3, 4, 5))     # 15
print(new_calc(1, operator.mul, 1, 2, 3, 4, 5))          # 120