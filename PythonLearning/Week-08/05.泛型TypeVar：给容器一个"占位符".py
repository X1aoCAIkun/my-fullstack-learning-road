# 如果你写了一个“装任何类型的栈”，你不希望写两次（一次给 int，一次给 str）

from typing import Generic, TypeVar

T = TypeVar("T")                # 创建类型占位符 T ，它可以是任意类型   

class Stack(Generic[T]):        # Generic 让类支持泛型参数
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, x: T) -> None:
        self._items.append(x)

    def pop(self) -> T:
        return self._items.pop()

s: Stack[int] = Stack()         # 创建一个只装整数的栈
s.push(1)
s.push(2)          # mypy 报错：期望 int，但是得到 str
# 这样就不需要创建两个栈，只需要新创建对象时修改传入 T 的类型就可以