# 主文件，调用模块函数实现程序
from score_app import storage, analyzer


data = storage.load()           # 加载原文件数据
data.append({"name": "小明", "math": 90})
storage.save(data)          # 保存数据

print(analyzer.average(data, "math"))