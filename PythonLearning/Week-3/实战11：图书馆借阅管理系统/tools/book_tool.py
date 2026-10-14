import json
from pathlib import Path

# 初始化文件
def init_book_file(file_path: Path):
    if not file_path.exists():
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({"books": [], "records": []}, f, ensure_ascii=False, indent=2)
    else:
        return

# 添加书籍
def add_book(file_path: Path, name: str, author: str, stock: int):
    # 读取json文件数据
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    book_list = data["books"]
    # book_list为空则添加起始id:1，存在则id为最大id加1
    if not book_list:
        new_book_id = 1
    else:
        new_book_id = book_list[-1]["book_id"]
    book_list.append({"book_id": new_book_id, "name": name, "author": author, "stock": stock})

   # 将更新记录添加到json文件
    data["books"] = book_list
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 借阅操作(可以一次借阅多本书籍)
def borrow_operation(file_path: Path, stu_name: str, borrow_id_list: list, borrow_date: str):
    # 读取json文件数据
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    book_list = data["books"]
    record_list = data["records"]
    # 只有匹配到对应id且库存大0才可以借阅
    for id in borrow_id_list:
        for item in book_list:
            if id == item["book_id"] and item["stock"] > 0:
                # record_list为空则添加起始id:1，存在则id为最大id加1
                if not record_list:
                    new_record_id = 1
                else:
                    new_record_id = record_list[-1]["record_id"]
                record_list.append({"record_id": new_record_id, "stu_name": stu_name, "borrow_books_id": borrow_id_list, "borrow_date": borrow_date})
                item["stock"] -= 1
    # 保存数据
    new_data = {"books": book_list, "records": record_list}
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

# 以txt文件形式输出低库存书籍信息
def export_low_stock(file_path: Path, out_txt: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    book_list = data["books"]
    lines =[]
    # 读取库存小于等于1的书籍信息，拼接成文本，并保存在文件中
    for book in book_list:
        if book["stock"] <= 1:
           line = f"图书id:{book["book_id"]} 书名:{book["name"]} 作者:{book["author"]} 剩余库存:{book["stock"]}"
           lines.append(line)
    content_txt = "\n".join(lines)
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(content_txt)
    
