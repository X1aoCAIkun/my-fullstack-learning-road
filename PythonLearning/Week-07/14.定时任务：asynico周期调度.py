import asyncio, datetime


async def heartbeat():
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(1)          # 每 1 秒执行一次

async def main():
    # 把 heartbeat 包装成后台任务，立刻开始并发运行
    task = asyncio.create_task(heartbeat())
    await asyncio.sleep(5)          # 跑 5 秒  main自己休眠5秒而 heartbeat 一直在跑
    task.cancel()           # 取消任务

asyncio.run(main())