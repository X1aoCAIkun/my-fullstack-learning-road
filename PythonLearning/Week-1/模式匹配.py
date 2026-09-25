# 当if/elis/else有太多判断时会显得代码很臃肿，可读性性较差
#此时可以考虑模式匹配match
#注意：match~case可以有多段代码块执行
score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')
#输出'score is B.'
#注意：只有最后一个case xxx:可以用case _:，表示任意值都可以匹配
age = 15

match age:
    case x if x < 10:           # 当age小于时匹配成功，并将age的值给x
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:         # 匹配多个值
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
