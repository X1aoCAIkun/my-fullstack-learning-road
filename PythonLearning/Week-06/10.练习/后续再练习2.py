# 题目1：手动拆掉 for
for ch in "Python":
    print(ch, end=" ")
print()     # 换行
# 用 iter() + while True + next() + try/except StopIteration 改写这段代码，代码里不能出现 for。
words = iter("Python")
while True:
    try:
        w = next(words)
    except StopIteration:
        break
    print(w, end=" ")
print()    # 换行 
# 回答：这段循环里 next() 一共被调用了多少次（包括最后抛异常的那次）？
# 7次
# 回答：for k in {"a": 1, "b": 2}: print(k) 打印的是什么？
# "a" "b"
# 预期输出： P y t h o n，共 6 行。想一想： for 循环凭什么知道“该停了”，而不是一直问下去？
# 它会捕捉到StopIteration异常，然后结束

# 题目2：一次性和可重复
# 实现下面两个类，让注释里的行为成立：
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __iter__(self):
        return iter(self.songs)

class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        cur = self.n
        self.n -= 1
        return cur

p = Playlist(["s1", "s2"])
print(list(p))          # ['s1', 's2']
print(list(p))          # ['s1', 's2']   第二次还能用

c = Countdown(3)
print(list(c))          # [3, 2, 1]
print(list(c))          # []            第二次空了
# 再回答：
# iter(p) is iter(p) 是 True 还是 False？
# False
# iter(c) is c 是 True 还是 False？
# True
# Playlist 是迭代器吗？Countdown 是可迭代对象吗？
# 不是（因为没有__next__）；是
# 想一想： 为什么一个类只要 __iter__ 返回 self，就必须自己维护“走到哪了”的状态？
# 因为 __iter__ 返回 self 后，next() 每次操作的都是同一个对象，没有独立的游标对象替它记位置。
# 如果不把进度存在属性里（比如 self.n），下一次 next() 就不知道从哪继续，只能从头再来。迭代器的本质就是“有状态的游标”。

# 题目3：斐波那契迭代器
# 写一个类 Fib(limit)，用迭代器协议逐个产出小于 limit 的斐波那契数（从 1, 1 开始）。要求：
# 实现 __iter__ 和 __next__
# 内部只保存两个变量表示当前的两个数，不能建列表
# 超过范围时 raise StopIteration
class Fib:
    def __init__(self, limit):
        self.limit = limit
        self.num1 = 1
        self.num2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num1 >= self.limit:
            raise StopIteration
        cur = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        return cur
        

print(list(Fib(20)))    # [1, 1, 2, 3, 5, 8, 13]
print(list(Fib(1)))     # []
print(list(Fib(2)))     # [1, 1]
# 再回答：
# f = Fib(20)，list(f) 之后再 list(f)，结果是什么？为什么？
# [] ; f这个迭代器走完了
# 想一想： 每次 next() 只前进一小步、从不回头，这个特性对“无限序列”意味着什么？
# 意味着可以按需取值且内存恒定

# 题目4：分块器写生成器函数 
# chunks(iterable, size)，把任意可迭代对象按 size 个一组切出来，最后一组可以不足。
# 要求：
# 只用 yield，不要先 list(iterable) 再切
# 传进来的是一次性生成器时也要能正常工作
def chunks(iterable, size):
    if size <= 0:
        raise ValueError("size不能为0")
    it = iter(iterable)
    while True:
        temp = []
        for _ in range(size):
            try:
                new = next(it)
            except StopIteration:
                break
            temp.append(new)
        if not temp:
            return
        yield temp
        if len(temp) < size:
            return

print(list(chunks("abcdefg", 3)))
# [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]
print(list(chunks("123456", 2)))        # [["1", "2"], ["3", "4"], ["5", "6"]]
print(list(chunks([], 2)))          # []

g = chunks((i * i for i in range(7)), 3)   # 输入也可以是生成器
print(next(g))                      # [0, 1, 4]
print(next(g))                      # [9, 16, 25]
print(next(g))                      # [36]
# 回答：调用 chunks([], 2) 的那一瞬间，函数体执行了吗？为什么？
# 没执行，它已经是生成器函数。调用它只创建生成器对象，函数体要等到第一次 next() 才执行。
# 想一想： 生成器暂停时，buf 里已经攒到一半的数据去哪了？
# 生成器暂停在 yield 时，它的整个栈帧被冻结保存，局部变量 temp、it 和当前执行位置都还活着，并没有被释放。
# 下一次 next() 会接着从那行往下执行；只有生成器被 close()、抛异常退出或被垃圾回收时，这些数据才会释放。

