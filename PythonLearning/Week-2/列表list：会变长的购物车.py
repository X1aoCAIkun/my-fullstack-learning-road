# 列表是一种特别的数据容器，它就像一个购物车，其中的元素就像购物车中的商品
# 可以进行往列表里增加元素等操作
# 同时，列表和数组一样，其中的元素都是有序的，都有一个唯一与之对应的下标
# 第一个元素的下标为0 ，最后一个元素下标为列表长度-1


# 1.列表的创建于索引
# 形式：列表名（像一种特殊的变量名） = [元素, 元素~~~~]
# 这里的元素可以是任意类型，甚至可以是列表
fruits_1 = ["苹果", "香蕉", "橘子"]
# 根据下标查找元素
print(fruits_1[0])        # "苹果"    
print(fruits_1[-1])        # "橘子" -1表示最后一个元素
print(len(fruits_1))        # 3，len()可以得出列表的长度（即列表中元素的个数）


# 2.切片（同字符串切片一样）,切片出来依然是一个列表
nums_1 = [10, 20, 30, 40, 50]
print(nums_1[1:4])        # [20, 30, 40]，输出下标1~4的元素，步长为1
print(nums_1[::-1])       # [50, 40, 30, 20, 10]，反向输出列表


# 3.对列表进行增删改查（要熟练使用这些Python这些内置的列表方法）
fruits_2 = ["苹果", "香蕉"]

# 3.1增操作
fruits_2.append("橘子")         # ["苹果", "香蕉", "橘子"]，append()是在列表末尾增加()里的元素,注意：一次只能追加一个元素
fruits_2.insert(1, "葡萄")          # ["苹果", "葡萄"，"香蕉", "橘子"]，insert(下标, 元素)是在列表的某下标处插入指定元素 
fruits_2.extend(["梨子", "桃子"])           # ["苹果", "葡萄"，"香蕉", "橘子", "梨子", "桃子"]，extend()可以末尾追加多个元素，它会将()里的元素拆开一个一个追加道列表中

# 3.2删操作
fruits_2.remove("香蕉")         # ["苹果", "葡萄"，"橘子", "梨子", "桃子"]，remove()可以指定删除列表中第一个匹配的元素，记住有多个匹配也只删第一个匹配的，注意当删除不在列表中的元素会报错
last = fruits_2.pop()           # ["苹果", "葡萄"，"橘子", "梨子"]，pop()会弹出列表指定位置元素（默认最后一个），这个元素会被移出列表且可以被一个变量接收
del fruits_2[0]             # ["葡萄"，"橘子", "梨子"]，del会删除指定下标的元素，记住del要写在列表名前隔一个空格
# fruits_2.clear()      会清空列表中的所有元素

# 3.3改操作
fruits_2[0] = "西瓜"        # ["西瓜"，"橘子", "梨子"]，直接根据下标赋值一个元素进行修改
fruits_2[1:3] = ["哈密瓜", "橙子"]      # ["哈密瓜", "橙子", "梨子"]，也可以使用切片的方式进行修改

# 3.4查操作
print("西瓜" in fruits_2)       # True ，in会遍历整个列表查找是否有匹配的元素，并返回一个bool值
print(fruits_2.index("梨子"))           # 2，index()会返回第一个匹配元素的下标
print(fruits_2.count("梨子"))           # 1，count()会返回查找元素在列表中出现的次数


# 4.列表推导式（重要，Pythonic利器）
# 需要注意的是列表推导式 = [表达式 for in 可迭代对象 if 条件]，比for循环更短更快
# 说白了就是直接将对列表的操作表达式写在[]内，这样更简洁，接下来对比一下
# 普通写法
squares = []        # 定义列表
for i in range(1, 6):       # 循环添加元素
    squares.append(i * i)      
# 推导式写法
squares = [i * i for i in range(1, 6)]          # 一行搞定，前面写要添加的元素，后面写推导式
print(squares)      # [1, 4, 9, 16, 25]
# 带筛选
evens = [i for i in range(20) if i % 2 == 0]        # 先筛选0~19中2的倍数给i，再给需要待添加的元素i加入列表
print(evens)        # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# 双层循环
paris = [(x, y) for x in [1, 2] for y in [3, 4]]        # 就像正常的双重循环一样执行
print(paris)        # [(1, 3), (1, 4), (2, 3), (2, 4)]


# 练习
# 给定nums_2 = [3, 1, 4, 1, 5, 9, 2, 6]，用一行代码：
nums_2 = [3, 1, 4, 1, 5, 9, 2, 6]
# 1.取出所有偶数
nums_3 = [i for i in nums_2 if i % 2 == 0]
print(nums_3)       # [4, 2, 6]
# 2.把每个数字平方
nums_4 = [i ** 2 for i in nums_2 ]
print(nums_4)       # [9, 1, 16, 1, 25, 81, 4, 36]


# 5.列表的运算
# 5.1可以使用“+”来拼接列表
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

# 5.2可以使用“*”来实现列表的重复自拼接
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

# 5.3列表也可以使用关系运算
items8 = [1, 2, 3, 4]
items9 = list(range(1, 5))
items10 = [3, 2, 1]
print(items8 == items9)     # True
print(items8 != items9)     # False
print(items8 <= items10)    # True，比较的是第一个元素的大小
print(items9 >= items10)    # False，比较的是第一个元素的大小


# 6.列表的遍历
# 方法一：在循环结构中通过索引运算，遍历列表元素。
languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])
# 方法二：直接对列表做循环，循环变量就是列表元素的代表。
languages = ['Python', 'Java', 'C++', 'Kotlin']
for language in languages:
    print(language)


# 7.元素排序和反转
# 列表的sort操作可以实现列表元素的排序，而reverse操作可以实现元素的反转
# 原地排序和反转，返回值为None
items11 = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items11.sort()
print(items11)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items11.reverse()
print(items11)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']