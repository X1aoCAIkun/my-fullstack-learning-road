from pathlib import Path
from tools import score_tool


BASE = Path(__file__).parent
STUDENT = BASE / "student.json"

stu_list = score_tool.load_student_data(STUDENT)
print(stu_list)

# 当文件不存在时添加数据
if not stu_list:
    stu_list.extend([{"name": "小明", "score": 70}, {"name":"小红", "score": 79}, {"name":"小刚", "score": 81}])

print(score_tool.calc_score_stat(stu_list))
score_tool.save_student_data(stu_list, STUDENT)