import asyncio, random, time

async def producer(name, q, orders):
    for order_id, cost in orders:
        await asyncio.sleep(random.uniform(0.1, 0.3))   # 模拟生产间隔
        await q.put((order_id, cost))                    # 队列满时自动等待（背压）
        print(f"[生产者{name}] 放入订单 {order_id}（处理耗时 {cost:.2f}s）")


async def worker(name, q, results):
    while True:
        item = await q.get()
        if item is None:                                 # 哨兵：退出
            break
        order_id, cost = item
        await asyncio.sleep(cost)                        # 模拟处理耗时
        results[name].append(order_id)
        print(f"[消费者{name}] 完成订单 {order_id}")
        q.task_done()


async def main():
    q = asyncio.Queue(maxsize=5)
    results = {f"C{i}": [] for i in range(1, 5)}

    # 3 个生产者 x 6 单 = 18 单，order_id 为 0~17
    orders = [[(i * 6 + j, random.uniform(0.2, 0.5)) for j in range(6)] for i in range(3)]

    workers = [asyncio.create_task(worker(f"C{i}", q, results)) for i in range(1, 5)]
    producers = [asyncio.create_task(producer(f"P{i + 1}", q, orders[i])) for i in range(3)]

    await asyncio.gather(*producers)     # 等所有订单都放进队列
    await q.join()                       # 等队列里所有任务被处理完
    for _ in workers:                    # 按消费者数量发哨兵
        await q.put(None)
    await asyncio.gather(*workers)       # 等消费者全部退出

    all_ids = [oid for ids in results.values() for oid in ids]
    assert len(all_ids) == 18, f"处理总数不对：{len(all_ids)}"
    assert sorted(all_ids) == list(range(18)), "有订单被漏掉或重复处理"

    print("\n各消费者处理数量：")
    for name, ids in results.items():
        print(f"  {name}: {len(ids)} 单")
    print(f"总计：{len(all_ids)} 单")

start = time.perf_counter()
asyncio.run(asyncio.wait_for(main(), timeout=30))
print(f"总耗时：{time.perf_counter() - start:.2f}s")
