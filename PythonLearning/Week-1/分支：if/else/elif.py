# if顾名思义就是如果的意思，后接一个判断表达式，只有表达式的值为True时才会执行if的代码块
# else则是当跳过if代码块后的执行，else后不接表达式,只有当if/elif都每执行才会执行
# 每个else会与其之前最近的if相匹配
# elif用于需要多个if的时候，表明有多个判断
# 注意：if/elif会顺序判断，当一个判断成功后，后续判断不会执行

score = int(input("请输入分数："))      # 字符串不比较大小，所以转换为int
if score >= 90:     # 注意：写完表达式后需要加‘:’
    print("A")      # Python用缩进来区分不同的代码块
elif score >=80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("不及格")
# 输入   输出
# 90    "A" 
# 80    "B" 
# 60    "C"
# 50    "不及格"