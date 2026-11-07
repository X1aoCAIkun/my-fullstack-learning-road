import random
import string

# string.digits是字符0~9，string.ascii_letters是字符大小写英文字母
ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len=4):
    """
    生成随机验证码
    :param code_len：验证码长度（默认为4）
    :return：由大小写英文字母和数字组成的随机字符串
    """
    return "".join(random.choices(ALL_CHARS, k=code_len))

# 注意：sample是无放回抽样（无重复）；choices是有放回抽样（可重复）
# 同时，choices里的参数k是关键字传参，ALL_CHARS是样本空间

for i in range(5):
    print(generate_code())