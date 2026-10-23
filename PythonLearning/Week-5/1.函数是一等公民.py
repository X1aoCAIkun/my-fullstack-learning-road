# Python中的函数就是一个普通对象，可以装进变量、可以当参数
# 可以当返回值
# 注意： 这个能力是装饰器的基础。不带()的是传递函数本省、带()的是调用并取结果

# 装进变量
def hello():
    return "hi"

f = hello       # f相当于接收了函数的地址，hello有了别名，这里不用()
print(f())      # hi


# 当作参数
def call(fn):
    return fn()

print(call(f))        # hi  call的fn接收了hello的地址


# 当作返回值

# 写法一
# def inner():
#     return "from inner"
# def factory():
#     return inner
# 写法二
def factory():
    def inner():
        return "from inner"
    return inner

g = factory()       # 这里g是接收了inner函数的地址
print(g())          # from inner 