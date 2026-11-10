import asyncio, aiohttp, time


async def fetch(session, url):
    async with session.get(url) as r:
        return await r.text()

async def main():
    url = [f"http://httpbin.org/delay/1" for _ in range(10)] 
    async with aiohttp.ClientSession() as s:
        result = await asyncio.gather(*(fetch(s, u) for u in url))
    print("拿到", len(result), "个响应")

t = time.time()
asyncio.run(main())
print("耗时", time.time() - t)          # 约一秒，10个请求并发
# 如果 requests 同步抓，要10秒P