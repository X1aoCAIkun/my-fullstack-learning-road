from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    email: str

u: User = {"id": 1, "name": "Alice", "email": "@qq.com"}
bad: User = {"id": 2, "name": "Tom", "email": "@qq.com"}         # mypy 会报错
# 注意：这里创建的对象，需要包含所有键，否则 mypy 也会报错
# 但也可以在 User 的继承里加个参数 total = False 这样键不全也不会报错

# 适合处理 JSON / API 响应