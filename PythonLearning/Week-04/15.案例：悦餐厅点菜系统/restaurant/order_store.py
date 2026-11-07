# 订单文件的读写（Part 3 考点：pathlib + with open）
from datetime import datetime
from pathlib import Path

ORDERS_DIR = Path(__file__).parent.parent / "orders"
ORDER_FILE = ORDERS_DIR / "订单记录.txt"


# 结算成功后追加一条订单（orders 目录不存在会自动创建）
def save_order(name, items, total, phone):
    ORDERS_DIR.mkdir(exist_ok=True)
    dishes = "、".join(f"{item.dish.name}x{item.count}" for item in items)
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {name} | {phone} | {dishes} | 共 {total:.2f} 元\n"
    with open(ORDER_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# 查看订单记录：文件不存在时提示而不是报错
def show_orders():
    if not ORDER_FILE.exists():
        print("暂无订单记录")
        return
    with open(ORDER_FILE, "r", encoding="utf-8") as f:
        print(f.read())
