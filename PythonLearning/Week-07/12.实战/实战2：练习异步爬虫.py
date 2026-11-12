# 写一个异步爬虫：抓 http://httpbin.ceshiren.com/uuid 共 50 次，
# 最多 10 个并发，计时。

import asyncio, time, aiohttp


async def fetch(sem, session, url):
    async with sem:
        async with session.get(url) as se:
            return await se.text()

async def main():
    sem = asyncio.Semaphore(10)
    url = ["http://httpbin.ceshiren.com/uuid"] * 50
    async with aiohttp.ClientSession() as cs:
        result = await asyncio.gather(*(fetch(sem, cs, u) for u in url))
    print(f"拿到 {len(result)} 个响应")

t = time.perf_counter()
asyncio.run(main())
print(f"耗时：{time.perf_counter() - t:.4f}s")

# Semaphore(10) 像个10张通行证的口子，没拿到证就await等待