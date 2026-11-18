# 对于一些复杂的类型名称，为了减少编码时间，可以为这些类型起别名

type UserId = int       # Python 3.12+ 新语法，这里是给 int 起了别名 UerId
type Vector = list[float]
type JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


def add_one(uid: UserId) -> UserId:
    return uid + 1