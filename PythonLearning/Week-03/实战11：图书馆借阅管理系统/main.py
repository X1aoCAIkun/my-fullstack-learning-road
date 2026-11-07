from pathlib import Path
from tools import book_tool


BASE = Path(__file__).parent
LIBRARY_DATA = BASE / "data.json"
EXPORT = BASE / "export.txt"

book_tool.init_book_file(LIBRARY_DATA)
book_tool.add_book( LIBRARY_DATA, "python程序设计", "张三", 2)
book_tool.add_book( LIBRARY_DATA, "计算机网络", "李四", 1)
book_tool.add_book( LIBRARY_DATA, "数据结构与算法", "王五", 3)
book_tool.add_book( LIBRARY_DATA, "操作系统原理", "赵六", 0)
book_tool.borrow_operation(LIBRARY_DATA, "小红", [1, 2, 4], "2026-10-14")
book_tool.export_low_stock(LIBRARY_DATA, EXPORT)