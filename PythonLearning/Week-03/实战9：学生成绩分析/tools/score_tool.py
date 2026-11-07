import json
from pathlib import Path

# 从文件加载数据
def load_student_data(file_path: Path):
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# 计算成绩统计，返回字典
def calc_score_stat(stu_list: list) -> dict:
    score_dict = {}
    scores = [stu["score"] for stu in stu_list]

    score_dict["总分"] = sum(scores)
    # 使用round()保留两位小数
    score_dict["平均分"] = round(sum(scores) / len(scores), 2)
    score_dict["最高分"] = max(scores)
    score_dict["最低分"] = min(scores)
    pass_count = [score for score in scores if score >= 60]
    score_dict["及格人数"] = len(pass_count)

    return score_dict

# 保存学生信息
def save_student_data(stu_list: list, file_path: Path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stu_list, f, ensure_ascii=False, indent=2)

# 模块自测
if __name__ == "__main__":
    BASE = Path(__file__).parent
    STUDENT = BASE / "student.json"
    data = load_student_data(STUDENT)
    if data:
        result = calc_score_stat(data)
        print(result)
        save_student_data(data, STUDENT)