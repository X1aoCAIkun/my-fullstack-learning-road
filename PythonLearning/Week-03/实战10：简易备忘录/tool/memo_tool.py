from pathlib import Path
import json


# 初始化memo文件数据，文件不存在时创建文件，在文件中新建空列表
def init_memo_file(file_path: Path):
    if not file_path.exists():
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

# 新增备忘录
def add_memo(file_path: Path, title: str, content: str):
    # 读取备忘录数据
    with open(file_path, "r", encoding="utf-8") as f:
        memo_list = json.load(f)
    if not memo_list:
        new_id = 1    
    else:
        new_id = memo_list[-1]["id"] + 1
    memo_list.append({"id": new_id, "title": title, "content": content, "done": False})
    # 新增备忘录后保存数据
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(memo_list, f, ensure_ascii=False, indent=2)
    print("添加完成")
    

# 标记已完成项目
def mark_done(file_path ,id: int):
    with open(file_path, "r", encoding="utf-8") as f:
        memo_list = json.load(f)
    # 遍历备忘录找到对应id
    for memo in memo_list:
        if memo["id"] == id:
            memo["done"] = True
            break
    # 保存备忘录更新状态
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(memo_list, f, ensure_ascii=False, indent=2)

# 输出未完成的项目条目，并以txt文件形式输出
def export_undone(file_path: Path, export_txt: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        memo_list = json.load(f)
    # 用列表推导式得到未完成项目列表
    undone_list = [memo for memo in memo_list if not memo["done"]]
    # 将undone_list转换成txt
    lines = []
    for item in undone_list:
        line = f"id:{item["id"]} 标题:{item["title"]} 内容:{item["content"]}"
        lines.append(line)
    # 每条项目后换行处理
    content_txt = "\n".join(lines)    
    with open(export_txt, "w", encoding="utf-8") as f:
        f.write(content_txt)


# 自测
if __name__ == "__main__":
    BASE = Path(__file__).parent
    MEMO = BASE / "memo.json"
    EXPORT =BASE / "export.txt"
    init_memo_file(MEMO)
    add_memo(MEMO, "复习Python", "复习json和pathlib")
    add_memo(MEMO, "写实验报告", "完成实战10代码")
    mark_done(MEMO, 1)
    export_undone(MEMO, EXPORT)
    print("自测完成")