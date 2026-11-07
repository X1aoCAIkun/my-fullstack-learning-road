from contextlib import contextmanager
import time


# yield会将函数分成两部分，之前未__enter__部分，之后为__exit__部分
@contextmanager
def timer(label="任务"):
    start = time.perf_counter()
    try:
        yield           # yield之前是enter，之后是exit
    finally:
        print(f"{label} 耗时 {time.perf_counter() - start:.4f}s")

with timer("求和"):
    sum(range(10_000_000))