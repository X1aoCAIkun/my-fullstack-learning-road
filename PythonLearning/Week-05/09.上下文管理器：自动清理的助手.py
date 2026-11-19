# 上下文管理器就是在使用完某项功能后，它会自动关闭
# 就好像酒店的退房系统--入住（使用功能）->退房，屋内设施停止（结束功能使用）


# 比如with就是如此
from pathlib import Path
BASE = Path(__file__).parent
TXT = BASE / "a.txt"

with open(TXT, "w", encoding="utf-8") as f:
    f.write("hi")
# 如果离开了with块，无论是否报错，文件f都会关闭


# 自定义：实现__enter__/__exit__，自己定义清理出入口
class Timer:
    def __enter__(self):          # 进入with时就会执行，将返回值交给as  
        import time
        self.start = time.perf_counter()
        return self                 # 这就相当于文件操作里 as 后的f

    def __exit__(self, exc_type, exc, tb):      # 离开with块时执行，3个参数是就收异常信息
        import time
        self.cost = time.perf_counter() - self.start
        print(f"耗时{self.cost:.4f}s")
        # return True           # return True会吞掉异常，谨慎使用

with Timer() as t:
    sum(range(10_000_000))