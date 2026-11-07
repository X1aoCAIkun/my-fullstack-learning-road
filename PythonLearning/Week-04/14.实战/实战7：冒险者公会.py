# 冒险者公会 —— 游戏角色养成系统
import random
from enum import Enum
from dataclasses import dataclass

# 定义枚举类，用于保存攻击加成系数
class Quality(Enum):
        COMMON = 1.0
        RARE = 1.2
        EPIC =1.5
        LEGENDARY = 2.0

# 用dataclass定义装备类
@dataclass
class Equipment:
    name: str
    quality: Quality
    attack_bonus: int

    def total_bonus(self):
        return self.attack_bonus * self.quality.value


# 角色类（父类）
class Character:
    def __init__(self, name: str, level=1, hp=100, attack=10, skills=None):
        self.name = name        # 角色名称
        self.max_hp = hp        # 初始最大血量     
        self.level = level      # 角色等级，初始等级为1
        self.__hp = hp          # 角色当前血量(私有)，初始血量为100
        self.attack = attack    # 角色攻击力，初始攻击力为10
        self.skills = skills if skills is not None else [] 

    # 受伤扣血方法，这里记得要给死亡角色血量归零
    def hurt(self, damage):
        if self.__hp - damage > 0:
            self.__hp -= damage
            return self.__hp
        else:
            self.__hp = 0
            return self.__hp
    
    # 判断角色是否存活 
    def is_alive(self):
        return self.__hp > 0

    # 两个输出信息魔法方法，适用不同的输出方式
    def __str__(self):
        return f"{self.name} Lv.{self.level} HP:{self.__hp}/{self.max_hp} 攻击:{self.attack}"
    def __repr__(self):
        return self.__str__()

    # 重载"=="\"<"\"+"运算符
    def __eq__(self, other):
        return self.name == other.name and self.level == other.level
    def __lt__(self, other):
        return self.level < other.level
    # 两个角色组队，返回新角色
    # 名字用 "张三&李四"，等级相加、血量相加、攻击取平均
    def __add__(self, other):
        new_name = self.name + "&" + other.name
        new_level = self.level + other.level
        new_hp = self.__hp + other.__hp
        new_attack = (self.attack + other.attack) // 2
        # 创建新角色
        return Character(new_name, new_level, new_hp, new_attack)

    # 实现三个property
    @property
    def hp(self):
        return self.__hp

    # 这里的_level与level要区分，这是两种不同渠道的赋值方法
    # 不区分则会出现死循环，外面的self.level=1进setter,setter里的self.level又进setter
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, l):
        if 1 <= l <= 100:
            self._level = l
        else:
            raise ValueError("等级只能是1~100")

    @property
    def power(self):
        return self.attack * self.level

    # 挂载装备
    def equip(self, item: Equipment):
        # 等效self.equipment = item
        setattr(self, "equipment", item)

    # 计算总伤害
    def total_attack(self):
        # 等效equipment = self.equipment
        equipment = getattr(self, "equipment", None)
        if equipment:
            return self.attack + equipment.total_bonus()
        else:
            return self.attack

    # 重写三个魔法方法，实现对技能列表的操作
    def __getitem__(self, key):
        return self.skills[key]

    def __call__(self, skill_name):
        if skill_name in self.skills:
            print(f"{self.name}使用了{skill_name}")
        else:
            print(f"{self.name}还没学会{skill_name}")

    def __len__(self):
        return len(self.skills)
    

# 练习动态属性 
# 药水类
class Potion:
    __slots__ = ("name", "heal")
    def __init__(self, name, heal):
        self.name = name
        self.heal = heal   


# 战士类（子类）
class Warrior(Character):
    def __init__(self, name, level=1, hp=100, attack=10):
        super().__init__(name, level, hp, attack)

    # 攻击方法
    def hit(self, target):
        target.hurt(self.attack * 2)
        print(f"{self.name}对{target.name}造成了{self.attack * 2}点伤害") 

    # 展示技能
    def skill(self):
        print("怒吼：气势爆发！")

# 法师类（子类）
class Mage(Character):
    def __init__(self, name, level=1, hp=100, attack=10):
        super().__init__(name, level, hp, attack)

    # 攻击方法
    def hit(self, target):
        target.hurt(self.attack + 10)
        print(f"{self.name}对{target.name}造成了{self.attack + 10}点伤害") 

    # 展示技能
    def skill(self):
        print("火球术：呼！")

