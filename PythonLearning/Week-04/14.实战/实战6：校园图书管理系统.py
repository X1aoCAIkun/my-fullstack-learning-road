# 编写一个**图书管理系统**，包含多种书籍，
# 实现借阅、归还、逾期罚款、信息展示功能。


# 图书类（父类）
class Book:
    def __init__(self, book_id, book_name, author, price, status=0):
        self.book_id = book_id          # 书籍编号
        self.book_name = book_name      # 书籍名
        self.author = author            # 作者
        self.price = price              # 价格
        self.status = status            # 借阅状态（0表示可借阅，1表示已借出）

    # 展示图书信息
    def show_info(self):
        print(f"""
        书籍编号：{self.book_id}
        书籍名：{self.book_name}
        作者：{self.author}
        价格：{self.price}
        借阅状态：{self.status} 0可借 1已借出
        """)

    # 借书，以借出的书不能借
    def borrow(self):
        if not self.status:
            self.status = 1
            return True
        return False
    
    # 还书，未借出的书不能还
    def back(self):
        if self.status:
            self.status = 0
            return True
        return False


# 普通图书类（子类1）
class NormalBook(Book):
    def __init__(self, book_id, book_name, author, price, status=0):
        super().__init__(book_id, book_name, author, price, status)
    
    # 重写show_info方法
    def show_info(self):
        super().show_info()
        print("分类：普通图书")


# 杂志类（子类2）
class Magazine(Book):
    def __init__(self, book_id, book_name, author, price, issue, status=0):
        super().__init__(book_id, book_name, author, price, status)
        self.issue = issue      # 杂志期数

    # 重写show_info方法
    def show_info(self):
        super().show_info()
        print(f"期数：{self.issue}")

# 工具书类（子类3）
class ReferenceBook(Book):
    def __init__(self, book_id, book_name, author, price, is_only_read, status=0):
        super().__init__(book_id, book_name, author, price, status)
        self.is_only_read = is_only_read        # 是否仅馆内阅读

    # 重写borrow方法
    def borrow(self):
        if self.is_only_read:
            return False
        return super().borrow()

    # 重写show_info方法
    def show_info(self):
        super().show_info()
        if self.is_only_read:
            print("阅读权限：仅可以在馆内阅读")
        else:
            print("阅读权限：可以带离阅读")


# 管理员类
class LibraryManager:
    def __init__(self, book_list=None):
        if not book_list:
            book_list = []
        self.book_list = book_list

    # 添加书籍到系统
    def add_book(self, book):
        self.book_list.append(book)

    # 根据书名模糊查询，展示所有匹配书籍
    def search_book(self, name):
        flag = False        # 是否找到书籍的标志位
        for book in self.book_list:
            if name in book.book_name:
                book.show_info()
                flag = True
        if not flag:
            print("未找到该书籍")

    # 根据编号借书，包含状态判断
    def borrow_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                res = book.borrow()
                if res:
                    print(f"{book.book_name}被借出")
                else:
                    print(f"{book.book_name}已被借出或不可借出")
                return
        print("未找到该书籍")


    # 归还图书，传入借阅天数
    def return_book(self, days, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                ret = book.back()
                if not ret:
                    print("该书籍未被借出")
                    return
                if isinstance(book, NormalBook) and days > 30:
                    print(f"逾期罚款：{(days - 30) * 0.5}")
                print("还书完成")
                return
        print("未找到该编号书籍")

    # 展示全馆书籍状态
    def show_all_book(self):
        for book in self.book_list:
            print(f"{book.book_name}：{book.status} 0可借阅 1已借出")


# 测试
if __name__ == "__main__":
    lib = LibraryManager()
    b1 = NormalBook(1, "Python入门", "张三", 45)
    b2 = Magazine(2, "编程周刊", "李四", 12, "2026‑08")
    b3 = ReferenceBook(3, "汉语大词典", "王五", 99, is_only_read=True)
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    print("====全部书籍====")
    lib.show_all_book()

    print("\n====借书测试====")
    lib.borrow_book(1)
    lib.borrow_book(3)   # 工具书仅馆内，借不出

    print("\n====查询书籍====")
    lib.search_book("Python")

    print("\n====逾期还书测试====")
    lib.return_book(35, 1)