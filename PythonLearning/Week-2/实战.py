# 实战1：词频统计升级版（使用正则）
import re
from collections import Counter

text = """
Python is great Python is easy Python is fun
We  love Python because Python makes life easy
"""

words = re. findall(r"\w+", text.lower())           # 全部小写并提取
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

text = "apple banana apple orange banana apple apple orange grape"
counter = Counter(text.split())

for word, n in counter.most_common():
    print(f"{word:<8} {'#' * n}  ({n})")

