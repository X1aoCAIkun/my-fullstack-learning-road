# range函数的仿写
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    cur = start
    while(step > 0 and cur < stop) or (step < 0 and cur > stop):
        yield cur
        cur += step

# enumerate函数的仿写（返回元素以及start开始的序号）
def my_enumerate(iterable, start=0):
    i = start
    for x in iterable:
        yield i, x
        i += 1

# zip函数的仿写（按小标将多个迭代对象配对分组）
def my_zip(*iterables):
    iters = [iter(it) for it in iterables]
    while True:
        result = []
        for it in iters:
            try:
                result.append(next(it))
            except StopIteration:
                return
        yield tuple(result)

# chain函数的仿写（串联多个迭代器）
def my_chain(*iterables):
    for it in iterables:
        yield  from it

print(list(my_range(5)))        # [0, 1, 2, 3, 4]
print(list(my_enumerate("abc", 1)))         # [(1, "a"), (2, "b"), (3, "c")]
print(list(my_zip([1, 2, 3], "abc", [10, 20, 30])))             # [(1, "a", 10), (2, "b", 20), (3, "c", 30)]
print(list(my_chain([1], (2, 3), "ab")))            # [1, 2, 3, "a", "b"]