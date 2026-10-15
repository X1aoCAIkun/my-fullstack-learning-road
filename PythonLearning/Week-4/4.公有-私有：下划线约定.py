class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # 公有
        self._secret = "内部用"      # 单下划线：约定“别动我” 受保护的
        self.__pin = "1234"         # 双下划线：名称改动 私有的

a = Account("李雷", 100)
print(a.owner)          # 李雷
print(a._secret)            # "内部用"，仍然可以访问，这只是人为约定的
# print(a.__pin)            # AttributeError
print(a._Account__pin)      # 1234（双下划线被改成_类名__name）

# 注意Python没有真正的私有--只有“君子协定”。“_”表示内部，"__"表示“我真的不想让你碰”