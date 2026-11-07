# 购物车与筛选（Part 2 考点：list / set / 列表推导式）

# 点菜：菜名加入购物车 list（允许重复点）
def add_dish(cart, name):
    cart.append(name)


# 删掉购物车里一份该菜，没有则返回 False
def remove_dish(cart, name):
    if name in cart:
        cart.remove(name)   # list.remove 只删第一个匹配
        return True
    return False


# 统计：返回 (菜品种类数, 总道数)，种类用 set 去重
def cart_stats(cart):
    return len(set(cart)), len(cart)


# 列表推导式：只看辣菜
def spicy_dishes(menu):
    return [dish for dish in menu.values() if "辣" in dish.tags]


# 列表推导式：只看 price 元以上的菜
def expensive_dishes(menu, price=30):
    return [dish for dish in menu.values() if dish.price > price]
