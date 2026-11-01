# itertools 中全是迭代器工具，一个比一个好用
"""
函数	                            作用	                例子	                        输出
chain(a, b, ...)	                串联多个可迭代	        chain([1,2],[3,4])	            1 2 3 4
islice(it, start, stop, step)	    切片迭代器	            islice(count(), 5, 10)	        5 6 7 8 9
groupby(it, key)	                按 key 分组（先排序！）	 groupby("aaabbc")	            ('a', aaa) ('b', bb) ('c', c)
product(a, b)	                    笛卡尔积	            product("AB", [1,2])	        A1 A2 B1 B2
combinations(it, r)	                组合	                combinations("ABC", 2)	        AB AC BC
permutations(it, r)	                排列	                permutations("AB", 2)	        AB BA
accumulate(it, func)	            累计	                accumulate([1,2,3,4])	        1 3 6 10
cycle(it)	                        无限循环	            cycle("AB")	                    A B A B …
takewhile(pred, it)	                满足条件就取	        takewhile(<5, count())	        0 1 2 3 4
dropwhile(pred, it)	                满足条件就丢	        dropwhile(<3, [1,2,3,4,1])      3 4 1
"""


from itertools import chain, islice, groupby, product, accumulate


print(list((chain([1, 2], [3, 4]))))        # [1, 2, 3, 4]
print(list(islice(range(100), 5)))          # [0, 1, 2, 3, 4]
print(list(accumulate([1, 2, 3, 4])))       # [1, 3, 7, 11]
print(list(product("AB", [1, 2])))          # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
words = ["apple", "ant", "bee", "bat", "cat"]
words.sort(key=lambda w: w[0])          # groupby 前必须先排序
for k, group in groupby(words, key=lambda w: w[0]):
    print(k, list(group))

# 练习：用 itertools.product 生成"3 位 0-9 数字"的所有密码，共 1000 个。
codes = ["".join(c) for c in product("01", repeat=3)]
# for c in codes:     # join不是原地替换，而是生成一个新元素
#     "".join(c)
print(len(codes), codes[:5])