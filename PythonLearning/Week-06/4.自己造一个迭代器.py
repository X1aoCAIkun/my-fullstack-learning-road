# 迭代器协议只要求两件事：
# 1. 有__iter__方法，返回self(迭代器自己)
# 2. 有__next__方法，每次返回下一个值，没了就raise StopIteration

class Countdown:
    """从 n 倒数到 1 的迭代器"""
    def __init__(self, n: int):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        cur = self.n
        self.n -= 1
        return cur

for x in Countdown(3):
    print(x)


# 练习：写一个 MyRange(start, stop, step=1)，模仿 range。
class MyRange:
    def __init__(self, start, stop, step=1):
        self.cur = start        # 不污染原始start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # step为正，超过或等于stop就停
        # step为负，小于或等于stop就停
        if (self.step > 0 and self.cur >= self.stop) or (self.step < 0 and self.cur <= self.stop):
            raise StopIteration
        tmp = self.cur
        self.cur += self.step
        return tmp

print(list(MyRange(0, 10, 2)))