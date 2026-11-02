def unique_lines(path):
    seen = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")        # 删除行右边（行尾）的换行符
            if line not in seen:
                seen.add(line)
                yield line

# 用法（边读边写，全程内存恒定），一个空文件写入，一个原始文件
with open("dedup.txt", "w", encoding="utf-8") as out:
    for line in unique_lines("big.log"):
        out.write(line + "\n")