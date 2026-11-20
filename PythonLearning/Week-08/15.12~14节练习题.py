# Week-08 第 12~14 节编程练习：个人记账本
# 要求：全程用 Pydantic v2，写完跑两遍验收：
#   python3 "Week-08/15.12~14节练习题.py"
#   mypy "Week-08/15.12~14节练习题.py"
#
# 背景：13 节用 Task/TaskList 重构了 todo，这次你自己从零写一个记账本，
#       不许翻 13 节抄，写完了再对照。

from datetime import datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

# ============================================================
# a) 定义 Expense(BaseModel)：一笔支出
#    id: int
#    amount: float          金额，必须 > 0 且 <= 100000（用 Field 约束）
#    category: Literal["food", "transport", "study", "other"]
#    note: str              备注，最长 50 字符，默认 ""
#    created_at: datetime   默认当前时间（提示：default_factory）
# ============================================================

# ============================================================
# b) 给 note 加 field_validator：去掉首尾空格
#    验收：Expense(..., note="  午饭  ") 存进去后 note == "午饭"
# ============================================================

# ============================================================
# c) 给 Expense 加字段 discount: float，默认 0，约束 >= 0
#    再加 model_validator(mode="after")：discount 不能大于 amount
#    （提示：14 节的 due/created_at 校验同款写法；
#      想一想为什么这个校验不能用 field_validator 做？）
#    验收：amount=10, discount=20 时必须抛 ValidationError
# ============================================================

# ============================================================
# d) 定义 ExpenseBook(BaseModel)：expenses: list[Expense] = []
#    实现三个方法：
#    add(amount: float, category: ..., note: str = "") -> Expense
#        id 自动取现有最大 id + 1（空本子从 1 开始）
#    total() -> float
#        所有支出的「实付」合计（amount - discount）
#    by_category(category: ...) -> list[Expense]
#        筛选某一类支出
# ============================================================

# ============================================================
# e) 给 ExpenseBook 加 save(path: Path) 和 load(path: Path)
#    和 13 节一样：存 JSON（indent=2, utf-8），文件不存在时 load 返回空本子
#    验收：save 之后再 load，model_dump() 的结果和原来完全一致
#    （想一想：datetime 存进 JSON 再读回来，还能对上吗？）
# ============================================================

# ============================================================
# f) 主流程（if __name__ == "__main__":）
#    1. load 同目录下的 expenses.json
#    2. 记三笔：午饭 25.5 food / 地铁 4 transport discount=1 / 买书 89 study
#    3. 打印 total() 和 by_category("food")
#    4. save 回 expenses.json
#    5. 用 try/except ValidationError 故意构造一笔非法支出
#       （amount=-5, category="game", discount 超额），打印错误信息，
#       数一数 pydantic 一次报出了几个错
# ============================================================


class Expense(BaseModel):
    id: int
    amount: float = Field(gt=0, le=100000)
    category: Literal["food", "transport", "study", "other"]
    note: str = Field(max_length=50, default="")
    created_at: datetime = Field(default_factory=datetime.now)
    discount: float = Field(ge=0, default=0)

    @model_validator(mode="after")
    def discount_check(self) -> "Expense":
        if self.discount > self.amount:
            raise ValueError(f"折扣金额：{self.discount}不能大于应付金额：{self.amount}")
        return self

    @field_validator("note")
    @classmethod
    def note_strip(cls, v: str) -> str:
        return v.strip()


class ExpenseList(BaseModel):
    expense: list[Expense] = []

    def add(
        self,
        amount: float,
        category: Literal["food", "transport", "study", "other"],
        note: str = "",
        discount: float = 0,
    ) -> "Expense":
        new_id = max((e.id for e in self.expense), default=0) + 1
        e = Expense(id=new_id, amount=amount, category=category, note=note, discount=discount)
        self.expense.append(e)
        return e

    def total(self) -> float:
        consume: float = 0
        for e in self.expense:
            consume += e.amount - e.discount
        return consume

    def by_category(
        self, category: Literal["food", "transport", "study", "other"]
    ) -> list[Expense]:
        bc: list[Expense] = []
        for e in self.expense:
            if e.category == category:
                bc.append(e)
        return bc

    def save(self, path: Path) -> None:
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "ExpenseList":
        if not path.exists():
            return cls()
        return cls.model_validate_json(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    path = Path(__file__).parent / "expenses.json"
    ex = ExpenseList.load(path)
    ex.add(25.5, "food", " 午饭 ")
    ex.add(4.0, "transport", "地铁", discount=1)
    ex.add(89.0, "study", "买书")
    print(ex.total())
    print(ex.by_category("food"))
    ex.save(path)
    try:
        ex.add(amount=-5, category="food", discount=10)
    except ValidationError as e:
        print(e)
