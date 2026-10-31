"""
iterable(可迭代对象)；它可以“被for循环”的东西；比如：list/dict/str/file；
它的关键方法：__iter__()返回一个迭代器

iterator(迭代器)；真正“一个一个吐”的家伙；比如：iter([1, 2, 3])的返回值；
关键方法：__next__()每次吐一个
"""

nums = [1, 2, 3]        # nums就是iterable，而不是iterator
it = iter(nums)         # 调用iter()就会调用__iter__()返回一个迭代器
print(next(it))         # 1
print(next(it))         # 2
print(next(it))         # 3
# print(next(it))         # StopIteration

"""
所以可以知道：
for x in nums:
就可以转换为：
it = iter(nums)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
"""

# 练习：用 iter() 和 next() 模拟 for x in "abc": print(x)，不要用 for。 
it_str = iter("abc")
while True:
    try:
        x = next(it_str)
    except StopIteration:
        break
    print(x)