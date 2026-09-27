# 例子1：100以内的素数
# 说明：素数指的是只能被 1 和自身整除的正整数（不包括 1）
# for i in range(2,100):
#     div_num = 0             # 用div_num记录i的整除数个数，每轮i循环刷新
#     for j in range(2,i + 1):
#         if i % j == 0:      # 可以整除则余数为0
#             div_num += 1
#     if div_num <= 2:        # 除1和i本身就两个整除数
#         print(f"{i}是素数",end='\t')         

# 例1升级版
# for num in range(2, 100):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):     # 如果num存在一个大于根号num的因数，那也一定会有一个小于根号的因数，所以不需要查那么多数字
#         if num % i == 0:
#             is_prime = False        # 只要存在一个非num本身的因数就一定不是素数
#             break
#     if is_prime:
#         print(num)

# 例子2：斐波那契数列
# 要求：输出斐波那契数列中的前 20 个数。
# x1 , x2 = 0 , 1             # x1表示数列的第0个数字，x2表示第一个数字
# for i in range(20):
#     x1 , x2 = x2, x1 + x2       # 依次移动x1和x2的位置，x1指向x2，x2指向数列的下一个数字（x1 + x2）
#     print(x1,end='\t')

# 例子3：寻找水仙花数
# 要求：找出 100 到 999 范围内的所有水仙花数。（指一个三位数，其各位数字立方和等于改数本身，如：1^3+5^3+3^3=153）
# count = 0
# for i in range(100,1000):
#      if (i // 100) ** 3 + (i % 10) ** 3 + ((i % 100) // 10) ** 3 == i:      # 依次得出百位、个位、十位上的数字
#           count += 1
#           print(i)
# print(f"共{count}个水仙花桃子数")

# 例3美化版
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# 例子4：百钱百鸡问题
# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
# for i in range(21):         # i记录公鸡只数（0~20）
#     for j in range(34):         # j记录母鸡只数（0~33）
#         for k in range(0,101,3):            # k记录小鸡只数，因为1钱不能拆开所以小鸡只数只能是0~100间3的倍数
#             if i * 2 + j * 3 + k // 3 == 100 and i + j + k == 100:          # 判断方案是否符合条件
#                 print(f"可行方案：公鸡/母鸡/小鸡：{i}/{j}/{k}")

# 例4优化版
# for x in range(21):
#     for y in range(34):
#         z = 100 - x - y         # 减少了一层循环
#         if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:        # z % 3 == 0判断小鸡个数是否为3的倍数
#             print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# 例子5：CRAPS赌博游戏
# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：
# 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
# 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数玩家继续摇骰子，直到分出胜负。
# 为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
# 每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
# 如果庄家获胜，玩家就会输掉自己下注的金额。
# 游戏结束的条件是玩家破产（输光所有的赌注）。
import random

current_bet = 1000         # 玩家当前剩余赌注，起始位1000

# 不知道游戏会进行多少轮，所以用while循环
while current_bet:              # 赌注不为0则可以继续游戏
    bet = int(input(f"当前剩余赌注{current_bet},请进行本次游戏下注："))
    while True:   
        player_first_num = random.randint(2,12)        # 玩家投出的第一次数               
        print(f"玩家第一次点数{player_first_num}",end='\n')
        if player_first_num == 7 or player_first_num == 11:         # == 优先级高于 |，所以：player_first_num == 7 | 11 → 实际是 player_first_num == (7 | 11) → player_first_num == 15，永远为 False
            print(f"玩家第一次投出了{player_first_num}，玩家直接获胜")
            current_bet += bet
            break
        elif player_first_num == 2 or player_first_num == 3 or player_first_num == 12:
            print(f"玩家第一次投出了{player_first_num}，庄家直接获胜")
            current_bet -= bet
            break
        else:                   # 第一次投骰子没分出胜负，则游戏继续进行直到分出胜负
            while True:         # 判断游戏是否决出胜负，默认没有      
                player_num = random.randint(2,12)       # 玩家第二次投骰子
                if player_num == 7:
                    print(f"玩家又投出了{player_num},庄家获胜")
                    current_bet -= bet
                    break
                elif player_num == player_first_num:
                    print(f"玩家投出了{player_num}与第一次相同,玩家获胜")
                    current_bet += bet
                    break
            break
