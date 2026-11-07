# 悦餐厅点菜系统 —— 程序入口（Part 1 考点：输入/类型转换/while/match）
from restaurant import menu_loader, cart, billing, order_store
from restaurant.models import Customer, VipCustomer, OrderItem


def main():
    print("===== 悦餐厅点菜系统 =====")

    # --- 顾客信息：年龄决定折扣，VIP 决定返现 ---
    name = input("请输入您的姓名：").strip()

    while True:
        age_str = input("请输入您的年龄：").strip()
        if age_str.isdigit():
            age = int(age_str)
            break
        print("年龄必须是数字，请重新输入")
    discount = 0.8 if age < 6 or age >= 65 else 0.95
    print(f"您的折扣：{discount}")

    is_vip = input("您是VIP会员吗？(y/n)：").strip().lower() == "y"
    while True:
        balance_str = input("请输入账户余额：").strip()
        if balance_str.replace(".", "", 1).isdigit():
            balance = float(balance_str)
            break
        print("余额必须是数字，请重新输入")
    customer = VipCustomer(name, balance) if is_vip else Customer(name, balance)

    menu = menu_loader.load_menu()
    cart_list = []

    # --- 主菜单循环 ---
    while True:
        print("\n1. 点菜  2. 查看购物车  3. 结算  4. 退出  5. 添加菜品  6. 订单记录")
        choice = input("请选择：").strip()

        match choice:
            case "1":   # 点菜
                print("\n--- 今日菜单（按价格从低到高）---")
                for dish in sorted(menu.values()):      # sorted 用到 Dish.__lt__
                    print(dish)
                while True:
                    order = input("输入菜名点菜（del 菜名 删一道，直接回车返回）：").strip()
                    if order == "":
                        break
                    if order.startswith("del "):
                        target = order[4:].strip()
                        if cart.remove_dish(cart_list, target):
                            print(f"已移除一份：{target}")
                        else:
                            print("购物车里没有这道菜")
                    elif order in menu:
                        cart.add_dish(cart_list, order)
                        print(f"已加入购物车：{menu[order]}")
                    else:
                        print("没有这道菜，请重新输入")

            case "2":   # 查看购物车
                if not cart_list:
                    print("购物车是空的")
                else:
                    kinds, total = cart.cart_stats(cart_list)
                    print(f"您共点了 {kinds} 种菜，共 {total} 道：")
                    for dish_name in set(cart_list):
                        count = cart_list.count(dish_name)
                        print(f"  {dish_name} x{count}（{menu[dish_name].price}元/份）")
                    print("只看辣菜：")
                    for dish in cart.spicy_dishes(menu):
                        print(f"  {dish}")
                    print("只看30元以上的菜：")
                    for dish in cart.expensive_dishes(menu):
                        print(f"  {dish}")

            case "3":   # 结算
                if not cart_list:
                    print("购物车是空的，先去点菜吧")
                else:
                    original = billing.calc_total(cart_list, menu)
                    packing_fee = 2 if len(cart_list) >= 3 else 0
                    pay = billing.calc_total(cart_list, menu, discount=discount, 打包费=packing_fee)
                    print(f"原价 {original:.2f} 元 → 折后应付 {pay:.2f} 元（含打包费 {packing_fee} 元）")
                    print(f"其中辣菜 {billing.spicy_count(cart_list, menu)} 道")

                    while True:     # 正则校验手机号（Customer 的静态方法）
                        phone = input("请输入手机号：").strip()
                        if Customer.is_phone_valid(phone):
                            break
                        print("手机号格式不正确（如 13812345678），请重新输入")

                    if customer.pay(pay):      # 多态：普通顾客/VIP 支付表现不同
                        print(f"支付成功！余额 {customer.balance:.2f} 元")
                        if isinstance(customer, VipCustomer):
                            print("已返现 5% 到余额")
                        items = [OrderItem(menu[n], cart_list.count(n)) for n in set(cart_list)]
                        order_store.save_order(customer.name, items, pay, phone)
                        print("订单已写入 orders/订单记录.txt")
                        cart_list.clear()
                    else:
                        print(f"余额不足（当前 {customer.balance:.2f} 元），支付失败")

            case "4":   # 退出
                print("谢谢惠顾，再见！")
                break

            case "5":   # 添加菜品（扩展功能：写回 menu.json）
                menu_loader.add_dish(menu)
                menu_loader.save_menu(menu)
                print("菜单已保存到 menu.json")

            case "6":   # 查看订单记录
                order_store.show_orders()

            case _:
                print("无此选项，请重新输入")


if __name__ == "__main__":
    main()
