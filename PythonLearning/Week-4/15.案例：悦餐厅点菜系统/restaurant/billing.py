# 算账（Part 3 考点：函数参数 + map / filter / reduce 高阶函数）
from functools import reduce


# 总价 = 菜品总价 × 折扣 + 附加费（**fees 如 打包费=2）
def calc_total(orders, menu, discount=1.0, **fees):
    prices = list(map(lambda name: menu[name].price, orders))  # map：取每道菜价格
    dish_total = reduce(lambda a, b: a + b, prices, 0)         # reduce：累加求和
    return dish_total * discount + sum(fees.values())


# filter：统计购物车里的辣菜道数
def spicy_count(orders, menu):
    spicy = filter(lambda name: "辣" in menu[name].tags, orders)
    return len(list(spicy))