# 射手类（子类）
class Archer(Character):
    def __init__(self, name, level=1, hp=100, attack=10):
        super().__init__(name, level, hp, attack)

    # 攻击方法
    def hit(self, target):
        # 暴击率，暴击则伤害*3
        ch_rate = random.random()
        mul = 1
        if ch_rate >= 0.5:
            mul = 3
        target.hurt(self.attack * mul)
        print(f"{self.name}对{target.name}造成了{self.attack * mul}点伤害") 

    # 展示技能
    def skill(self):
        print("百步穿杨！")

# 对战函数（多态函数）
def battle(c1, c2):
    while c1.is_alive() and c2.is_alive():
        c1.hit(c2)
        # 攻击前判断是否阵亡
        if c2.is_alive():
            c2.hit(c1)
    if c1.is_alive():
        print(f"{c1.name}获胜")
        return c1
    else:
        print(f"{c2.name}获胜")
        return c2

# 练习多继承与MRO
class Flyable:
    def move(self):
        print("飞向天空")

class Swimmable:
    def move(self):
        print("潜入水中")
class SkyKnight(Warrior, Flyable):
    def move(self):
        super().move()
        print("并在天空中盘旋")
# 问题思考
# SkyKnight().move() 会依次调用哪些类的 move？
# SkyKnight.move()->Flyable.move()->SkyKnight.move()

# 为什么能通过 super() 找到 Flyable.move？
# super() 不是"直接找父类"，而是沿实例类的 MRO 列表向后找
# 第一个定义了 move() 的类。
# SkyKnight 的 MRO 里，Warrior 和 Character 都没定义 move，
# 所以一路往后找到了 Flyable。
# 这正是 MRO 存在的意义——如果只是找直接父类，
# super().move() 在 Warrior 这里就该报错了

# print(SkyKnight.__mro__) 输出什么？
# SkyKnight, Warrior, Character, Flyable, object

# 如果改成 class SkyKnight(Flyable, Warrior)，MRO 会变成什么样？
# SkyKnight, Flyable, Warrior, Character, object

# mixin 应该放在父类列表的什么位置？为什么？
# 放在主父类后 ①子类必须排在父类前面 ②保持各父类原本的顺序。





# 测试
if __name__ == "__main__":
    c1 = Character("张三", 3, 100, 20)
    c2 = Character("张三", 3, 100, 20)
    c3 = Character("李四", 5, 150, 30)
    print(c1 == c2)         # True
    print(c1 < c3)          # True
    print(c1 + c3)          # 张三&李四 Lv.8 HP:250/250 攻击:25
    print([c1, c3])         # 放进列表也能正常显示（考验 __repr__）
    
    c4 = Warrior("王五", 6, 100, 20)
    c5 = Mage("赵六", 7, 100, 20)
    c6 = Archer("小明", 8, 100, 20)
    print(c4 == c5)
    print(c4 < c5)
    print(c5 + c6)
    c4.skill()
    c5.skill()
    c6.skill()
    battle(c4, c5)
    battle(c5, c6)
    battle(c4, c6)
    
    SkyKnight("天空骑士").move()
    print(SkyKnight.__mro__)

    c7 = Character("张三", 3, 100, 20)
    print(c7.power)                      # 60
    c7.level = 5
    print(c7.power)                      # 100
    # c7.level = 999                       # ValueError
    # c7.hp = 999                          # AttributeError：hp 只读
    e1 = Equipment("屠龙刀", Quality.EPIC, 10)
    print(e1.total_bonus())              # 15.0

    c8 = Mage("小红", 20, 100, 50)
    e2 = Equipment("尚方宝剑",Quality.LEGENDARY, 20)
    print(c8.total_attack())
    c8.equip(e2)
    print(c8.total_attack())

    p1 = Potion("狂暴", "无")
    # p1.extra = 1            # AttributeError 因为Potion类限定了只能由name和heal这两个属性

    c9 = Character("小明", 3, 100, 20, skills=["火球术", "治疗术", "闪现"])
    print(len(c9))              # 3
    print(c9[0])                # 火球术
    print(c9[2])                # 闪现
    c9("火球术")                # 小明 使用了 火球术！
    c9("召唤术")                # 小明 还没学会 召唤术