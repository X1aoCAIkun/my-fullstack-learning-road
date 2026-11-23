import json
from collections.abc import Callable
from datetime import datetime, timedelta
from pathlib import Path
from typing import Final, Generic, Literal, Protocol, TypedDict, TypeVar

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

#  a) 类型别名 + 常量（第 4、9 节）
type BookId = int
type FineRule = Callable[[int], float]  # 逾期天数，返回罚金
MAX_BORROW_DAYS: Final = 30


# b) TypedDict 接外部数据（第 7 节）
class RawBook(TypedDict):
    id: int
    title: str
    isbn: str  # 国际标准图书号
    stock: int


c_dict: RawBook = {"id": 1, "title": "Python 101", "isbn": "978-3-16-148410-0", "stock": 5}
# e_dict: RawBook = {"id": 2, "title": "Python 102", "stock": 3}          # Missing key
# 思考题写进注释：
# 外部数据为什么先用 TypedDict 接再转 Pydantic？（提示：TypedDict 在运行时是什么东西？）
# TypeDict 是用 mypy做静态校验不会对运行有影响，这要没有校验成本
# 再转为 Pydantic 模型，在运行时校验数据，区分原始不可信数据和校验完的数据


# c) Pydantic 模型（第 12、14 节）
class Book(BaseModel):
    id: BookId
    title: str = Field(min_length=1, max_length=100)
    isbn: str
    stock: int = Field(ge=0)
    status: Literal["available", "borrowed"] = Field(default="available")
    borrowed_at: datetime | None = Field(default=None)

    @field_validator("title")
    @classmethod
    def check_title(cls, v: str) -> str:
        c_v = v.strip()
        if not c_v:
            raise ValueError("title 不能为空白")
        return c_v

    @model_validator(mode="after")
    def check_borrow_at(self) -> "Book":
        if self.status == "borrowed" and self.borrowed_at is None:
            raise ValueError("书本已借出，借出时间不能为空")
        if self.status == "available" and self.borrowed_at is not None:
            raise ValueError("书本未借出，不能有借出时间")
        return self

    @classmethod
    def from_raw(cls, raw: RawBook) -> "Book":
        new_book: Book = Book(id=raw["id"], title=raw["title"], isbn=raw["isbn"], stock=raw["stock"])
        return new_book


# d) 泛型仓库（第 5 节）
T = TypeVar("T", bound=Book)  # 限定 T 是 Book 或其子类


class Repo(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get(self, bid: BookId) -> T | None:
        for b in self._items:
            if b.id == bid:
                return b
        return None

    def all(self) -> list[T]:
        return self._items


# 思考题写进注释：get 的 id 写死 BookId 合理吗？想让 Repo 真正通用该怎么改？
# （提示：第二个 TypeVar，或用一个带 id 属性的 Protocol 约束 T）
# 不合理；给 bid 也用泛型


# e) Protocol 导出器（第 6 节）
class Exporter(Protocol):
    def export(self, books: list[Book]) -> str: ...


class JsonExporter:
    def export(self, books: list[Book]) -> str:
        return json.dumps([b.model_dump(mode="json") for b in books], ensure_ascii=False, indent=2)


class TextExporter:
    def export(self, books: list[Book]) -> str:
        return "\n".join(f"[{b.id}] {b.title} 库存：{b.stock} 状态：{b.status}" for b in books)


def publish(exporter: Exporter, books: list[Book]) -> None:
    print(exporter.export(books))


# f) 业务逻辑（第 4、13 节）
class Library(BaseModel):
    books: list[Book] = []

    def borrow(self, bid: BookId) -> Book:
        for b in self.books:
            if b.id == bid and b.stock > 0:
                b.status = "borrowed"
                b.stock -= 1
                b.borrowed_at = datetime.now()
                return b
        raise ValueError("借阅书籍不存在")

    def return_book(self, bid: BookId, rule: FineRule | None = None) -> float:
        for b in self.books:
            if b.id == bid:
                b.status = "available"
                b.stock += 1
                date = b.borrowed_at
                b.borrowed_at = None
                if date is None:  # 这个解决的是 mypy 不知道 date 是不是 None
                    return 0.0
                delta = datetime.now() - date
                if delta > timedelta(days=MAX_BORROW_DAYS):
                    if not rule:
                        return (delta.days - MAX_BORROW_DAYS) * 0.5
                    return rule(delta.days - MAX_BORROW_DAYS)
                return 0.0
        raise ValueError("书籍未找到")

    def save(self, path: Path) -> None:
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Library":
        if not path.exists():
            return cls()
        return cls.model_validate_json(path.read_text(encoding="utf-8"))


# g) 主流程（if __name__ == "__main__":）
if __name__ == "__main__":
    rbs: list[RawBook] = [
        {"id": 1, "isbn": "101", "stock": 5, "title": "python"},
        {"id": 2, "isbn": "102", "stock": 6, "title": "java"},
        {"id": 3, "isbn": "103", "stock": 7, "title": "c++"},
    ]

    bs: list[Book] = [Book.from_raw(rb) for rb in rbs]
    repo: Repo[Book] = Repo()
    for item in bs:
        repo.add(item)

    lib = Library(books=bs)

    # 1) 借两本（要还两本，得先借出来两本）
    lib.borrow(1)
    lib.borrow(2)

    # 2) 模拟逾期：把借出时间往前拨，否则刚借的书永远不到 30 天
    for b in lib.books:
        if b.id == 1:
            b.borrowed_at = datetime.now() - timedelta(days=40)  # 逾期 10 天
        if b.id == 2:
            b.borrowed_at = datetime.now() - timedelta(days=35)  # 逾期 5 天

    fine_default = lib.return_book(1)  # 默认：逾期每天 0.5 元
    fine_custom = lib.return_book(2, rule=lambda days: days * 2.0)  # 自定义：逾期每天 2 元
    print(f"默认罚金：{fine_default}（预期 5.0）")
    print(f"自定义罚金：{fine_custom}（预期 10.0）")

    # 3) 两种导出器
    publish(JsonExporter(), lib.books)
    publish(TextExporter(), lib.books)

    # 4) 存读一致性
    db = Path(__file__).parent / "library.json"
    lib.save(db)
    lib2 = Library.load(db)
    assert lib == lib2, "存读结果不一致"
    print("存读一致 ✓")

    # 5) 非法数据：title 全空格 / borrowed 但无借出时间 / stock=-1
    try:
        Book(id=4, title="   ", isbn="104", stock=-1, status="borrowed", borrowed_at=None)
    except ValidationError as e:
        print(f"一次报出 {e.error_count()} 个错误")
        print(e)
