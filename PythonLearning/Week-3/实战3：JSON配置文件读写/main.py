import json
from pathlib import Path


# 为了让生成的文件存在指定目录下
BASE = Path(__file__).parent        # 直接找到该文件（main.py）的完整路径（相对终端的）
CONFIG = BASE / "config.json"           # 因为BASE以经时Path对象，不需要再次创建

def load_config():
    if CONFIG.exists():
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    return {"theme": "light", "lang": "zh"}         # 当config.json文件不存在时返回默认信息

def save_config(cfg):
    CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")

cfg = load_config()     # 先加载文件
cfg["theme"] = "dark"
save_config(cfg)
print("已保存", cfg)
