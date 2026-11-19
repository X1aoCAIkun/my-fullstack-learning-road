# 对于一些基础的类型注解应该掌握

name: str = "Alice"
age : int = 18
height: float = 1.75
is_student: bool = True

scores: list[int] = [90, 80, 70]            # Python 3.9+ 版本可以直接用内置类型
profile: dict[str, str | int] = {"name": "Alice", "age": 18}
point: tuple[float, float] = (1.0, 2.0)

def greet(name: str, times: int = 1) -> None:
    for _ in range(times):
        print(f"hi {name}")

# 注意：Python 3.8及之前要 from typing import List, Dict, Tuple，写List[int]
# 3.9+ 及以上版本推荐用小写内置 list[int]