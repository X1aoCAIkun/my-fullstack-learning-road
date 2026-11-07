# 游戏对象有牌、扑克、玩家三类对象，所以有三个类
from enum import Enum
import random

# 因为花色是固定的，而且我们想用0~3四个数字代表花色，所以使用枚举比较好
class Suite(Enum):
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

# 牌类
class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = "♠♥♣♦"
        faces = ["", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{suites[self.suite.value]}{faces[self.face]}"

    # 为了能是后续arrange()函数可以比较大小，所以这里对运算符重载
    # l是小，g是大，e是等，eq是==，ne是!=
    def __lt__(self, other):
        if self.suite.value == other.suite.value:
            return self.face < other.face
        return self.suite.value < other.suite.value

# 扑克类
class Pork:
    # 整合了一副扑克牌
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.current = 0        # 记录当发的最后一张牌的位置
    # 洗牌
    def shuffle(self):
        self.current = 0        # 洗牌则发的最后一张牌回到开头那张牌
        random.shuffle(self.cards)
        
    # 发牌(一张一张发)
    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

    # 检查还有没有牌可以发
    @property
    def has_next(self):
        return self.current < len(self.cards)

# 玩家类
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []     # 玩家的牌

    # 摸牌
    def get_one(self, card): 
        self.cards.append(card)

    # 整理手牌
    def arrange(self):
        self.cards.sort()

# 先初始化一组扑克牌
pork = Pork()
pork.shuffle()
# 四个玩家
p1 = Player("东邪")
p2 = Player("西毒")
p3 = Player("南帝")
p4 = Player("北丐")
# 发牌（每人13张）
for _ in range(13):
    p1.get_one(pork.deal())
    p2.get_one(pork.deal())
    p3.get_one(pork.deal())
    p4.get_one(pork.deal())
# 检查牌发完没
if not pork.has_next:
    print("牌发完了")
# 玩家整理手牌后展示
p1.arrange()
print(f"{p1.name}：{p1.cards}")
p2.arrange()
print(f"{p2.name}：{p2.cards}")
p3.arrange()
print(f"{p3.name}：{p3.cards}")
p4.arrange()
print(f"{p4.name}：{p4.cards}")
