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

# 练习5：第 9 节：itertools 组合拳
# (a) 密码穷举：用 product 生成所有 4 位数字 PIN（0000~9999），
# 打印总数和前 5 个。然后回答：如果要求4 位数字互不重复，
# 该换哪个函数？总数是多少？
from itertools import product, permutations, groupby, accumulate, islice

PIN = ["".join(x) for x in product("0123456789", repeat=4)]
print(PIN[:5])
unique_PIN = ["".join(x) for x in permutations("0123456789", 4)]
print(len(unique_PIN))

# (b) 游程编码：用 groupby 把 "aaabbbcca" 压缩成 
# [('a', 3), ('b', 3), ('c', 2), ('a', 1)]。
# 注意 groupby 返回的 group 是一个迭代器
# 想一想 len(list(group)) 里为什么必须写 list()。
w = []
for k, words in groupby("aaabbbcca"):
    w.append((k, len(list(words))))
print(w)
# 必须些list()是因为words是一个迭代器，
# 而且groupby迭代完，它也迭代完

# (c) 阶乘累进：用 accumulate 一行算出 
# [1, 2, 6, 24, 120]（前 5 个阶乘），
# 提示：accumulate 的第二个参数可以传 lambda a, b: a * b。
n = [x for x in range(1, 6)]
print(list(accumulate(n, lambda a, b: a*b)))

# (d) 预测输出——islice 的消耗性：
it = iter(range(10))
print(list(islice(it, 3)))      # [0, 1, 2]
print(list(islice(it, 3)))      # [3, 4, 5] it是一个迭代器，它已经遍历到3了 


# 题 6（实战 1 风格）：手写 my_takewhile 和 my_cycle
# (a) 手写 my_takewhile(pred, it)：
# 只要 pred 为真就吐，第一次为假立即停。
def my_takewhile(pred, it):
    for item in it:
        if pred(item):
            yield item
        else:
            return
print(list(my_takewhile(lambda x: x < 3, [1, 2, 3, 4, 1])))   # [1, 2]

# (b) 手写 my_cycle(it)：无限循环吐出一个可迭代对象的所有元素。
# 测试（别真 list() 它，会卡死，用 islice 取前几个）：
def my_cycle(it):
    cache = []
    for item in it:
        cache.append(item)          # 边吐边存
        yield item
    if not cache:
        return
    while True:
        yield from cache
        
print(list(islice(my_cycle("AB"), 5)))          # ['A', 'B', 'A', 'B', 'A']
print(list(islice(my_cycle(iter([1, 2])), 5)))  # [1, 2, 1, 2, 1]  ← 注意传的是迭代器！

# 练习7：第 6 + 9 节综合：groupby 陷阱
# 预测输出，并解释 groupby 的分组规则：
for k, g in groupby([1, 1, 2, 2, 1, 1]):
    print(k, list(g))       # 1 [1, 1]  2 [2, 2]  1 [1, 1]