# 实现接受不定量的数据，并用字典打包返回总和、平均值等数据

def stat_analysis(*args: int|float) -> dict|None:
    nums = list(args)
    if  nums:
        result = {}
        result["sum"] = sum(nums)
        result["avg"] = sum(nums) / len(nums)
        result["max"] = max(nums)
        result["min"] = min(nums)
        return result
    else:
        return None

if __name__ == "__main__":
    print(stat_analysis(12, 45, 33, 67 ,21))