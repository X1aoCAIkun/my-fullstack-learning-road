# 1. 定义形式单/双引号都可以,三队双引号可以进行多行注释
s1 = "Hello"

s2 = 'Hi'

s3 = """Hello everyone
my name is yu
nice too meet you"""

# +可以用于字符串的拼接
s4 = s1 + s2
print(s4)       # "HelloHi"

# （*）可以表示一个字符串进行多次自拼接
s5  = s2 * 3
print(s5)       #"HiHiHi"

# 2. 切片操作：就是将字符串的一部分提出
# 形式：s[起点：终点：步长]，默认值为：0、字符串的长度、1
# 起点：是切片的第一个字符（最前的起点是0）
# 终点：是切片终止的后一个位置，终点上的字符不会被取到（比如要取0、1、2三个字符，那终点就是3）
# 步长：表示自起点每几个字母后输出（1为依次输出，-1为从后输出）
# 三者可以省略不写，但顺序不会变
s6 = "Python"
print(s6[0])        # "p"
print(s6[-1])       # "n"
print(s6[0:3])      # "Pyt"
print(s6[2:])       # "thon"
print(s6[ : : -1])      # "nohtyP"

# 3.f-string格式化操作：让输出格式更加美观，直观
# 形式为print(f"{变量名/表达式}……………………{变量名/表达式}")
name = "小明"
score = 79
print(f"{name}这次考了{score}分，{"及格" if score >= 60 else "不及格"}")
#输出为：“小明这次考了79分，及格”

# 4.字符串常用的一般方法
#形式：变量名.方法名()
s7 = "  Hello Python  "
print(s7.strip())          # 'Hello Python'  去首尾空格
print(s7.lower())          # 全小写
print(s7.upper())          # 全大写
print(s7.replace("o","0")) # 替换
print(s7.split())          # ['Hello', 'Python']  按空格分割
print("-".join(["a","b","c"]))  # a-b-c  用 - 连接
print("Python".startswith("Py"))# True
print("Python".endswith("on"))  # True
print("Python".find("th"))      # 2  找不到返回 -1
print(len("Python"))            # 6  长度
print(ord('A'))                 # 65 ord()可以将字符转换为它对应的Unicode编码
print((chr(65)))                # 'A'，作用与ord()相反

# 5.占位符% %s(占位字符) %d(占位整数)等
print("Hello,%s"%'world')       # Hello,world
print("Hi, %s, you have $%d." % ('Michael', 1000000))       # 'Hi, Michael, you have $1000000.'
print("%2d-%02d" % (3, 1))              #  3-01  %2d表示占两位，%02d表示占两位添一个0
print("%.2f" % 3.1415926)               # 3.14  .2f表示保留小数点后两位
# 注意 %s可以将所有数据类型转换为字符串
print("age: %s,gender: %s" %(18 , True))

# format(),会将format()数据传入{0},{1}…………中
print("Hello, {0}, 成绩提升了 {1:.1f}%".format('小明', 17.125))         # 'Hello, 小明, 成绩提升了 17.1%'