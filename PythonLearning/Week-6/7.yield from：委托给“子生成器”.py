def chain(*iterables):
    for it in iterables:
        for x in it:
            yield x

# 等价写法（更快、更短、转发更彻底）
def chain2(*iterable):
    for it in iterable:
        yield from it

print(list(chain([1, 2], (3, 4), "ab")))        # [1, 2, 3, 4, "a". "b"]
print(list(chain2((5, 6), [7, 8], "cd")))       # [5, 6, 7 ,8, "c", "d"]

# 二者对比，yield from it 不仅可以省一层for，还会自动转发send/throw/close
# 写复杂协程时是必须的。（这里的协程知识后面会讲）