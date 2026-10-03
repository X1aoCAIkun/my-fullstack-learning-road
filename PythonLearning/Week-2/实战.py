# 实战1：词频统计升级版（使用正则）
import re
from collections import Counter

text1 = """
Python is great Python is easy Python is fun
We  love Python because Python makes life easy
"""

words = re. findall(r"\w+", text1.lower())           # 全部小写并提取
counter = Counter(words)        # 统计列表中每个元素出现的次数
print(counter.most_common(3))           # [('Python', 4), ('is', 3), ('easy', 3)] 返回频率最高的前三个词


# 实战2：学生成绩管理
students = []        # 学生成绩列表

def add_student(name, math, english):
    students.append({"name": name, "math": math, "english": english})

add_student("小明", 90, 85)
add_student("小红", 78, 92)
add_student("小刚", 65, 70)

# 平均分
for s in students:
    s["avg"] = (s["math"] + s["english"]) / 2

# 按平均分你排序
students.sort(key=lambda s: s["avg"], reverse=True)

for s in students:
    print(f"{s["name"]:>4}  数学{s['math']}   英语{s["english"]}    平均{s["avg"]:.1f}")


# 实战3：ASCII词云
from collections import Counter

text2= "apple banana apple orange banana apple apple orange grape"
counter = Counter(text2.split())

for word, n in counter.most_common():
    print(f"{word:<8} {'#' * n}  ({n})")


# 实战4：给定一个简单列表，对元素进行排序
# 简单列表：元素类型不是符合类型（列表/元组/字典）
# 示例：[3, 1, 4, 1, 5, 9, 2, 6, 5]
list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# 升序排序
print(sorted(list1))        # [1, 1, 2, 3, 4, 5, 5, 6, 9]
# 降序排序
print(sorted(list1, reverse=True))        # [9, 6, 5, 5, 4, 3, 2, 1, 1]


# 实战5：给定一个学生信息列表，根据学生的成绩进行排序
students = [
    {"name": "小明", "math": 90},
    {"name": "小红", "math": 78},
    {"name": "小刚", "math": 65}
]
students.sort(key=lambda s: s["math"], reverse=True)
print(students)


# 实战6：给定一个整数列表，计算并打印该列表中所有偶数地和
list2 = [3,1,4,2,1,5]
sum = 0         # 存储所有偶数和
for i in list2:
    if i % 2 == 0:
        sum += i
print(sum)


# 实战7：给定一个字典，其中每个人地姓名作为键，对应地年龄作为值
# 请找出年龄最大者的姓名与年龄，并打印出来
dict1 = {"张三": 18, "李四": 17, "王五": 21, "赵六": 20}
max_age = 0
max_name = ""
for key, value in dict1.items():
    if value >= max_age:
        max_age = value
        max_name = key
print(f"{max_name}:{max_age}")


# 实战8：给定一个已排序的整数列表，要求输入一个整数，
# 并根据列表原有的排序规律将其插入正确的位置
list3 = [1, 2, 3, 4, 5, 6, 7]
target = 7
for i in range(len(list3)):
    if list3[i] >= target:
        list3.insert(i, target)
        break
    elif i == len(list3) - 1:
        list3.append(target)

print(list3)