# 除了基础的类型注解，还有一些特殊的类型注解需要学习
"""
注解                            含义                                    例子
Optional[x]或x | None           x或None                                 name: str | None = None
Union[A, B]或A | B              A或B                                    x: int | str
Literal["a", "b"]               只能是这几个具体值                       mode: Literal["r", "w"]
Any                             任何类型（关掉检查）                      data: Any
Callable[[int, str], bool]      一个吃（int, str）返回bool的函数          见下面例子
Final[int]                      常量，不能再赋值                          PI: Final = 3.14
"""

# 对于 Literal 和 Callable 需要导入
from collections.abc import Callable
from typing import Literal


def open_file(path: str, mode: Literal["r", "w", "a"] = "r") -> None:
    print(path, mode)

# open_file("a.text", "x")        # mypy 报错：Literal 只允许 r/w/a
# 注意这里是需要文件保存后才会 显示/消除 报错

def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)

print(apply(lambda n: n * 2, 5))        # 10


# 练习：写一个 parse_age(value: str | int) -> int，
# 传字符串和整数都能解析，非数字字符串抛 ValueError。
def parse_age(value: str | int) -> int:
    if isinstance(value, int):
        return value
    if value.isdigit():     # 注意：bool被认为是字符串
        return int(value)
    raise ValueError(f"非法年龄：{value!r}")

print(parse_age(18), parse_age(20))             # 18 20