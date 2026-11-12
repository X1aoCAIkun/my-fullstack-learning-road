# 这个实战将直观的对比不同方式处理 IO密集型 任务的速度

import time, requests, asyncio, aiohttp
from concurrent.futures import ThreadPoolExecutor

URLS = [f"https://movie.douban.com/top250?start={i*25}" for i in range(10)]        # 一页展示25部电影，共10页 
HEADERS = {"User-Agent": "Mozilla/5.0"}             # 请求头字典，伪装成浏览器（User-Agent），豆瓣网拒绝Python爬虫访问

# 1.同步
def sync_run():
    t =  time.time()
    [requests.get(u, headers=HEADERS) for u in URLS]        # 爬取结果
    print(f"同步耗时：{time.time() - t:.4f}s")

# 2.多线程
def thread_run():
    t = time.time()
    with ThreadPoolExecutor(10) as th:
        list(th.map(lambda u: requests.get(u, headers=HEADERS), URLS))
    print(f"多线程耗时：{time.time() - t:.4f}s")

# 3.异步
async def async_run():
    t = time.time()
    async with aiohttp.ClientSession(headers=HEADERS) as s:
        await asyncio.gather(*(s.get(u) for u in URLS))
    print(f"异步耗时：{time.time() - t:.4f}s")

sync_run()                      # 约3.39秒
thread_run()                    # 约0.93秒
asyncio.run(async_run())        # 约0.53秒
# 可以看到：同步耗时长很多，异步比多线程更快、更省内存（一个线程默认8MB的栈，1000个协程才几MB）