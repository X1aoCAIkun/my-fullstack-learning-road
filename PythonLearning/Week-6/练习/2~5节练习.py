# 练习1：不用 for，只用 iter()、next()、while、try/except，
# 遍历字典 d = {"a": 1, "b": 2, "c": 3}，
# 打印出 a -> 1 这样的格式。
# 要求：必须显式捕获 StopIteration，代码里不能出现 for 关键字。

d = {"a": 1, "b": 2, "c": 3}
it = iter(d.items())

while True:
    try:
        key, value = next(it)
        print(f"{key} -> {value}")
    except StopIteration:
        break

# 练习2：把下面每个对象分类：
# 仅 iterable / 仅 iterator / 两者都是 / 两者都不是：
"""
[1, 2, 3]        "hello"         {"x": 1}
range(5)         iter([1, 2])    enumerate("ab")
reversed("ab")   zip([1], [2])   map(str, [1, 2])
5                3.14            open("某文件.txt")

第一行都只是iterable以及range(5)
第四行前两个都不是
其他都是二者都是

iter()一个迭代器返回的依然是它自己，因为__iter__返回的就是self
"""

# 练习3：预测输出——迭代器是"一次性"的
nums = iter([1, 2, 3, 4])
print(sum(nums))        # 10
print(sum(nums))        # 0
print(3 in nums)        # False
# 迭代器raise后就停在了raise这了，下次用就会继续raise，sum的初始值为0；
# in 会自动except StopIteration异常

# 练习4：预测输出——嵌套循环里的"共享迭代器"
it = iter([1, 2, 3, 4, 5])
for a in it:
    for b in it:
        print(a, b)     # 1 2，1 3，1 4，1 5
# 内层对it用了next()，内层已经将it耗尽所以a只有1

# 练习5：实现 ChunkIterator（自定义迭代器，进阶）
# 用类实现一个 Chunk 迭代器：把任意可迭代对象按固定大小切成块。
class Chunk:
    def __init__(self, iterable, step):
        if step <= 0:
            raise ValueError
        self.iterable = iter(iterable)
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        chunk = []
        count = 0
        while count < self.step:
            try:
                chunk.append(next(self.iterable))
            except StopIteration:
                break
            count += 1
        if not chunk:
            raise StopIteration
        return tuple(chunk)

print(list(Chunk("abcdef", 2)))    # [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(list(Chunk([1, 2, 3, 4, 5], 2)))  # [(1, 2), (3, 4), (5,)]
print(list(Chunk([], 3)))          # []

# 练习6：生成器函数的三个灵魂拷问
# (a) 用生成器函数实现 fibonacci(n)，
# 惰性地产出前 n 个斐波那契数（从 1, 1 开始）。
def fibonacci(n):
    count = 0
    num = []
    x = 0
    while n > 0:
        if count in (0, 1):
            x = 1
            num.append(x)
        else:
            x = num[count - 2] + num[count - 1]
            num.append(x)
        yield x
        n -= 1
        count += 1
print(list(fibonacci(6)))
# 更简洁的写法
# def fibonacci(n):
#     a, b = 1, 1
#     while n > 0:
#         yield a
#         a, b = b, a + b
#         n -= 1
# (b) 预测输出——yield 之后还有代码：
def countdown(n):
    print("start")
    while n > 0:
        yield n
        n -= 1
    print("end")

g = countdown(2)
print(next(g))      # 2
print(next(g))      # 1
# print(next(g))   # end StopIteration
# (c) 基于 (a) 回答：
g = fibonacci(5)
print(list(g))      # [1, 1, 2, 3, 5]
print(list(g))      # []，g迭代器耗尽了，list接住了异常返回了[]

# 练习7：实现 SlidingWindow（滑动窗口迭代器）
# 用类实现一个 SlidingWindow 迭代器：
# 窗口大小固定为 n，每次滑动 1 格，产出连续的"窗口元组"。
class SlidingWindow:
    def __init__(self, iterable, size):
        self.iterable = iter(iterable)
        self.l = len(iterable) 
        self.size = size
        if size < 0:
            raise ValueError
        self.Nums = []
        self.stop = len(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        count = 0
        while count < self.size:
            if self.l < self.size:
                self.stop = 0
                break
            if len(self.Nums) < self.size:
                try:
                    self.Nums.append(next(self.iterable))
                except StopIteration:
                    break
                count += 1
                self.stop -= 1
            else:
                try:
                    self.Nums[:self.size - 1] = self.Nums[1:self.size]
                    self.Nums[-1] = next(self.iterable)
                except StopIteration:
                    break
                count = self.size
                self.stop -= 1
        if self.stop == 0 and count == 0:
            raise StopIteration
        return tuple(self.Nums)

print(list(SlidingWindow("abcdef", 3)))
# [('a', 'b', 'c'), ('b', 'c', 'd'), ('c', 'd', 'e'), ('d', 'e', 'f')]

print(list(SlidingWindow([1, 2, 3, 4], 2)))
# [(1, 2), (2, 3), (3, 4)]

print(list(SlidingWindow("abc", 5)))   # 窗口比数据还长
# []

print(list(SlidingWindow([], 3)))      # 空输入
# []

print(list(SlidingWindow("abc", 1)))  # n = 1
# [('a',), ('b',), ('c',)]   


# 第七题改良版，只依赖StopIteration，且支持任意迭代器
class New_SlidingWindow:
    def __init__(self, iterable, size):
        if size <= 0:
            raise ValueError("size必须大于0")
        self.it = iter(iterable)
        self.size = size
        self.buf = None         # 当前窗口 初始为None
    def __iter__(self):
        return self
    def __next__(self):
        # 第一个窗口初始化
        if self.buf == None:
            temp =[]
            count = 0
            while count < self.size:
                try:
                    temp.append(next(self.it))
                except StopIteration:
                    break
                count += 1
            if len(temp) < self.size:
                raise StopIteration     # 连第一个窗口都未满
            self.buf = temp         # 存入历史记录
        else:
            try:
                new = next(self.it)
            except StopIteration:
                raise StopIteration     # 所有元素遍历完了
            self.buf = self.buf[1:] + [new]
        return tuple(self.buf)

print(list(New_SlidingWindow("abcdef", 3)))
# [('a', 'b', 'c'), ('b', 'c', 'd'), ('c', 'd', 'e'), ('d', 'e', 'f')]

print(list(New_SlidingWindow([1, 2, 3, 4], 2)))
# [(1, 2), (2, 3), (3, 4)]

print(list(New_SlidingWindow("abc", 5)))   # 窗口比数据还长
# []

print(list(New_SlidingWindow([], 3)))      # 空输入
# []

print(list(New_SlidingWindow("abc", 1)))  # n = 1
# [('a',), ('b',), ('c',)]   