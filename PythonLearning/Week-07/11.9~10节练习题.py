# 并发抓取网页
# 用 aiohttp + asyncio.gather 实现：
# 并发请求 10 个 URL；
# 复用同一个 aiohttp.ClientSession；
# 每个请求返回状态码和响应长度；
# 输出成功响应数量、每个 URL 的结果、总耗时；
# 使用 time.perf_counter() 计时；
# 必须使用 async with session.get(...) 和 await r.text()。
# 可以使用 http://httpbin.org/delay/1；如果网络不可用，可以用 asyncio.sleep 模拟请求。
import asyncio, aiohttp, time

async def fetch(session, url):
    async with session.get(url) as se:
        status = se.status          # 状态码
        text = await se.text()            # 读取响应内容
        return (status, len(text))

async def main():
    urls = ["http://httpbin.org/delay/1"] * 10
    async with aiohttp.ClientSession() as cs:
        result = await asyncio.gather(*(fetch(cs, u) for u in urls))
    print(f"拿到 {len(result)} 个响应结果")
    print(result)

t = time.perf_counter()
asyncio.run(main())
print(f"耗时：{time.perf_counter() - t:.4f}s")