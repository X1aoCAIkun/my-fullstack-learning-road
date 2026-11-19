# 理解这个标题，用个类比
# 餐厅老板雇一个超能服务员（事件循环）。每次客人点完菜，他不站着等菜出锅
# 而是立刻去招呼下一桌。菜好了厨师按铃他再回来端。一个人服务50桌就是 asynico
"""
关键概念
事件循环event loop           那个“超能服务员”，调度的所有协程
协程 coroutine               用 async def 定义的函数
await                        “我要等IO，先暂停，让别人先跑”
Task                         把协程包成“可调度的”对象
"""

# 第一个异步程序
import asyncio

async def hello(name, delay):       # 调用协程函数时不会立刻执行代码，而是产生一个协程对象
    print(f"{name} 开始")
    await asyncio.sleep(delay)          # 让出控制权给事件循环
    print(f"{name} 结束")

async def main():
    await asyncio.gather(                   # 同时跑多个协程，交给事件循环进行并发调度 
        hello("A", 1),
        hello("B", 2),
        hello("C", 1),
    )         

asyncio.run(main())      # 启动异步协程
# A 开始
# B 开始
# C 开始
# A 结束
# C 结束
# B 结束            可以看到开始时是按顺序，结束则是按完成的顺序，且耗时一般与最长的那个协程差不多


# async（异步）/sync（同步      ）不能直接混
async def fetch():
    import time
    # time.sleep(3)               # 错！这是同步堵塞，整个事件循环（所有协程）堵死3秒
    await asyncio.sleep(3)          # 对！这才是异步等待，单个协程等待，不影响其他协程