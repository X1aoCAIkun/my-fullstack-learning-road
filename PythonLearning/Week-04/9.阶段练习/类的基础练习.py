# 定义一个`Student`类

# 1. 实例属性：姓名 name (公有)，学号`__id`(私有属性)
# 2. 实例方法`show_info()`：打印学生姓名和学号（只能在类内部访问私有`__id`）
# 3. 类方法`get_class_name()`：返回字符串 "学生管理类"
# 4. 静态方法`is_adult(age)`：接收年龄，返回 True (≥18) / False (<18)

# 测试：

# - 创建学生对象：name="张三"，id="2026001"
# - 调用 show_info ()
# - 调用类方法、静态方法测试年龄 19、17


class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def show_info(self):
        print(f"姓名：{self.name} 学号：{self.__id}")

    @classmethod
    def get_class_name(cls):
        return "学生管理类"

    @staticmethod
    def is_adult(age):
        return age >= 18


stu = Student("张三", 2026001)
stu.show_info()
print(Student.get_class_name())
print(stu.is_adult(19))
print(Student.is_adult(17))