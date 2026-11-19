# 无论 threading 还是 multiprocessing 都太啰嗦了，concurrent.futures 给了
# 一个统一的接口

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch(url):
    import urllib.request     
    return len(urllib.request.urlopen(url).read())      # 访问网页，下载页面内容，并返回页面字节长度

url = ["http://wwww.example.com"] * 10

# IO 密集 -> 线程池
with ThreadPoolExecutor(max_workers=5) as ex:
    sizes = list(ex.map(fetch, url))
print(sizes)

# 只要把 ThreadPoolExecutor 切换到 ProcessPoolExecutor 就能切到多进程，接口一模一样

# 练习：I/O 密集任务
# 用 ThreadPoolExecutor(max_workers=5) 执行 10 个模拟下载任务；
# 每个任务用 time.sleep(0.5) 模拟网络等待；
# 记录总耗时，并解释为什么总耗时接近 1 秒而不是 5 秒；
# 把 ThreadPoolExecutor 换成 ProcessPoolExecutor，思考：会更快吗？为什么？
# 不会，因为下载任务依赖外部资源，属于 IO密集型
import time

def load(n):
    time.sleep(0.5)
    return n

s = time.time()
nums = [i for i in range(10)]
with ThreadPoolExecutor(max_workers=5) as th:
    process = list(th.map(load, nums))
print(f"{time.time() - s:.4f}s")