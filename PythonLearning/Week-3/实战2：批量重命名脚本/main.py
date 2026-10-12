from pathlib import Path

folder = Path("photo")          # 创建文件路径

# 遍历photo文件夹下文件夹的.jpg文件，拿到索引与元素，从索引1开始
for i, f in enumerate(sorted(folder.glob("*.jpg")), 1):
    new = folder / f"photo_{i:03d}.jpg"
    f.rename(new)
    print(f"{f.name} -> {new.name}")

# 注意：这里的f.name和new.name不是同一个值，因为f.rename(new)修改的时
# 硬盘上的文件名字，而f现在在内存上，所以f.name还是原来的名字