# 参数作为“食材”，是决定函数产出结果的决定性因素之一


# 1.4种参数
def order(name, size="中杯", *toppings, **options):
    print(f"{name}一杯{size}")
    print("加料：", toppings)
    print("配置：", options)

order("拿铁")   # 因为order函数没有返回值且有print输出，所以不需要变量直接调用函数
# 拿铁一杯中杯
# 加料：()
# 配置：{}

# 解释这4种参数
# name：位置参数（必填），不填的话后续调用函数也不可以传参
# size：默认参数（也可以传参）
# \*toppings：收集多余参数转为tuple，不知道传入多少个参数时用
# \**options：收集多余关键字参数转为dict，不知道传入多少个关键字参数时用
# 注意这4种参数的位置不可以调换，位置参数->默认参数->*arg->**kwargs


# 2.关键字调用
# 一般调用实参是顺序传给形参,关键字调用就是在传参时直接指定实参传给哪个形参，
# 这样就可以不要注意位置
def power(base, exp):
    return base ** exp

print(power(2, 10))         # 1024
# 关键字调用
print(power(exp=10, base=2))        # 1024

# 如果想要参数一定为位置参数可以这样：def test(a, b, c, /)，此时a,b,c不可以关键字传参
# 同样，def test(*, a, b, c)就必须关键字传参
