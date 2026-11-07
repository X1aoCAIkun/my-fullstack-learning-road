from contextlib import contextmanager
from pathlib import Path


# 用contextmanager装饰后就由yield分割__enter__和__exit__
@contextmanager
def safe_write(path, encoding="utf-8"):
    """写入临时文件，成功才rename - 防止半截文件覆盖原文件"""
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")  # 创建临时文件，后缀为.json.tmp
    f = tmp.open("w", encoding=encoding)
    try:
        yield f
        f.close()
        tmp.replace(path)           # 原子替换（操作要么全部成功，要么完全不生效）
    except Exception:
        f.close()
        tmp.unlink(missing_ok=True)         # 删除临时文件，即使tmp不存在
        raise       # 重新抛出异常，防止except之后，外层看不到异常 

with safe_write("config.json") as f:
    f.write('{"debug": true}')