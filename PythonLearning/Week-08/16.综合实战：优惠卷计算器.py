from collections.abc import Callable
from typing import Final, Literal, TypeVar

from pydantic import BaseModel, Field, field_validator, model_validator

# a) 别名 + 常量（第 4、9 节）
type Money = float
MAX_PERCENT: Final = 100


# b) Pydantic 优惠券（第 12、14 节）
class Coupon(BaseModel):
    code: str = Field(min_length=4, max_length=10)
    kind: Literal["percent", "cash"]
    value: float = Field(gt=0)

    @field_validator("code")
    @classmethod
    def code_strip_up(cls, v: str) -> str:
        return v.strip().upper()

    @model_validator(mode="after")
    def check_kind(self) -> "Coupon":
        if self.kind == "percent" and self.value > MAX_PERCENT:
            raise ValueError(f"金额：{self.value}不能超过最高折扣：{MAX_PERCENT}")
        return self


# c) 泛型 + Callable（第 4、5 节）
T = TypeVar("T")


def pick_best(items: list[T], key: Callable[[T], float]) -> T | None:
    if not items:
        return None
    return min(items, key=key)


# d) 算价（第 4 节）
def apply(coupon: Coupon, price: Money) -> Money:
    if coupon.kind == "percent":
        return price * (100 - coupon.value) * 0.01
    total = price - coupon.value
    if total < 0:
        return 0
    return total


# e) 主流程
# 构造三张券：" save20 " percent/20、"CASH5" cash/5、
# 以及一张非法的 percent/150（except ValidationError 捕获打印）
# 用 pick_best + lambda 选出「对 100 元商品最划算」的券（key是最优惠价格）
# 打印选中券的 code 和最终价
if __name__ == "__main__":
    coupons = [
        Coupon(code=" save20 ", kind="percent", value=20.0),
        Coupon(code="CASH5", kind="cash", value=5.0),
    ]

    try:
        Coupon(code="error", kind="percent", value=150.0)
    except Exception as e:
        print(e)

    pc: Coupon = pick_best(coupons, key=lambda c: apply(c, 100))
    total: float = apply(pc, 100)
    print(f"卷：{pc}, 总价：{total}")
