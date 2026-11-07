class Account:
    def __init__(self, owner, balance=0):       # balance是默认参数
        self.owner = owner
        self._balance = balance     # 属性balance是“受保护的”

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        if n >self._balance:
            raise ValueError("余额不足")        # 抛出异常
        self._balance -= n

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f"<{type(self).__name__} {self.owner} ￥{self._balance}>"

class SavingAccount(Account):
    def __init__(self, owner, balance=0, rate=0.3):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance *= (1 + self.rate)

class CheckingAccount(Account):
        OVERDRAFT = 1000
        def withdraw(self, n):          # 方法重写：允许透支1000
            if n >self._balance + self.OVERDRAFT:
                raise ValueError("超出透支限额")
            self._balance -= n

s = SavingAccount("李雷", 1000)
s.add_interest()
print(s)            # <SavingAccount 李雷 ￥1030.0>

c = CheckingAccount("韩梅梅", 500)
c.withdraw(800)             # 没有超过透支额度，不抛出异常
print(c)            # <CheckingAccount 韩梅梅 ￥-300>