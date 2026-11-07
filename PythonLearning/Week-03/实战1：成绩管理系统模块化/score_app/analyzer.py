# 计算平均分
def average(students, subject):
    return sum(s[subject] for s in students) / len(students)