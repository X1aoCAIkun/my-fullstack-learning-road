from pathlib import Path
from tool import memo_tool


BASE = Path(__file__).parent
MEMO = BASE / "memo.json"
EXPORT =BASE / "export.txt"
memo_tool.init_memo_file(MEMO)
memo_tool.add_memo(MEMO, "复习Python", "复习json和pathlib")
memo_tool.add_memo(MEMO, "写实验报告", "完成实战10代码")
memo_tool.mark_done(MEMO, 1)
memo_tool.export_undone(MEMO, EXPORT)