# 菜单的读取与保存（Part 3 考点：JSON 序列化与反序列化）
import json
from pathlib import Path
from .models import Dish, Category

# 把 json 里的分类字符串映射成 Category 枚举
CATEGORY_MAP = {c.value: c for c in Category}

BASE = Path(__file__).parent.parent
MENU = BASE / "menu.json"


# 加载菜单：json → {"菜名": Dish对象}
def load_menu(file_path: Path = MENU):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    menu = {}
    for name, info in data.items():
        category = CATEGORY_MAP.get(info.get("category", ""), "")
        menu[name] = Dish(name, info["price"], info["tags"], category)
    return menu


# 交互式添加一道菜（扩展功能）
def add_dish(menu):
    name = input("菜名：").strip()
    if name in menu:
        print(f"{name} 已在菜单里")
        return
    while True:
        price_str = input("价格：").strip()
        if price_str.isdigit():
            price = int(price_str)
            break
        print("价格必须是数字，请重新输入")
    tags = input("口味标签（用空格分隔，如：辣 招牌）：").split()
    category_str = input("分类（辣/甜/素）：").strip()
    menu[name] = Dish(name, price, tags, CATEGORY_MAP.get(category_str, category_str))
    print(f"已添加：{menu[name]}")


# 把菜单写回 json（枚举要转回字符串，json 不认识枚举）
def save_menu(menu, file_path: Path = MENU):
    data = {}
    for name, dish in menu.items():
        category = dish.category.value if isinstance(dish.category, Category) else dish.category
        data[name] = {"price": dish.price, "tags": dish.tags, "category": category}
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
