# 数据模型（Part 4 考点：类/继承/多态/魔法方法/property/dataclass/enum）
import re
from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    """菜品类目（枚举）"""
    SPICY = "辣"
    SWEET = "甜"
    VEGETABLE = "素"


# 菜品类
class Dish:
    def __init__(self, name, price, tags, category=""):
        self.name = name            # 菜名
        self.price = price          # 价格
        self.tags = tags            # 口味标签列表
        self.category = category    # 分类（Category 枚举或字符串）

    # 输出菜品信息（直接 print 对象时）
    def __str__(self):
        return f"{self.name} {self.price}元 {'、'.join(self.tags)}"

    # 输出菜品信息（print 字典/列表里的 Dish 时）
    def __repr__(self):
        return self.__str__()

    # 对 < 重载：按价格比较（菜单排序用）
    def __lt__(self, other):
        return self.price < other.price


# 顾客类（基类）
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance    # 私有属性：外部不能直接访问/修改

    # 支付：余额不足返回 False
    def pay(self, money):
        if money > self.__balance:
            return False
        self.__balance -= money
        return True

    # 余额回补（VIP 返现时调用，避免子类直接碰私有属性）
    def refund(self, money):
        self.__balance += money

    # @property：余额变成只读属性，外部能看不能改
    @property
    def balance(self):
        return self.__balance

    # 类方法：从 "姓名,余额" 字符串创建顾客
    @classmethod
    def from_line(cls, line):
        name, balance = line.split(",")
        return cls(name, float(balance))

    # 静态方法：正则校验手机号
    @staticmethod
    def is_phone_valid(phone):
        return bool(re.fullmatch(r"1[3-9]\d{9}", phone))


# VIP 顾客：继承 Customer，重写 pay，支付后返现 5%
class VipCustomer(Customer):
    def pay(self, money):
        if money > self.balance:
            return False
        super().pay(money)
        self.refund(money * 0.05)
        return True


# 订单条目（结算时把购物车整理成 OrderItem 列表）
@dataclass
class OrderItem:
    dish: Dish
    count: int


# 多态：同一个函数，普通顾客和 VIP 表现不同
def checkout(customer, total):
    return customer.pay(total)


if __name__ == "__main__":
    # 多态测试
    normal = Customer("张三", 100)
    vip = VipCustomer("李四", 100)
    print(checkout(normal, 50), normal.balance)     # True 50
    print(checkout(vip, 50), vip.balance)           # True 52.5（返现 2.5）

    # 类方法测试
    c = Customer.from_line("王五,66.6")
    print(c.name, c.balance)                        # 王五 66.6

    # 静态方法测试
    print(Customer.is_phone_valid("13812345678"))   # True
    print(Customer.is_phone_valid("12345"))         # False

    # dataclass 测试
    print(OrderItem(Dish("宫保鸡丁", 28, ["辣"]), 2))
