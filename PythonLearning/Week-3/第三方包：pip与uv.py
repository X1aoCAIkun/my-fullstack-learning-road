# 当Python的标准库里的函数没有我们需要的功能，除了自己定义模块
# 还可以导入第三方库，减少一些不必要的工作
# 导入第三方库一般用pip和uv终端指令


# 老牌 pip
"""
pip install requests（需要的第三方库）
pip uninstall requests
pip list
pip install -r requirement.txt
"""


# 新潮的 uv（速度快十几倍）
"""
uv pip install requests
uv venv .venv       # 创建虚拟环境
source .venv/bin/activate
"""


# 锁定版本到 requirements.txt
"""
pip freeze > requirements.txt
"""