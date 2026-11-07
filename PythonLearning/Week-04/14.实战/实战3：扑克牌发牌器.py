import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    rank: str       # 数字
    suit: str       # 花色
    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    RANKS = list("23456789TJQKA")
    SUITS = "♠♥♦♣"

    def __init__(self):
        self.cards = [Card(r, s) for r in self.RANKS for s in self.SUITS]
        random.shuffle(self.cards)       # 打乱列表元素顺序，但是是原地打乱

    def deal(self, n):
        hand , self.cards = self.cards[:n], self.cards[n:]      # 实现不放回抽取
        return hand

    def __len__(self):
        return len(self.cards)

deck = Deck()
print(deck.deal(5))         # 输出前5张牌
print("剩余:", len(deck))
