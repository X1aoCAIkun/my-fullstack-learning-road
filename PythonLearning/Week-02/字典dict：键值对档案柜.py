# 字典dict就好像一本字典书--通过“词条”（键值）查“释义”（元素值），查找速度极快
# 其实好像tuple的namedtuple功能一样，只不过dict将它常态化了
# dict也是有序的（这个一般不提）、可变的、可重复的（指的时元素值可重复，但是键值不可重复）
# dict的每个元素值于键值绑定，所以索引方式是键值
# dict的键值一定要为不可变类型（字典、元组、字符串等），元素可以为任意类型


# 1.dict的一般用法
# 定义方式：字典名 = {"键值": 元素值, ~~~~}
person1 = {"name": "李雷", "age": 18, "city": "北京"}
# 也可以用dict()方法创建
person3 = dict(name = "张三", age = 20, city = "上海")
# 可以通过Python内置函数zip压缩两个序列并创建字典（不常用）
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
# 通过键值查找元素
print(person1["name"])           # 李雷
#通过键值修改元素值
person1["city"] = 19
# 当输入一个新的键值时，会与元素值作为一个新键值对加入dict
person1["job"] = "学生"         
# 删除键值对也通过键值，键值不存在也会报错的
del person1["city"]
# 也有pop()\popitem()\clear()方法，同上
person5 = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person5.pop('age'))  # 25
print(person5)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person5.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person5)             # {'name': '王大锤', 'height': 178}
person5.clear()
print(person5)             # {}
# 也可以用成员运算
print("name" in person1)         # True


# 2.安全的查找：get/setdefault
score = {"小明": 90}

# print(score["小红"])            # KeyError报错，键值不存在

# 为了避免查找到一个不存在的键值产生报错，所以在查找dict时要使用get/setdefault方法
# get("键值"， 默认值（可选）)
print(score.get("小红"))            # None，键值不存在且无规定默认值
print(score.get("小红", 0))         # 0
# setdefault：没有就设上，有就返回
# setdefault("键值", 默认值（不写就为None）)
# key存在时
res1 = score.setdefault("小明", 98)
print(res1)          # 90
print(score)        # {"小明": "90"}字典不会被改变
# key不存在时
res2 = score.setdefault("小红", 100)
print(res2)         # 100
print(score)        # {"小明": "90", "小红", 100}


# 3.对dict的遍历
person2 = {"name": "李雷", "age": 18}

for key in person2:             # 默认遍历字典是遍历键值
    print(key)              # name, age

for key, value in person2.items():          # items()会将键值对的值赋给key和value
    print(key, "=", value)          # name = 李雷， age = 18


print(list(person2.keys()))         # ['name', 'age'] keys()方法会查询所有的键值
print(list(person2.values()))       # ['李雷', 18] values()方法会查询所有的元素值


# 4. 字典的推导式，和列表大致相同，只是赋的值要是一个键值对（x: y）
nums1 = [1, 2, 3, 4]
square_map = {n: n*n for n in nums1}
print(square_map)           # {1: 1, 2: 4, 3: 9, 4: 16}


# 练习统计句子 "the quick brown fox jumps over the lazy dog the end" 里每个单词出现的次数。
sentence = "the quick brown fox jumps over the lazy dog the end"
dict1 = {}
for word in sentence.split():
    dict1[word] = dict1.setdefault(word, 0) + 1
print(dict1)
# 再统计一下这句话中每个字母出现的次数
dict2 = {}
for letter in sentence:
    if "A" <= letter <= "Z" or "a" <= letter <= "z":
        dict2[letter] = dict2.get(letter, 0) + 1
print(dict2)


# 字典内容补充
# 字典的update()方法可以将两个列表合并起来，且只会将被添加dict在添加dict中没有的键值对进行添加
# update()方法也可以等效与 person3 |= person4
person3 = {'name': '王大锤', 'age': 55, 'height': 178}
person4 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person3.update(person4)
print(person3)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}