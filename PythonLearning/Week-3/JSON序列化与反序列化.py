# 面对庞大的数据，不统一的格式往往会浪费大量存储空间
# 所以Python使用JSON字符串解决
# JSON就像快递员的“打包标准格式”。Python对象太复杂，存盘/联网前需要“打包”成JSON字符串
# 带s的方法是处理字符串的，不带是处理文件的
# 注意一下转换关系
# dict <→ JSON 对象 `{}`
# list /tuple → JSON 数组 `[]`  JSON数字[] -> list
# str → 字符串（自动加双引号）
# int、float → 数字
# True <→ true；False <→ false
# None <→ null



import json

data = {"name": "李雷", "age": 18, "skills": ["py", "js"]}

# 对象 -> JSON字符串（序列化）
# dumps()方法就是将转字符串方法。ensure_ascii=False，直接显示中文，不转换ascii码；indent=2表示自动换行+缩进
text = json.dumps(data, ensure_ascii=False, indent=2)
print(text) 

# JSON字符串 -> 对象（反序列化）
back = json.loads(text)
print(back["skills"][0])        # py

# 直接和文件打交道
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("user.json", encoding="utf-8") as f:
    obj = json.load(f)
print(obj)