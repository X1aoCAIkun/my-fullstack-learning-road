# 1.定义两个整型变量，计算它们的和，并打印输出
x1 = int(input("输入被加数："))
x2 = int(input("输入加数："))
print(f"{x1} + {x2} = %d" %(x1 + x2))

# 2.定义两个整型变量，比较它们的值，并打印输出
x3 = int(input("输入第一个数："))
x4 = int(input("输入第二个数："))
if x3 > x4:
     print(f"{x3}大于{x4}")
elif x3 == x4:
     print(f"{x3}等于{x4}")
else:
     print(f"{x3}小于{x4}")

# 3.计算1~100（包含1和100）所有的整数和
sum = 0
for i in range(1,101):
    sum += i
print(f"1~100（包含1和100）所有的整数和为：{sum}")

# 4.输出由1，2，3，4四个数组成的互不重复,且三个数字各不相同的三位数
num = 0
for i in range(1,5):
     for j in range(1,5):
          for k in range(1,5):
               if i != j and i != k and j != k:
                    num += 1
                    print(i * 100 + j * 10 + k , end='\t')
print(f"共{num}个数")

# 5.打印九九乘法表
for i in range(1,10):
     for j in range(1,i + 1):
          print(f"{j} * {i} = %d" %(i * j) , end='\t')
     print()

# 6.打印所有水仙花桃数（指一个三位数，其各位数字立方和等于改数本身，如：1^3+5^3+3^3=153）
count = 0
for i in range(100,1000):
     if (i // 100) ** 3 + (i % 10) ** 3 + ((i % 100) // 10) ** 3 == i:
          count += 1
          print(i)
print(f"共{count}个水仙花桃子数")

# 7.猴子第一天宅摘下了若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，第二天早上又将剩下的桃子
# 吃掉一半，又多吃了一个，以后每天把早上都吃了前一天剩下的一半零一个，到第10天早上想再吃时，见只
# 剩下一个桃子了，求第一天一共摘了多少个桃子
current = 1         # 最后一天剩下一个桃子
for i in range(1,10):
      current = (current + 1) * 2       # 向前一天计算
print(f"摘了{current}个桃子")

# 8.输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
s1 = input("输入一串字符串：")
letter = 0      # 英文字母
digit = 0       # 数字
space = 0       # 空格
other = 0       # 其他字符
for i in s1:
    if i.isalpha():        # isalpha()是判断字符是否为英文字母的函数
        letter += 1
    elif i.isdigit():      # isdigit()是判断字符是否为数字的函数
        digit += 1
    elif i.isspace():      # isspace()是判断字符是否为空格的函数
        space += 1
    else:
        other += 1
print(f"{s1}由{letter}个英文字母,{digit}个数字,{space}个空格,{other}个其他字符组成")

# 9.接收用户输入的三个数字，并按从小到大的顺序排列
x5 = float(input("输入第一个数字："))
x6 = float(input("输入第二个数字："))
x7 = float(input("输入第三个数字："))
tem = 0
if x5 > x6:
     tem = x5
     x5 = x6
     x6 = tem
if x5 > x7:
     tem = x5
     x5 = x7
     x7 = tem
if x6 > x7:
     tem = x6
     x6 = x7
     x7 = tem 
print(f"三个数排列好后：{x5}-{x6}-{x7}")

# 10.用户输入一个奇数，程序需要找到一个最小的由连续9组成的数，这个数能被用户输入的数整除
# 输出这个最小的数以及它除以输入的奇数的结果
x8 = int(input("输入一个奇数"))
n = 1
while True:
     n_9 = int('9' * n)
     if n_9 % x8 == 0:
          print(f"这个最小数为:{n_9}，除法结果为：{n_9} / {x8} = {int(n_9 / x8)})")
          break
     else:
          n += 1

# 11.提示用户最多连续输入7个整数（每个数再1~50之间，包括1和50），对于有效数字打印
round = 1
while True:
     if round <= 7:
        x9 = int(input(f"输入一个1~50的整数，最多输入7次，这是第{round}次，输入0终止"))
     else:
          break
     if 1 <= int(x9) <= 50:
          print(f"{x9}为有效数字")
          round += 1
     elif x9 == 0 or round > 7:
          print("程序终止")
          break
     else:
          print("输入数字无效")
          continue
