# 实现一个账户系统

# 1. 类 `Account`
#    - 公有：用户名 name
#    - 私有：`__balance` 余额
#    - 实例方法 `deposit(money)`：存钱，money>0 才增加余额
#    - 实例方法 `get_balance()`：查看私有余额（外部不能直接访问__balance）
#    - 类方法 `bank_name()`：返回 "XX 银行账户系统"
#    - 静态方法：`is_positive(num)` 判断数字是否大于 0
# 2. 子类 `VipAccount` 继承 Account
#    - 重写 deposit 方法：存钱额外赠送 1% 金额（比如存 100，实际入账 101）
# 3. 多态测试：写函数`add_money(account, num)`，调用 deposit
# 分别传入普通 Account 对象、VipAccount 对象测试存钱


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, money):
        if money > 0:
            self.__balance += money

    def get_balance(self):
        return self.__balance

    @classmethod
    def bank_name(cls):
        return "农业银行账户系统"

    @staticmethod
    def is_positive(num):
        return num > 0

class VipAccount(Account):
    def deposit(self, money):
        if money > 0:
            # 不建议这样写
            # self._Account__balance += 1.01 * money
            super().deposit(money * 1.01)

def add_money(account, num):
    account.deposit(num)

normal_a = Account("na", 0)
vip_a = VipAccount("va", 0)
print(normal_a.is_positive(100))        # True
add_money(normal_a, 100)
print(vip_a.is_positive(100))           # True
add_money(vip_a, 100)
print(normal_a.get_balance())           # 100
print(vip_a.get_balance())          # 101
print(Account.bank_name())          # 农业银行账户系统
