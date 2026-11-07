# 引入json模块对文件标准化管理，并用pathlib完成文件的创建与读取
import json
from pathlib import Path


PATH = Path("score.json")       # 创建文件路径

# 加载函数
def load():
    if not PATH.exists():
        return []       # 分数文件还未存在时返回一个空列表（主文件用列表存储数据）
    return json.loads(PATH.read_text(encoding="utf-8"))

# 保存数据函数
def save(data):
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
