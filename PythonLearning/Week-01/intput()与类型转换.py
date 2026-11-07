# input()方法用于接收输入，接收的输入都会转换为字符串,()中可以加入字符串以提示输入
name = input("请输入姓名：")        # 程序会在这停下等待输入，知道输入回车
age = input("请输入年龄：")

print(type(age))        # <class'str'>

# 类型名()的方法可以显示转换变量类型至指定类型
age = int(age)
print(type(age))        # <class'int'>
print(f"你明年的年龄是：{age + 1}")     # "你明年的年龄是：age + 1"

# 这里区分一下显示与隐示转换
#隐示转换是Python自己判断转换类型，如：1 + 2.0 Python会自动将1由int转换为float
#显示转换就是用户明确了转换类型，如：int(x)