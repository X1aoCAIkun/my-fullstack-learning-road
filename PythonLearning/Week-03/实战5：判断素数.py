def is_prime(num: int) -> bool:
    """
    判断一个正数是不是素数
    :num：传入的正数
    :return：num是素数则返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False 
        return True

print(is_prime(30))