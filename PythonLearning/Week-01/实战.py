# 实战1：BMI计算器

# 定义height和weight两个变量接收用户的身高与体重
height = float(input("请输入身高（m）："))
weight = float(input("请输入体重（kg）："))

# bmi的计算
bmi = weight / (height ** 2)
print(f"你的BMI指数为：{bmi:.2f}")      # :.2f表示保留两位小数

# 根据bmi划分区间
if bmi >= 28.0:
    print("肥胖")
elif 24.0 <= bmi <= 27.9:
    print("超重")
elif 18.5 <= bmi <= 23.9:
    print("正常")
else:
    print("偏瘦")


# 实战二：猜数字游戏
import random       # 引入python包便于使用方法

# target用于存放待猜的数字
target = random.randint(1,1000)     # 随机生成有一个1~999的数字
round = 0       # 用于记录猜数轮次

while True:         # 没猜中之前一直进入循环
    guess = int(input("输入一个数字："))
    round += 1        # 输入一个数字后回合数加1
    if guess < target:
        print("小了")        # 每轮输入一个猜的数字
    elif guess > target:
        print("大了")
    else:
        print(f"猜中了,猜了{round}次")
        break           # 结束循环


# 实战三：九九乘法表

for i in range(1,10):       # 控制第一个数
    for j in range(1,i + 1):    #控制第二个数
        print(f"{j} * {i} = {i * j}",end = "\t")        # 同一行的表达式间隔一个"\t"
    print()     #换行