# 不仅 Threading多线程 有Queue，asynico异步协程 也有Queue

import asyncio, random

async def producer(q: asyncio.Queue):
    for i in range(5):
        await asyncio.sleep(random.random())        # 模拟生产时间
        await q.put(i)
        print(f"生产 {i}")
    await q.put(None)           # 哨兵：通知消费者生产结束

async def consumer(q: asyncio.Queue):
    while True:
        item = await q.get()
        if item is None:
            break
        await asyncio.sleep(0.5)        # 模拟消费时间
        print(f"消费 {item}")

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main())