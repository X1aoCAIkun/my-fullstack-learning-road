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
students1 = [
    {"name": "小明", "math": 90},
    {"name": "小红", "math": 78},
    {"name": "小刚", "math": 65}
]
students1.sort(key=lambda s: s["math"], reverse=True)
print(students1)


# 实战6：给定一个整数列表，计算并打印该列表中所有偶数地和
list2 = [3,1,4,2,1,5]
sum1 = 0         # 存储所有偶数和
for i in list2:
    if i % 2 == 0:
        sum1 += i
print(sum1)


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


# 实战9：给定一行英文。忽略大小写，去掉,.!?;标点，统计词频。按词频降序
# 输出；次数相同按单词升序。最后输出不同单词的数量
text3 = "Hello hello world!Python,Python is hello"
words = re.findall(r"\w+",text3)
print(words)
counter = Counter(words)
print(counter)


# 实战10：开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5. 列出所有学生：遍历所有学生信息并输出。
# 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统。

students2 = {}      # 数据结构用字典嵌套字典：{name:{subject:score}}
while True:
    # 开始菜单
    print("-" * 110)
    print("欢迎使用教务管理系统".center(100, "-"))
    print("1.添加学生信息---2.修改学生信息---3.删除学生信息---4.查询学生信息---5.列出所有学生信息---6.统计班级成绩---7.退出系统")

    choice = input("输入数字则功能：")
    # 根据输入数字匹配对应操作
    match choice:
        case "1":
            name = input("输入学生姓名：")

            if name in students2.keys():        # 避免重复添加同一人
                print("该学生已经存在，重新选择操作")
                continue
            else:
                chinese = float(input("输入语文成绩："))
                math = float(input("输入数学成绩："))
                english = float(input("输入英语成绩："))
                students2[name] = {"chinese": chinese, "math": math, "english": english}
                print("添加成功，继续选择需要的操作")
                continue

        case "2":
            name = input("输入要修改信息的学生姓名：")

            if name not in students2.keys():            # 避免修改一个不存在的人
                print("该学生不存在，继续选择操作")
                continue
            else:
                chinese = float(input("输入语文成绩："))
                math = float(input("输入数学成绩："))
                english = float(input("输入英语成绩："))
                students2[name] = {"chinese": chinese, "math": math, "english": english}
                print("修改成功，继续选择需要的操作")
                continue

        case "3":
            name = input("输入要删除信息的学生姓名：")

            if name not in students2.keys():        # 避免删除一个不存在的学生
                print("该学生不存在，请重新选择操作")
                continue
            else:
                delete_student = students2.pop(name)
                print(f"删除学生：{name}，信息：{delete_student}，删除成功，请继续选择操作")
                continue

        case "4":
            name = input("输入要查询信息的学生姓名：")

            if name not in students2.keys():        # 避免查询一个不存在的人
                print("该学生不存在，请重新选择操作")
                continue
            else:
                print(f"{name}的信息如下：")
                print(f"{students2[name]}")
                print("请继续选择操作")
                continue

        case "5":
            if not students2:       # 判空防止程序崩溃
                print("信息系统不存在信息，请重新选择操作")
                continue
            else:
                for name in students2:
                    print(f"{name}：{students2[name]}")
            continue

        case "6":
            cn_scores = []
            math_scores = []
            en_scores = []
            if not students2:       # 判空防止程序崩溃
                print("信息系统不存在信息，请重新选择操作")
            else:    
                # 收集各科成绩列表
                for name in students2:
                    cn_scores.append(students2[name]["chinese"])
                    math_scores.append(students2[name]["math"])
                    en_scores.append(students2[name]["english"])
                
                # 计算各科平均分
                ave_cn = sum(cn_scores) / len(cn_scores)
                ave_math = sum(math_scores) / len(math_scores)
                ave_en = sum(en_scores) / len(en_scores)
                
                #找寻各科最值
                min_cn = min(cn_scores)
                max_cn = max(cn_scores)
                min_math = min(math_scores)
                max_math = max(math_scores)
                min_en = min(en_scores)
                max_en = max(en_scores)

                min_cn_student = [name for name in students2 if students2[name]["chinese"] == min_cn]
                max_cn_student = [name for name in students2 if students2[name]["chinese"] == max_cn]
                min_math_student = [name for name in students2 if students2[name]["math"] == min_math]
                max_math_student = [name for name in students2 if students2[name]["math"] == max_math]
                min_en_student = [name for name in students2 if students2[name]["english"] == min_en]
                max_en_student = [name for name in students2 if students2[name]["english"] == max_en]

                # 输出综合信息
                print(f"各科平均分，语/数/英：{ave_cn}--{ave_math}--{ave_en}")
                print(f"各科最高/低分学生姓名，语/数/英：{max_cn_student}/{min_cn_student}-----{max_math_student}/{min_math_student}-----{max_en_student}/{min_en_student}")

        case "7":
            print("退出系统成功")
            break
            
        case _:
            print("选择错误，请重新选择")
            continue