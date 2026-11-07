# 要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
# 需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
# 其中，部门经理的月薪是固定 15000 元；
# 程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
# 销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。


from abc import ABCMeta, abstractmethod


# 分析题目可知，有员工、部分经理、程序员、销售员四类对象，且员工是其他三类
# 的父类，但是员工类在后续不会实例对象（因为员工是有具体职能的），所以这里
# 员工可以使用抽象类
class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    # 这里用装饰器声明为抽象方法（是为了让子类去重写）
    @abstractmethod
    def get_salary(self):
        pass

# 部门经理类
class Manager(Employee):
    def get_salary(self):
        return 15000

# 程序员类
class Programmer(Employee):
    def __init__(self, name, work_hours=0):
        super().__init__(name)
        self.work_hours = work_hours

    def get_salary(self):
        return self.work_hours * 200

# 销售员类
class Salesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05


employees = [Manager("张三"), Programmer("李四"), Salesman("王五")]
for em in employees:
    if isinstance(em, Programmer):           # instance用于比较两参数是否类型一致
        em.work_hours = int(input("输入程序员工作时长："))
    elif isinstance(em, Salesman):
        em.sales = int(input("输入销售员销售额："))
    print(f"{em.name}本月工资：￥{em.get_salary():.2f}")