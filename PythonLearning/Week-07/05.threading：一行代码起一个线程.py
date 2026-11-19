import threading
import time

def worker(name):
    print(f"{name} 开始")
    time.sleep(1)           # 程序停止一秒，模拟IO操作
    print(f"{name} 结束")

# 创建线程对象，target是要执行的函数，args（是元组，所以有逗号）是传给函数的参数
t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))
t1.start(); t2.start()      # 同时启动，真正开启线程，并发跑，不是立刻执行，但是谁先跑由操作系统调度
t1.join(); t2.join()        # 等两个都跑完，t1和t2两个子线程跑完主线程才会执行
print("主线程退出")
# 注意：这里的耗时约为 1 秒，在t1进行模拟IO操作时，t2会跑；注意如果不加join
# 那么主线程就会在两个子线程sleep的时候跑完


# Lock：保护共享资源
counter = 0
lock = threading.Lock()

def add():
    global counter
    for _ in range(100_000):
        with lock:              # 进入临界区，其他线程等待
            counter += 1

threads = [threading.Thread(target=add) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)          # 1000000
# 不加锁的话，counter += 1 不是原子操作（读->加->写），多个线程会“踩脚”导致最终值小于100万


# Queue：线程安全的传话筒
import queue

q = queue.Queue()       # 自带锁，无需Lock

def producer():
    for i in range(5):
        q.put(i)        # 将数据放入队列
        print(f"生产 {i}")
        time.sleep(0.1)         # 给时间让子线程跑

def consumer():
    while True:
        item = q.get()      # 从队列中取出数据，没取到会堵塞等待，不会直接报错
        if item is None:        # 哨兵值，结束信号
            break
        print(f"消费 {item}")
        q.task_done()

# daemon是守护线程，主线程结束，consumer这个子线程会被强制收回，这里是给52~53行兜底
threading.Thread(target=consumer, daemon=True).start()
producer()
q.put(None)                 # 通知消费者结束，结束信号


# 练习1：7. 多线程下载模拟器
import random

def load(name):
    print(f"开始下载 {name}")
    time.sleep(random.randint(1, 3))
    print(f"{name} 下载完成")

s = time.perf_counter()
th = [threading.Thread(target=load, args=(i,)) for i in range(5)]
for t in th:
    t.start()
for t in th:
    t.join()
print(f"总耗时：{time.perf_counter() - s:.4f}s")
# 总耗时最接近最慢的那个任务，因为这个线程sleep了其他线程会趁机跑

# 练习2：. 双生产者-双消费者
q1 = queue.Queue()
total_lock = threading.Lock()

total = 0

def pro1():
    for i in range(5):
        q1.put(i)
        print(f"p1 生产 {i}")
        time.sleep(0.1)

def pro2():
    for i in range(5, 10):
        q1.put(i)
        print(f"p2 生产 {i}")
        time.sleep(0.1)

def con1():
    global total
    while True:
        try:
            item = q1.get()
            if item is None:
                break
            print(f"c1 消费 {item}")
            with total_lock:        # 给total加锁防止出现脏读数据
                total += item
        finally:
            q1.task_done()
def con2():
    global total
    while True:
        try:
            item = q1.get()
            if item is None:
                break
            print(f"c2 消费 {item}")
            with total_lock:
                total += item
        finally:
            q1.task_done()


c1 = threading.Thread(target=con1)
c2 = threading.Thread(target=con2)
p1 = threading.Thread(target=pro1)
p2 = threading.Thread(target=pro2)
c1.start(); c2.start()
p1.start(); p2.start()
p1.join(); p2.join()
q1.put(None)
q1.put(None)
c1.join(); c2.join()
print(f"总消费：{total}")