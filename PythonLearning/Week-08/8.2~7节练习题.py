# Week-08 练习题（覆盖第 2~7 节）
# 要求：所有函数、变量、类都要写完整的类型注解，写完用 mypy 检查一遍
# 运行：mypy "Week-08/8.练习题.py"

import random
from collections.abc import Callable
from typing import Final, Generic, Literal, Protocol, NotRequired, TypedDict, TypeVar

# ============================================================
# 第 1 组：基础类型注解（对应第 2、3 节）
# ============================================================

# 1.1 给下面的函数补上注解：参数、返回值一个都不能少
def repeat(text: str, times: int = 2) -> str:
    return text * times


# 1.2 给下面的变量补上注解（注意 age 可能是 int 也可能是 str）
scores: list[int] = [90, 85, 77]
profile: dict[str, str | int] = {"name": "Alice", "age": 18}
point: tuple[float, float] = (1.0, 2.0)


# 1.3 思考题（写在注释里回答）：
# 下面这行代码，Python 运行时会报错吗？mypy 会报错吗？为什么？
def double(x: int) -> int:
    return x * 2

# print(double("ha"))   # 你的回答：运行时不会报错；mypy 会报错；因为注释并不会影响程序运行，但是 mypy 会根据注释检错


# ============================================================
# 第 2 组：特殊注解（对应第 4 节）
# ============================================================

# 2.1 写一个 find_user(user_id: int) 函数：
#     在下面的 USERS 里按 id 查找，找到返回名字，找不到返回 None
#     提示：返回值该用什么注解？
USERS = {1: "Alice", 2: "Bob"}

def find_user(user_id: int) -> str | None:
    for uid, name in USERS.items():
        if uid == user_id:
            return name
    return None

print(find_user(1))

# 2.2 写一个 set_level(level) 函数，level 只允许 "easy" / "normal" / "hard"
#     用注解保证传 "hell" 时 mypy 直接报错，函数体里打印 level 即可
def set_level(level: Literal["easy", "normal", "hard"]) -> str:
    return level

print(set_level("easy"))
# print(set_level("hell"))


# 2.3 写一个 retry(fn, times) 函数：
#     fn 是一个「无参数、返回 int」的函数
#     调用 fn，如果抛异常就重试，最多试 times 次，成功返回结果，全部失败抛 RuntimeError
#     提示：fn 的注解怎么写？
def retry(fn: Callable[[], int], times: int) -> int:
    error: Exception | None = None
    for _ in range(times):
        try:
            return fn()
        except Exception as e:
            error = e
    raise RuntimeError("多次运行仍然失败") from error

def get_number() -> int:
    if random.random() < 0.5:
        raise ValueError("值小于0.5")
    return 10

print(retry(get_number, 3))


# 2.4 定义一个常量 MAX_RETRY = 3，用注解保证它之后不能被重新赋值

MAX_RETRY: Final = 3


# 2.5 找错题：下面的 parse_age 有一个隐藏 bug（和第 4 节的练习同款）
#     想一想：parse_age(True) 会发生什么？为什么？怎么修？
def parse_age(value: str | int) -> int:
    if isinstance(value, int):
        return value
    if value.isdigit():
        return int(value)
    raise ValueError(f"非法年龄：{value!r}")

print(parse_age(True))      # 会直接输出 True 因为布尔类型是int的子类，所以在第一个判断为真

# 改进版
def parse_age_refine(value: str | int) -> int:
    if type(value) is int:
        return value
    if isinstance(value, str):
        return int(value)
    raise ValueError(f"非法年龄：{value!r}")

# print(parse_age_refine(True))         # 抛出异常


# ============================================================
# 第 3 组：TypeVar 泛型（对应第 5 节）
# ============================================================

# 3.1 仿照课上的 Stack，写一个泛型队列 Queue[T]：
#     enqueue(x: T) 入队，dequeue() -> T 出队（先进先出）
#     要求：Queue[int] 里 enqueue("hi") 时 mypy 必须报错

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue: list[T] = []

    def enqueue(self, value: T) -> None:
        self.queue.append(value)
        
    def dequeue(self) -> T | None:
        if not self.queue:
            return None
        return self.queue.pop(0)

q: Queue[int] = Queue()
# q.enqueue("hi")
        

# 3.2 写一个泛型函数 first(items: list[T]) -> T | None：
#     返回列表第一个元素，空列表返回 None
#     要求：传 list[int] 时，mypy 能推断出返回值是 int | None（而不是 Any）

