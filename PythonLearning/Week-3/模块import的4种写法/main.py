# 写法1：导入整个模块
import math_utils
print(math_utils.add(1, 2))     # 3


# 写法2：起别名
import math_utils as mu
print(mu.PI)        # 3.14159


# 写法3：导入模块中的单个功能
from math_utils import add
print(add(3, 4))            # 7


# 写法4：导入模块中的全部功能（不推荐）
from math_utils import *
# 注意：这样会污染命名空间，难追踪变量来自哪里