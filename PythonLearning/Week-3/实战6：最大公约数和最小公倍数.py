def gcd(x: int, y: int) -> bool:
    """求两个正整数的最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> bool:
    """求最小公倍数"""
    return x * y // gcd(x, y)

print(gcd(18, 12))
print(lcm(18, 12))