# mypy 除了可以在编码时动态检查，也可以使用静态类型检查

def add(a: int, b: int) -> int:
    return a + b

# print(add("1", 2))   # mypy 报错  