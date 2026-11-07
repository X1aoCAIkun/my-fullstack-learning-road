# 1. for循环的展开
class Box:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        print("iter")
        return iter(self._data)

b = Box([1, 2])
for x in b:
    print("x =", x)
for y in b:
    print("y =", y)
# 写出完整输出（不运行）。
# 答：iter x = 1 x = 2    iter y = 1 y = 2
# 两次 for 一共调用了几次 __iter__？
# 答：两次
# 底层迭代器的 __next__ 一共被调用了几次（包括最后引发 StopIteration 的那两次）？
# 答：6次
# 把第一个 for 改写成等价的 while + try/except，代码里不能出现 for。
it = iter(b)
while True:
    try:
        new = next(it)
    except StopIteration:
        break
    print("x =", new)
# 一句话回答：for 为什么能“自动停下来”，不需要你写 try？
# 答：for会自动处理StopIteration，然后结束循环

# 2. 可迭代对象 VS 迭代器
class A:
    def __iter__(self):
        return [1, 2, 3]

class B:
    def __iter__(self):
        return iter([1, 2, 3])

class C:
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration

# 分别写出下面几行的结果（值或异常）：
# for x in A(): print(x)
# for x in B(): print(x)
# list(C())
# iter(B()) is iter(B())
# 答：TypeError    1 2 3     []    False（每回iter都会创建一个新的迭代器）
# 解释 A 为什么不行：__iter__ 返回 [1, 2, 3] 和返回 iter([1, 2, 3]) 差在哪？
# 答：因为A返回的是一个列表并非迭代器，for无法执行,for需要一个迭代器
# 写一个函数 describe(obj)，不借助 isinstance，
# 只靠 iter() 判断并返回：
# "iterator"（自己就是迭代器）
# "iterable"（只能产生迭代器）
# "neither"（连 iter() 都不支持）
def describe(obj):
    try:
        it = iter(obj)
    except TypeError:
        return "neither"
    if it is obj:
        return "iterator"
    return "iterable"

print(describe(iter([1, 2])))   # "iterator"
print(describe([1, 2]))       # "iterable"
print(describe("ab"))       # "iterable"
print(describe(range(3)))       # "iterable"
print(describe(5))       # "neither"

# 3. 自己造一个迭代器
# 和 zip 反过来：实现一个 最长配对 迭代器 ZipLongest，
# 短的序列用 fillvalue 补，所有来源都耗尽才结束。
# 要求：
# 用类实现，不是生成器
# 构造签名：ZipLongest(*iterables, fillvalue=None)
# __iter__ 返回 self，__next__ 返回一个元组
# 如果某一行所有来源都已经耗尽，不要产出全 fillvalue 的行，直接 StopIteration
# 每个来源是否耗尽只能判断一次，不能每行都重复计数
class ZipLongest:
    def __init__(self, *iterables, fillvalue=None):
        self.iters = [iter(it) for it in iterables]
        self.fillvalue = fillvalue
        # 每个可迭代对象的耗尽标志
        self.done = [False] * len(self.iters)
    def __iter__(self):
        return self
    def __next__(self):
        if all(self.done):
            raise StopIteration
        temp = []
        got_any = False
        for index, it in enumerate(self.iters):
            if self.done[index]:
                temp.append(self.fillvalue)
            else:
                try:
                    val = next(it)
                    temp.append(val)
                    got_any = True
                except StopIteration:
                    temp.append(self.fillvalue)
                    self.done[index] = True
        if not got_any:
            raise StopIteration
        return tuple(temp)

print(list(ZipLongest([1, 2], "ab", [10])))
# [(1, 'a', 10), (2, 'b', None)]
print(list(ZipLongest([], [1])))
# [(None, 1)]
print(list(ZipLongest([1], [2], fillvalue=0)))
# [(1, 2)]
print(list(ZipLongest()))
# []

# 4. 生成器函数
# 写一个生成器 running_max(iterable)：
# 每读到一个元素，就产出“到目前为止的最大值”。
def running_max(iterable):
    it = iter(iterable)
    try:
         cur = next(it)
    except StopIteration:
        return          # 空输入时不返回值
    yield cur
    for i in it:
        cur = max(cur, i)
        yield cur
print(list(running_max([3, 1, 4, 1, 5, 9, 2, 6])))
# [3, 3, 4, 4, 5, 9, 9, 9]
print(list(running_max([])))    # []
print(list(running_max([5])))   # [5]
# 再预测下面代码的输出（不运行），并说明它体现了生成器的什么特性：
# 体现了生成器的按需拉取
def noisy():
    for x in [3, 1, 4]:
        print("produce", x)
        yield x

g = running_max(noisy())
print(next(g))
print(next(g))
# 最后回答：调用 running_max(noisy()) 的那一瞬间，
# noisy 里的 print 会执行吗？为什么？
# 不会，因为生成器函数调用时只创建生成器对象

# 5. 生成器表达式
numbers = [5, -3, 12, 8]
num_gen = (x for x in numbers)
print(sum(num_gen))

# 6. yield from
def echo():
    while True:
        msg = yield
        print(f"收到：{msg}")

def via_for():
    for x in echo():
        yield x

def via_yf():
    yield from echo()

g1 = via_for(); next(g1); g1.send("hi")         # 收到：None
g2 = via_yf();  next(g2); g2.send("hi")         # 收到：hi

# 7. 协程 send/throw/close
# 写一个协程 max_tracker()：
# next(g) 预激，返回 None
# g.send(x) 返回“截至目前的最大值”
# g.throw(ValueError) 表示重置：清空当前最大值，
# 协程继续存活，并返回 None
# 其他异常类型不捕获，直接让协程退出
def max_tracker():
    m = None
    while True:
        try:
            cur = yield m
        except ValueError:
            m = None
            continue
        if m is None or cur > m:
            m = cur 
g = max_tracker()
print(next(g))              # None
print(g.send(3))            # 3
print(g.send(1))            # 3
print(g.send(7))            # 7
print(g.throw(ValueError))  # None，重置
print(g.send(2))            # 2

# 8. itertools 排班
staff = ["A", "B", "C", "D"]
# 用 cycle + islice 生成 7 天值班名单 → 
# ['A', 'B', 'C', 'D', 'A', 'B', 'C']
from itertools import cycle, islice, combinations, groupby
print(list(islice(cycle(staff), 7)))
# 用 combinations(staff, 2) 列出所有两人的搭档组合 → 
# 共 6 组，按顺序写出前 3 组
c = list(combinations(staff, 2))
print(c)
print(c[:3])
# 用 groupby 统计每人值了几天（提示：先 sorted）→ 
# A:2, B:2, C:2, D:1
# groupby函数的第二个返回值是临时迭代器
g = list(islice(cycle(staff),7))
result = {person: sum(1 for _ in days)
          for person, days in groupby(sorted(g))}
print(result)
# {'A': 2, 'B': 2, 'C': 2, 'D': 1}
# 回答：cycle 为什么既能接收 list，
# 也能接收一次性生成器并重复输出？它内部做了什么？
# 因为它内部做了缓存