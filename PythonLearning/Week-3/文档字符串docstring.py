# docstring就是在函数开头用""""""写明函数的基本信息（功能、参数含义、返回结果）


def divide(a, b):
    """两数相除

    Args：
        a：被除数
        b：除数（不能为0）

    
    Returns：
        商：类型float
    """
    return a / b

print(divide.__doc__)
help(divide)        # 生成帮助文档，依靠docstring以及Python对象自带的元信息（参数列表等）
