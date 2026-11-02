# 练习1：第 6 节）：惰性求值陷阱——预测输出
x = 10
g = (x * i for i in range(3))     # 生成器表达式
lst = [x * i for i in range(3)]   # 列表推导式

x = 100
print(list(g))      # [0, 100, 200]
print(lst)          # [0, 10, 20]
# 这里g是生成器，在第7行前g未做任何计算，在计算前x被赋上了新值
# 所以g生成器里的x为100，而lst在生成时就已经计算完了，lst已经
# 是一个不含x的列表了；但是注意：生成器里的元素是未计算的，
# 但是条件range(3)是已经算完了的

# 练习2：第 7 节：用 yield from 实现 flatten
# 用生成器函数实现 flatten(data)，把任意嵌套的列表完全拍平
def flatten(data):
    for item in data:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))          # [1, 2, 3, 4, 5]
print(list(flatten([[1, 2], [], [3, [4, [5]]]])))  # [1, 2, 3, 4, 5]

# 只用yield 和 for
def flatten1(data):
    for item in data:
        if isinstance(item, list):
            for i in flatten1(item):
                yield i
        else:
            yield item

print(list(flatten1([1, [2, [3, 4]], 5])))          # [1, 2, 3, 4, 5]
print(list(flatten1([[1, 2], [], [3, [4, [5]]]])))  # [1, 2, 3, 4, 5]

# 两版对比可知：yield from 省去了一层for循环，且第一种更不易出现变量名错误

# 练习3：（第 8 节）：写一个"实时平均值"协程
# 用协程实现 averager()：不断 send() 数字进去，
# 每次 send 都返回"当前已收数字的平均值"。
def averager():
    sum = 0
    count = 0
    avg = None
    while True:
        num = yield avg     # next会停在这
        if num is None:         
            break
        sum += num
        count += 1
        avg = sum / count

g = averager()
next(g)          # 启动
print(g.send(10))    # 10.0
print(g.send(20))    # 15.0
print(g.send(30))    # 20.0

# 练习4：第 8 节：预测输出——close() 和 throw()
# def echo():
#     while True:
#         msg = yield
#         print(f"收到：{msg}")

# g = echo()
# next(g)
# g.send("hi")
# g.close()
# g.send("bye")     # 异常StopIteration

def echo():
    while True:
        try:
            msg = yield
        except ValueError:
            print("忽略错误")
        else:
            print(f"收到：{msg}")

g = echo()
next(g)
g.send("hi")
g.throw(ValueError)
g.send("hello")     # 协程还存在，hello依旧会输出