def first(items: list[T]) -> T | None:
    if not items:
        return None
    return items[0]

lis: list[int] = [1]
print(first(lis))

# ============================================================
# 第 4 组：Protocol（对应第 6 节）
# ============================================================

# 4.1 定义一个协议 Speakable：要求有 speak(self) -> str 方法
#     再写两个「不继承任何协议」的类 Dog 和 Robot，各自实现 speak
#     写函数 announce(items: list[Speakable]) -> None，逐个打印 speak() 的结果
#     验证：announce([Dog(), Robot()]) 能通过 mypy
class Speakable(Protocol):
    def speak(self) -> str:
        ...

class Dog:
    def speak(self) -> str:
        return "汪汪"

class Robot:
    def speak(self) -> str:
        return "吱吱"

def announce(items: list[Speakable]) -> None:
    for item in items:
        print(item.speak())

announce([Dog(), Robot()])


# 4.2 思考题（写在注释里回答）：
#     如果给 Robot 删掉 speak 方法，mypy 会在哪一行报错？
#     是 Robot 类定义处，还是 announce 调用处？为什么？
# 会在调用 announce 函数这行；因为只有 announce 函数的参数 items 规定了列表的元素来自于 Speakable

# ============================================================
# 第 5 组：TypedDict（对应第 7 节）
# ============================================================

# 5.1 定义一个 Book(TypedDict)：title: str, author: str, price: float
#     构造一个合法的 Book 字典
#     再故意构造两个非法的（类型错一个、少一个键），用注释标出 mypy 会报什么错

class Book(TypedDict):
    title: str
    author: str
    price: float

b1: Book = {"title": "Python", "author": "tom", "price": 23.5}
# b2: Book = {"title": "Python", "author": "tom", "price": "23.5"}            # Incompatible types
# b3: Book = {"title": "Python", "price": 23.5}               # Missing key "author" for TypedDict "Book"

# 5.2 写函数 discount(book: Book, percent: float) -> Book：
#     返回一个价格打折后的「新」Book（不要改原字典）
def discount(book: Book, percent: float) -> Book:
    return {**book, "price": book["price"] * percent}

print(discount(b1, 0.5))

# 5.3 进阶：API 返回的用户数据里 nickname 字段可能没有
#     定义 UserDict：id: int, name: str 必填，nickname: str 可选
#     提示：查一下 NotRequired（Python 3.11+）或 total=False 的用法

class UserDict(TypedDict):
    id: int
    name: str
    nickname: NotRequired[str]

u1: UserDict = {"id": 1, "name": "tom", "nickname": "dick"}
u2: UserDict = {"id": 1, "name": "jack"}

# ============================================================
# 第 6 组：综合题（串起 2~7 节）
# ============================================================

# 6.1 迷你购物车：
#     a) 定义 Item(TypedDict)：name: str, price: float, qty: int
#     b) 写泛型类 Cart(Generic[T])：add(x: T)、items() -> list[T]
#     c) 写函数 total(cart: Cart[Item], coupon: Callable[[float], float] | None = None) -> float
#        计算总价（price * qty 求和）；如果传了 coupon，就把 coupon 作用在总价上
#     d) 用 Literal 定义支付方式 PayMethod = "alipay" / "wechat" / "cash"
#        写 checkout(cart: Cart[Item], method: PayMethod) -> None，打印应付金额和支付方式
#     验收：Cart[Item] 里 add("not an item") 必须被 mypy 拦下

class Item(TypedDict):
    name: str
    price: float
    qty: int

class Cart(Generic[T]):
    def __init__(self) -> None:
        self.goods: list[T] = []

    def add(self, x: T) -> None:
        self.goods.append(x)

    def items(self) -> list[T]:
        return self.goods

def total(cart: Cart[Item], coupon: Callable[[float], float] | None = None) -> float:
    goods: list[Item] = cart.items()
    cost = 0.0
    for g in goods:
        cost += g["price"] * g["qty"]
    if not coupon:
        return cost
    return coupon(cost)

def coupon(cost: float) -> float:
    return cost * 0.8

def checkout(cart: Cart[Item], method: Literal["alipay", "wechat", "cash"]) -> None:
    cost = total(cart)
    print(f"支付金额：{cost}， 支付方式：{method}")

g: Cart[Item] = Cart()
# g.add("not a item")