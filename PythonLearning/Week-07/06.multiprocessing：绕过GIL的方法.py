# 前面学习了面向 IO密集型 任务的 threading，今天开始学习面向 CPU密集型 的 multiprocessing
# multiprocessing 启动真正的子进程，每个进程有自己的解释器和GIL，这样可以利用
# 到 CPU 的多核

from multiprocessing import Pool
import time

def cpu_work(n):
    return sum(i*i for i in range(n))       # 可以看出这是个 CPU密集 任务

if __name__ == "__main__":          # Windows/Mac必须有这一行
    nums = [10_000_000] * 4
    t = time.time()
    with Pool(4) as p:              # 创建4个进程的进程池
        result = p.map(cpu_work, nums)      # 这里的map与内置的map不同，这里的map是真正计算，而内置的是创建迭代器对象
    print(f"{time.time() - t:.4f}s")          # 比单进程约快4倍
    # 单进程对比
    t1 = time.time()
    result = list(map(cpu_work, [10_000_000] * 4))
    print(f"{time.time() - t1:.4f}s")

# 注意：进程间的通信比线程贵得多（要序列化），不要给小任务开一堆进程


# 练习：CPU 密集任务
# 串行：对 4 个 n = 5_000_000 计算 sum(i * i for i in range(n))，记录耗时；
# 并行：用 multiprocessing.Pool(4) 执行同样的 4 个任务，记录耗时；
# 输出加速比，并保证串行和并行执行的任务数量一致；
# 必须使用 if __name__ == "__main__":。
if __name__ == "__main__":
    t2 = time.time()
    r1 = list(map(cpu_work, [5_000_000] * 4))
    consume1 = time.time() - t2
    print(f"{consume1:.4f}s")   
    t3 = time.time()
    with Pool(4) as p:
        p.map(cpu_work, [5_000_000] * 4)
    consume2 = time.time() - t3
    print(f"{consume2:.4f}s")
    print(f"加速比：{consume1 / consume2:.4f}")