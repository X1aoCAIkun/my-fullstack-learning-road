# try块：需要进行异常处理的主代码，需要配合except或者finally使用
# except块：捕获异常，其后接的是捕获的异常类型，代码块是对异常的处理
# else块：在未出现异常时执行
# finally块：永远都会执行
# 注：Exception会捕获大部分异常，难以分清出错类型不利于修改
# 而BaseException是所有异常的根，它会捕获所有异常


try:
    n = int(input("数字："))
    print(10 / n)
except ValueError:
    print("不是有效数字")
except ZeroDivisionError:
    print("除数不能为0")
except Exception as e:              # 放在所有except后兜底，捕获其余不匹配的异常
    print("其他错误", e)
else:
    print("没异常才执行")
finally:
    print("无论如何都会执行（清理）")


# Python内置的异常类型也许不够我们的实际所需，所以有了自定义异常
# 继承于Exception
class InsufficientFundsError(Exception):
    """余额不足"""

def withdraw(balance, n):
    """
    :balance：余额
    :n：取钱数目
    """
    if n > balance:
        # 这里要主动抛出自定义的异常，否则这个异常不会被捕获
        raise InsufficientFundsError(f"想取 {n}，只有{balance}")            # 抛出自定义异常的一个对象
    return balance - n

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print("被捕获", e)


# 异常链（raise from） raise 新异常 from 旧异常，表示新异常由旧异常导致
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("解析配置失败") from e
# 报错信息会同时显示原始的ValueError和RuntimeError

# 注意：在以后的编码过程中，不要catch了所有异常后pass--这是工程灾难。要么处理，要么让异常抛上去