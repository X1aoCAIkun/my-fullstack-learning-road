# 你要实现一个批处理程序，分别处理 CPU 密集任务和 I/O 密集任务，并比较串行、线程池、进程池的耗时。

import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

CPU_NUMS = [3_000_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000, 8_000_000]
IO_IDS = list(range(12))

def cpu_task(n):
    return sum(i * i for i in range(n))

def io_task(task_id):
    time.sleep(0.3 + (task_id % 4) * 0.2)
    return task_id

# 要求：
# CPU 并行使用 multiprocessing.Pool(3)。
# I/O 线程池使用 ThreadPoolExecutor(max_workers=4)。
# I/O 进程池使用 ProcessPoolExecutor(max_workers=4)。
# 所有函数只返回结果，不要在函数内部打印耗时。
# 串行、并行必须使用同一份输入数据。
# 使用 if __name__ == "__main__": 保护程序入口。

def run_serial_cpu(nums):
    """串行执行 cpu_task，返回结果列表"""
    res1 = list(map(cpu_task, nums))
    return res1

def run_pool_cpu(nums, workers):
    """用 multiprocessing.Pool 执行 cpu_task，返回结果列表"""
    with Pool(3) as p:
        res2 = p.map(workers, nums)
    return res2

def run_serial_io(task_ids):
    """串行执行 io_task，返回结果列表"""
    res3 = list(map(io_task, task_ids))
    return res3

def run_thread_io(task_ids, workers):
    """用 ThreadPoolExecutor 执行 io_task，返回结果列表"""
    with ThreadPoolExecutor(max_workers=4) as th:
        res4 = list(th.map(workers, task_ids))
    return res4

def run_process_io(task_ids, workers):
    """用 ProcessPoolExecutor 执行 io_task，返回结果列表"""
    with ProcessPoolExecutor(max_workers=4) as pr:
        res5 = list(pr.map(workers, task_ids))
    return res5

def main():
    s1 = time.perf_counter()
    res1 = run_serial_cpu(CPU_NUMS)
    consume1 = time.perf_counter() - s1
    print(f"CPU 串行：{consume1:.4f}s")

    s2 = time.perf_counter()
    res2 = run_pool_cpu(CPU_NUMS, cpu_task)
    consume2 = time.perf_counter() - s2
    print(f"CPU 进程池：{consume2:.4f}s，加速比{consume1/consume2:.2f}")

    s3 = time.perf_counter()
    res3 = run_serial_io(IO_IDS)
    consume3 = time.perf_counter() - s3
    print(f"I/O 串行：{consume3:.4f}s")

    s4 = time.perf_counter()
    res4 = run_process_io(IO_IDS, io_task)
    consume4 = time.perf_counter() - s4
    print(f"I/O 进程池：{consume4:.4f}s")

    s5 = time.perf_counter()
    res5 = run_thread_io(IO_IDS, io_task)
    consume5 = time.perf_counter() - s5
    print(f"I/O 线程池：{consume5:.4f}s")

    assert res1 == res2
    assert res3 == res4 == res5

if __name__ == "__main__":
    main()