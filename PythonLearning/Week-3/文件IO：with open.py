# 文件操作可以将数据存储下来，省去每回的输入


# 1.写操作
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n第二行\n")


# 2.读操作
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)


# 3.按行读（推荐，省内存）
with open("hello.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())


# 总结一下
"""
with open会自动开关文件，建议一直使用with
"hello.txt"是打开的文件
r：只读（默认），打开的文件必须存在，否则出现异常
w：写（会清空原文件），打开的文件不存在会自动创建（存在主文件夹下）
a：追加，打开文件不存在也会自动创建
b：二进制，一般要配合使用（如rb、wb）
x：创建（已存在则报错）
encoding="utf-8",编码方式，这里是中文
as f ,是给打开的文件取别名
后面的部分就像函数体一样，是要对文件完成的操作
"""