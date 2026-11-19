# 生成器除了可以"吐"东西，还能"接"东西

def echo():
    while True:
        msg = yield     # yield 表达式：右边是吐出来的值，"接"的是 send() 送进来的
        print(f"收到：{msg}")

g = echo()
next(g)         # 先启动生成器才会到第一个 yield
g.send("hi")
g.send("hello")
g.close()       # 关闭生成器

# 这些是协程的雏形。Python后来用 async/await 替代了它（第七周学），但学会
# 老代码对理解新代码很有作用