# 1.两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
nums1 = [2, 7, 11, 15]
target = 9
solution1 = []
for i in range(len(nums1)):
    for j in range(i + 1, len(nums1)):
        if nums1[i] + nums1[j] == target:
            solution1.append(i)
            solution1.append(j)

print(solution1)


# 2.回文数
# 给你一个整数x，如果x是一个回文整数，返回True；否则返回False
# 回文数是这正序（从左向右）和倒叙（从右向左）读都是一样的整数
# 例如：121是回文，而123不是
x = list(input("输入一个整数（可以带符号）"))
reverse_x = x[::-1]         # 反转列表
if x == reverse_x:
    print("True")
else:
    print("False")


# 3.最长公共前缀
# 给定一个字符串列表
# 查找各字符串中最长公共前缀，如果不存在公共前缀，则返回空字符
strs1 = ["flower", "flow", 'flight']
solus = ""
# 从一个字符串的第一个字母作为比较位
for i in range(len(strs1[0])):
    alpha = strs1[0][i]
    flag = True  # flag作为标记
    for j in strs1[1:]:      # 遍历除第一个字符串的字符串
        if len(j) <= i or j[i] != alpha:        # 如果比较的字母下标或者字母不匹配都直接截止所有比较
            flag = False
            break
    if flag:
        solus += alpha
    else:
        break
      
print(solus)


