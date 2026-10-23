# 装饰器就是在不改变函数的情况下，给函数添加上额外的附加功能
# 这里就要将闭包的知识运用上了

# 不带@的版本
def shout(fn):
    def wrapper():
        return fn().upper() + "!!!"
    return wrapper

def hello():
    return "hi"

hello = shout(hello)            # 将原来的hello替换为加了shout装饰器后的hello
print(hello())          # HI!!!

# 带@的版本
@shout
def hello():
    return "hi"
# @xxx写在def f 上一行，就是f = xxx(f)的简写

print(hello())          # HI!!!

# 我对装饰器的理解（根据以上的例子）
# shout就是装饰器，hello就是原函数。我们知道函数是可以作为参数的，
# hello将自己作为参数传入了shout，又自己接收了改变后的自己
# 所以 新hello = wrapper + 作为外层变量的旧hello