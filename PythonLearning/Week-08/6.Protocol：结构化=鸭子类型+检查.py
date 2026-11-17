# 类比：你不在乎它叫什么名字（class），只在乎它会不会嘎嘎叫（方法）

from typing import Protocol


class Drawable(Protocol):       # 一个类不需要显示继承 Drawable ，只要有 draw 方法，就可以被 mypy 当成 Drawable 类来使用
    def draw(self) -> None:
        ...         # 协议方法的占位说明e

class Circle:
    def draw(self) -> None:
        print("画圆")

class Square:
    def draw(self) -> None:
        print("画方")

def render(items: list[Drawable]) -> None:
    for it in items:
        it.draw()

render([Circle(), Square()])            # 画圆  画方  它们都没继承 Drawable ，但都“长得像”
# Protocol 是 Python 类型系统里最优雅的设计之一