# 题目5：一进一出，不许建表
nums = [5, -3, 12, 8, -1, 20, 7]
# 用一行生成器表达式求所有正数的平方和。
# 用生成器表达式 + next() 求第一个大于 10 的数。
# 写函数 sum_of(iterable, pred)，用生成器表达式返回满足 pred 的元素之和。
print(sum(x ** 2 for x in nums if x > 0))                # 682

nums_gen = (x for x in nums if x > 10)
print(next(nums_gen))                              # 12

def sum_of(iterable, pred):
    return sum(x for x in iterable if pred(x))   
print(sum_of(nums, lambda x: x > 0))    # 52

g = (x * x for x in nums)
print(sum(g))
print(sum(g))
# 想一想： 第 4 题第二次为什么是 0？这和“生成器表达式不是列表”有什么关系？
# 因为g这个生成器的"游标"已经在第一次输出走完了，生成器是一次性的，列表是可重复使用的

# 题目6：拍平一切
# 写 flatten(items)，递归拍平任意层嵌套的 list / tuple，用 yield from 委托给递归调用
def flatten(items):
    for it in items:
        if isinstance(it, (list, tuple)):
            yield from flatten(it)
        else:
            yield it
print(list(flatten([1, [2, [3, 4]], 5])))
# [1, 2, 3, 4, 5]
print(list(flatten([])))                # []
print(list(flatten(["ab", ["cd", "ef"]])))
# ['ab', 'cd', 'ef']   注意：字符串不拆
# 写 chain_all(*iterables)，把所有来源依次串起来，只能用一层循环 + yield from。
def chain_all(*iterables):
    for it in iterables:
        yield from it

print(list(chain_all([1, 2], (3, 4), "ab")))
# [1, 2, 3, 4, 'a', 'b']
# 想一想： yield from x 和 for i in x: yield i 结果一样，那 yield from 多做了什么？
# 多做了send()和close()以及throw()

# 题目7：滑动平均计算器
# 写协程 running_average()：
# next(g) 预激，返回 None
# g.send(x) 返回“截至目前所有已发送数字的平均值”
# g.throw(ValueError) 表示重置：清空累计值和计数，协程继续存活，返回 None
# 其他异常不捕获，让协程退出
def running_average():
    sum = 0
    count = 0
    avg = None
    while True:
        try:
            num = yield avg
            sum += num
            count += 1
            avg = sum / count
        except ValueError:
            sum = 0
            avg = None
            count = 0
        

g = running_average()
print(next(g))            # None
print(g.send(10))         # 10.0
print(g.send(20))         # 15.0
print(g.send(30))         # 20.0
print(g.throw(ValueError))# None（重置）
print(g.send(8))          # 8.0
print(g.send(12))         # 10.0

g.close()
try:
    print(g.send(1))
except StopIteration:          # StopIteration
    print("协程已关闭")
# 想一想： send() 送进去的值，是被哪一行代码“接住”的？throw() 之后为什么协程没有死？
# num = yield avg中的num；没死，异常也会到 num = yield avg

# 题目8：排班小工具
staff = ["A", "B", "C", "D", "E"]
# 只用 itertools（cycle、islice、combinations、groupby、accumulate、product）完成：
# 从 C 开始，排 7 天值班表。
# 列出所有两人搭档组合，共几组？写出前 3 组。共10组
# 统计 7 天里每人值了几天。
# 已知每天工作量 [3, 1, 4, 1, 5]，求累计工作量。
# 用 product 生成两位密码（字母 A、B），列出全部。
from itertools import cycle, islice, combinations, groupby, accumulate, product
print(list(islice(cycle(staff), 2, 9)))         # ['C', 'D', 'E', 'A', 'B', 'C', 'D']
print(list(islice(combinations(staff, 2), 3)))      # [('A', 'B'), ('A', 'C'), ('A', 'D')]

work_staff = [x for x in islice(cycle(staff), 2, 9)]
temp = {key: len(list(value)) for key, value in groupby(sorted(work_staff))}
print(temp)
work_time = [3, 1, 4, 1, 5]
print(list(accumulate(work_time)))
print(["".join(x) for x in product("AB", repeat=2)])
# 想一想： 第 3 题为什么必须先排序？如果不排序，groupby 会把同一个人的记录分成几组？
# groupby是相邻元素分组，不排序7天就有7个分组，把同一个人的记录分成两组