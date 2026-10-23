# 闭包就像人一直带着脑子一样，函数始终带着自己的环境（外层变量）

def make_counter():
    count = 0       # 外层变量
    def inner():
        nonlocal count              # 声明这个count是外层函数的那个count
        count += 1
        return count
    return inner

c = make_counter()          # 这里c就等效于inner函数了
print(c(), c(), c())        # 1, 2, 3  这里就像把inner函数剥离了make_counter
# 可以知道inner函数脱离了make_counter函数后使用的count依然外层变量

# 闭包的经典用例
def make_addr(n):           # 这里的n就是外部变量
    def add(x):
        return x + n
    return add

add5 = make_addr(5)         # 可以理解为add5既接收了add函数，也接收了外部变量n
add10 = make_addr(10)
print(add5(3), add10(3))        # 8, 13 
# 总结：闭包 = 函数 + 它记住的外部变量