nums = [1, 2, 3, 4]

# map：对每个元素做处理（一般用于对数据流式处理）
print(list(map(lambda x: x * x, nums)))         # [1, 4. 9. 16]

# filter：过滤（同上）
print(list(filter(lambda x: x % 2 == 0, nums)))         # [2, 4]

# reduce：累计（统计）（一般用于聚合）
from functools import reduce
print(reduce(lambda a, b: a + b, nums))         # 10

# 但其实很多时候这些函数都可用推导式写（可读性更强）
# 对map()可以改为如下形式
print([x * x for x in nums])
# 对filter()函数可改为如下形式
print([x for x in nums if x % 2 == 0])
# 对reduce()函数则使用for循环
sum = 0
for x in nums:
    sum += x
print(sum)