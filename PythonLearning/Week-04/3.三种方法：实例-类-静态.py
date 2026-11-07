class Counter:
    total = 0                   # 类属性（所以实例对象都可以使用）

    def __init__(self):
        self.value = 0          # 实例属性

    def incr(self):             # 实例方法，操作单个实例
        self.value += 1
        Counter.total += 1

    @classmethod
    def stats(cls):             # 类方法(cls = 类本身)， 操作类本身
        print(f"总共 {cls.total} 次")

    @staticmethod
    def help():                 # 静态方法(没有self / cls)，工具函数，逻辑上属于类
        print("Counter 用法：c.incr()")

a = Counter(); a.incr(); a.incr()
b = Counter(); b.incr()
Counter.stats()         # 总共 3 次
Counter.help()