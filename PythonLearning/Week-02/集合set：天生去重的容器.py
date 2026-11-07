# 集合就像一个没有重复客人的会员名单--同一个人加入最多算一次
# 其实集合就像特殊去重的列表，集合是无序的（因此没有下标）
# 但是又可变（意味着集合可修改）
# 同样，其他容器的一些用法（推导式等）set也可以使用
# 需要注意的是，set中的元素类型必须是hashable(哈希类型)，通常不可变类型是哈希类型

# 1.定义
# 直接定义'{}'标识，集合中至少要有一个元素否则python会认定它是一个字典
a = {1, 2, 3, 4, 4}
print(a)        # {1, 2, 3, 4} 会自动去重
b = {3, 4, 5, 6}
# 通过set()转换
nums1 = [1,1,2,3,4,5,5]
unique = set(nums1)
print(unique)           # {1, 2, 3, 4, 5}


# 2.集合的二元运算
# set的二元运算也可以和"="结合使用，这里就不展示了
print(a | b)
print(a.union(b))         
# {1, 2, 3, 4, 5, 6} 并集
print(a & b)            
print(a.intersection(b)) 
# {3, 4} 交集
print(a - b)            
print(a.difference(b))
# {1, 2} 差集
print(a ^ b)          
print(a.symmetric_difference(b))
# {1, 2, 5, 6} 对称集（并集减去交集）


# 3.增删
a.add(10)           
a.discard(1)            # 不存在对应元素不会报错
a.remove(2)             # 不存在会报错


# 4.frozenset：不可变集合(意味着可以作为字典的键)
fs = frozenset({1, 2,3})


# 5.集合的遍历（for-in）
for elem in a:
    print(elem)             # 输出结果不定，因为set是无序的