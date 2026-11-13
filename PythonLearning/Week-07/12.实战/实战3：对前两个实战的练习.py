# Q1：信号量限流爬虫
import asyncio, aiohttp, time

async def fetch(sem, session, url):
    try:
        async with sem:
            async with session.get(url) as se:
                status = se.status
                text = await se.text()
                return (status, len(text))
    except Exception as e:
        return (None, type(e).__name__)

async def main1():
    URL1 = ["http://httpbin.ceshiren.com/uuid"] * 30
    sem = asyncio.Semaphore(8)
    start = time.perf_counter()
    async with aiohttp.ClientSession() as cs:
        result = await asyncio.gather(*(fetch(sem, cs, u) for u in URL1))
    consume1 = time.perf_counter() - start
    success_count = 0
    fault = []
    for res in result:
        if res[0] is not None and 200 <= res[0] < 300:
            success_count += 1
        else:
            fault.append(res)
    return consume1, success_count, fault


consume1, success_count, fault = asyncio.run(main1())
print(f"总耗时：{consume1:.4f}s, 成功数：{success_count}/失败项：{fault}")


# Q2：三种方式同台对比
import requests
from concurrent.futures import ThreadPoolExecutor

URL = ["http://httpbin.ceshiren.com/uuid"] * 10
HEADERS = {"User-Agent": "Mozilla/5.0"}

# 1.串行
def sync_run():
    t = time.perf_counter()
    [requests.get(u, headers=HEADERS) for u in URL]
    consume = time.perf_counter() - t
    print(f"同步串行耗时：{consume:.4f}s")
    return consume

# 2.多线程
def thread_run():
    t = time.perf_counter()
    with ThreadPoolExecutor(10) as th:
        list(th.map(lambda u: requests.get(u, headers=HEADERS), URL))
    consume = time.perf_counter() - t
    print(f"多线程耗时：{consume:.4f}s")
    return consume

# 3.异步协程
async def async_run():
    t = time.perf_counter()
    async with aiohttp.ClientSession(headers=HEADERS) as cs:
        await asyncio.gather(*(cs.get(u) for u in URL))
    consume = time.perf_counter() - t
    print(f"异步协程耗时：{consume:.4f}s")
    return consume

c1 = sync_run()
c2 = thread_run()
print(f"多线程加速比：{c1 / c2:.4f}")
c3 = asyncio.run(async_run())
print(f"异步协程加速比：{c1 / c3:.4f}")


# Q3：超时与错误兜底
async def fetch1(session, url):
    try:
        async with session.get(url) as se:
            status = se.status
            text = await se.text()
            return (url, status, len(text))
    except Exception as e:
        return (url, None, type(e).__name__)
    
async def main2():
    timeout = aiohttp.ClientTimeout(total=3)
    URL = ["http://httpbin.ceshiren.com/uuid"] * 18 + ["http://nonexist-abc123456.test"] * 2
    HEADERS = {"User-Agent": "Mozilla/5.0"}
    async with aiohttp.ClientSession(timeout=timeout, headers=HEADERS) as cs:
        result = await asyncio.gather(*(fetch1(cs, u) for u in URL))
    success_count = 0
    fault = []
    for res in result:
        if res[1] is not None and 200 <= res[1] < 300:
            success_count += 1
        else:
            fault.append(res)
    return success_count, fault

s, f = asyncio.run(main2())
print(f"成功数：{s}/失败数：{len(f)}, 失败类型：{f}")