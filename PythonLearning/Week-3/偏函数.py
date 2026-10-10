# 偏函数是指固定函数得某些参数，生成一个新的函数，这样就无需在每次调用
# 函数时传递相同的参数，一般使用functools模块里的partial函数创建偏函数

import functools

int2 = functools.partial(int, base=2)       # 2进制转10进制函数
int8 = functools.partial(int, base=8)       # 8进制转10进制函数
int16 = functools.partial(int, base=16)       # 16进制转10进制函数

print(int("1001"))      # 1001
print(int2("1001"))     # 9
print(int8("1001"))     # 513
print(int16("1001"))        # 4097