# pathlib是用于文件读取的


from pathlib import Path

p = Path("data") / "users.txt"      # 跨平台拼接
print(p)                # data/users.txt

p.parent.mkdir(parents=True, exist_ok=True)   # 创建data目录
p.write_text("hello", encoding="utf-8")
print(p.read_text(encoding="utf-8"))        # "hello"

print(p.exists(), p.is_file(), p.suffix, p.stem)
# True True .txt users

# 遍历目录
for f in Path(".").glob("*.py"):
    print(f.name, f.stat().st_size)