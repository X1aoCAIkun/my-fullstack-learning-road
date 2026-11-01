# 生成器就好像一个集成好的迭代器，联想到之前的列表推导式，生成器也有表达式
# 把列表推导式的 [] 换成 () 就是生成器表达式

# 列表推导式
squares_list = [x*x for x in range(10_000_000)]
# 这里会立即算10000000个数，吃几十MB内存

# 生成器推导式
squares_gen = (x*x for x in range(10_000_00))
# 这里只生成了一个生成器（一种迭代器），什么都没算

print(sum(squares_gen))         # 一个一个算，内存恒定

# 注意：当只需要 一遍for 做求和、最大值、连接，永远优先用生成器表达式

# 练习：读一个 1GB 的 CSV，统计第 3 列数字之和，内存不能超过 100MB
def col3_nums(path):
    with open(path, encoding="utf-8") as f:
        next(f)         # 跳过表头
        for line in f:          # 文件对象本身就是迭代器，一行一行读
            yield float(line.split(",")[2])

print(sum(col3_nums("big.csv")))            # 整个过程只占一行内存

# 解析：open()返回的文件对象就是一个迭代器
