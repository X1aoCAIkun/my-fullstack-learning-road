from contextlib import contextmanager


class FakeDB:
    def __init__(self):
        self.connected = False
    def connect(self):
        self.connected = True
        print("DB 连接")
    def close(self):
        self.connected = False
        print("DB 关闭")
    def query(self, sql):
        print("执行：", sql)

@contextmanager
def de_session():
    db = FakeDB()
    db.connect()
    try:
        yield db
    finally:
        db.close()

with de_session() as db:
    db.query("SELECT * FROM users")
    # raise RuntimeError("故意出错")        # 即使报错也会执行finally