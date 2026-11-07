# ============================================================
# 14. 综合大题:魔法竞技场(回合制对战)
# ============================================================
# 总目标:用 Week-5 学过的知识,从零搭建一个回合制对战小游戏的核心系统,
#         最后跑通一场完整的对战演示。
#
# 玩法:你(60 蓝量)对战一个 100 血的训练假人。每回合选择一个技能,
#       命中率 80%,连续命中会积累"连击",连击越高伤害加成越高;
#       未命中则连击清零。把假人血量打到 0 就获胜。
#
# 三个技能(用 partial 造,见任务4):
#   火球术:伤害 30,耗蓝 10
#   冰箭术:伤害 20,耗蓝 5
#   雷霆术:伤害 45,耗蓝 20,有 2 秒冷却
#
# 知识点覆盖地图:
#   任务1 → 闭包(连击计数器)        任务2 → @lru_cache(伤害加成)
#   任务3 → 自定义异常体系           任务4 → partial + 函数是一等公民
#   任务5 → 带参数的装饰器(冷却)    任务6 → 类装饰器(攻击统计)
#   任务7 → 上下文管理器类(战斗)    任务8 → @contextmanager(阶段日志)
#   任务9 → 异常链(规则加载)        主流程 → try/except/else/finally 大串连
#
# 建议按任务顺序逐个写、逐个自测,最后再组装主流程。
# ============================================================


# ---------- 任务1:闭包 · 连击计数器 ----------
# 写 make_combo_tracker(),返回两个函数 hit() 和 miss():
#   - hit():连击数 +1,返回当前连击数
#   - miss():连击数清零,返回 0
# 提示:内部状态是 make_combo_tracker 的局部变量,
#       hit/miss 里用 nonlocal 修改它。
# 自测:hit() 得到 1,再 hit() 得到 2,miss() 得到 0,再 hit() 得到 1。
#       (自测完记得 miss() 一下清零,不然连击数会被带进后面的对战)

def make_combo_tracker():
    """计算连击次数"""
    count = 0
    def hit():
        """连击持续"""
        nonlocal count
        count += 1
        return count
    def miss():
        """连击中断"""
        nonlocal count
        count = 0
        return count
    return hit, miss

hit, miss = make_combo_tracker()
print(hit())        # 1
print(hit())        # 2
print(miss())       # 0


# ---------- 任务2:@lru_cache · 连击奖励 ----------
# 写递归函数 bonus(n):n 连击时的伤害加成。
#   bonus(0) = 0,bonus(n) = bonus(n-1) + 5
# 用 @lru_cache(maxsize=None) 装饰,打印 bonus(50) 和 bonus.cache_info()。
# 想一想:为什么这里 hits 很可能是 0?            因为这里的每个bonus(n)都只会被计算一次
#        (对比斐波那契——bonus 的递归每个 n 只被算一次,没有重复计算)

from functools import lru_cache

@lru_cache(maxsize=None)
def bonus(n):
    """计算连击加成"""
    if n == 0:
        return 0
    return bonus(n-1) + 5

print(bonus(50))
print(bonus.cache_info())


# ---------- 任务3:自定义异常体系 ----------
# 定义四个异常(都写在类体里给个 docstring 即可):
#   BattleError(Exception)                  # 战斗系统异常基类
#   NotEnoughManaError(BattleError)         # 蓝量不足
#   SkillOnCooldownError(BattleError)       # 技能冷却中
#   InvalidSkillError(BattleError)          # 技能编号不存在
# 想一想:为什么三个子类都要继承 BattleError 而不是直接继承 Exception?       后续就只要一个except就可以捕获这这三种异常
#        (提示:主流程里可以 except BattleError 一网打尽)

class BattleError(Exception):
    """战斗系统异常基类"""
class NotEnoughManaError(BattleError):
    """蓝量不足"""
class SkillOnCooldownError(BattleError):
    """技能冷却中"""
class InvalidSkillError(BattleError):
    """技能编号不存在"""


# ---------- 任务4:partial · 三个技能 ----------
# 1. 写基础函数 cast_skill(name, base_damage, mana_cost, mana):
#    - 蓝量不足(mana < mana_cost)时 raise NotEnoughManaError,
#      消息里带上技能名、需要多少、当前多少
#    - 否则返回 (base_damage, mana - mana_cost)
# 2. 用 partial 固定前三个参数,造出三个技能:
#    fireball = partial(cast_skill, "火球术", 30, 10)
#    ice_arrow = partial(cast_skill, "冰箭术", 20, 5)
#    thunder   = 见任务5(它还要套冷却)
# 3. 把技能放进字典 skills = {"1": fireball, "2": ice_arrow, "3": thunder}
#    —— 函数装进容器,这就是"函数是一等公民"。
# 自测:fireball(mana=100) 得到 (30, 90);
#       fireball(mana=5) 应抛出 NotEnoughManaError(用 try 接住验证)

from functools import partial

def cast_skill(name, base_damage, mana_cost, mana):
    """
    :name: 技能名称
    :base_damage: 技能基础伤害
    :mana_cost: 技能耗蓝量
    :mana: 人物初始蓝量
    """
    if mana < mana_cost:
        raise NotEnoughManaError(f"技能 {name} 需要蓝量：{mana_cost} 现有蓝量：{mana}")
    else:
        return (base_damage, mana - mana_cost)


# 用两种形式构建技能函数（其他属性固定，mana后续调用技能时传入）
fireball = partial(cast_skill, name="火球术", base_damage=30, mana_cost=10)
ice_arrow = partial(cast_skill, "冰箭术", 20, 5)

print(fireball(mana=100))
try:
    print(fireball(mana=5))
except NotEnoughManaError as n:
    print("出现异常：", n)


# ---------- 任务5:带参数的装饰器 · 技能冷却 ----------
# 写 cooldown(seconds, label="技能"),返回装饰器,要求:
#   - 用 nonlocal 记录上次成功释放的时间
#   - 冷却期内调用 → raise SkillOnCooldownError(f"{label} 冷却中,请稍后再试")
#   - 冷却期外调用 → 更新时间,正常放行原函数并返回其结果
# 用法(注意:装饰器套在 partial 外面):
#   thunder = cooldown(2, label="雷霆术")(partial(cast_skill, "雷霆术", 45, 20))
# 自测:连续调 thunder(mana=100) 两次,第二次应抛 SkillOnCooldownError;
#       time.sleep(2) 后再调,应成功。

import time

def cooldown(seconds, label="技能"):
    """
    :seconds: 技能的冷却时间 
    :label: 执行冷却的技能名称
    """
    start = 0       # 上次使用技能的时间，初始为0
    def deco(fn):
        """
        :fn: 技能函数
        """
        def wrapper(*arg, **kwargs):
            nonlocal start
            now = time.perf_counter()       # 记录当前时间
            if now - start < seconds:
                raise SkillOnCooldownError(f"技能 {label} 冷却中，请稍后再试")
            else:
                result = fn(*arg, **kwargs)     # result接收技能函数的结果
                start = time.perf_counter()             # 更新技能释放时间
                return result
        return wrapper
    return deco

thunder = cooldown(2, "雷霆术")(partial(cast_skill, "雷霆术", 45, 20))
# 技能列表（字典）
skills = {"1": fireball, "2": ice_arrow, "3": thunder}

print(thunder(mana=100))
try:
    print(thunder(mana=80))
except SkillOnCooldownError as s:
    print("出现异常：", s)
time.sleep(2)
print(thunder(mana=50))
time.sleep(2)


# ---------- 任务6:类装饰器 · 攻击统计 ----------
# 1. 写类装饰器 CountCalls:
#    - __init__ 里用 wraps(fn)(self),保存 fn,准备 self.history = []
#    - __call__ 里调用原函数,把 (args, 结果) 追加进 self.history,返回结果
#    - 再写一个普通方法 total(self),返回 history 的长度
# 2. 用 @CountCalls 装饰 attack:
#    def attack(skill, mana):
#        - 调 skill(mana) 得到 (基础伤害, 剩余蓝量)
#        - 调 hit() 拿到当前连击数,总伤害 = 基础伤害 + bonus(连击数)
#        - 打印 "连击 x{n},总伤害 {总伤害}"
#        - 返回 (总伤害, 剩余蓝量)
# 自测:attack(ice_arrow, 100) 调两次,打印 attack.total() 应为 2,
#       打印 attack.history 查看记录。

from functools import wraps

class CountCalls:
    def __init__(self, fn):
        wraps(fn)(self)
        self.fn = fn        # 技能函数
        self.history = []   # 技能使用记录

    def __call__(self, *args, **kwds):
        result = self.fn(*args, **kwds)
        self.history.append((args, result))
        return result

    def total(self):
        return len(self.history)

@CountCalls
def attack(skill, Mana):
    damage_mana = skill(mana=Mana)
    hit_count = hit()
    bonus_num = bonus(hit_count)
    total_damage = damage_mana[0] + bonus_num
    print(f"连击 x{hit_count}，总伤害 {total_damage}")
    return (total_damage, damage_mana[1])

attack(ice_arrow, 100)
attack(ice_arrow, 100)
print(attack.total())
print(attack.history)
miss()


# ---------- 任务7:上下文管理器类 · 战斗场景 ----------
# 写类 Battle:
#   - __enter__:记录开始时间,self.rounds = 0,打印 "战斗开始!",return self
#   - __exit__:打印耗时;根据 exc_type 是否为 None 区分两种结束语:
#       无异常 → "战斗结束:共 {rounds} 回合,耗时 X.XXs"
#       有异常 → "战斗异常中断({异常类型名}),耗时 X.XXs"
#     注意:不要吞掉异常(return False 或什么都不 return)
# 提示:主流程里用 with Battle() as battle:,
#      每回合把 battle.rounds 更新为当前回合数。

class Battle:
    def __enter__(self):
        self.start = time.perf_counter()
        self.rounds = 0         # 战斗回合数
        print("战斗开始")
        return self
    def __exit__(self, exc_type, exc, tb):
        if not exc_type:
            print(f"战斗结束：共 {self.rounds} 回合，耗时 {time.perf_counter() - self.start:.2f}s")
        else:
            print(f"战斗异常中断({exc_type.__name__})，耗时 {time.perf_counter() - self.start:.2f}s")
            
with Battle() as b:
    attack(fireball, 100)
    b.rounds = 1
miss()

# ---------- 任务8:@contextmanager · 阶段日志 ----------
# 用 @contextmanager 写 stage(name):
#   - 进入时打印 ">>> 进入 {name}",退出时打印 "<<< 退出 {name}"
#   - 块内抛异常时,"退出"这行也必须打印,异常照常向外抛
# 可选加分:用一个全局变量 depth 控制缩进(进入 +1,退出 -1),
#           这样嵌套的 stage 日志会像树一样一层层缩进。

from contextlib import contextmanager

depth = 0

@contextmanager
def stage(name):
    global depth
    print("  " * depth + f">>> 进入 {name}")
    depth += 1
    try:
        yield
    finally:
        depth -= 1
        print("  " * depth + f"<<< 退出 {name}")


# ---------- 任务9:异常链 · 规则加载 ----------
# 写 load_rules(path):
#   1. 函数内部执行 int(path)(模拟"规则文件内容不是合法数字")
#   2. 捕获 ValueError 后 raise BattleError("规则文件解析失败") from e
# 外层 try 捕获 BattleError,打印 "规则加载失败,使用默认规则" 和 e.__cause__,
# 让程序能继续往下走。

def load_rules(path):
    try:
        int(path)
    except ValueError as v:
        raise BattleError("规则文件解析失败") from v

try:
    load_rules("a")
except BattleError as b:
    print("规则加载失败，使用默认规则")
    print(b.__cause__)


# ---------- 主流程:把一切组装起来 ----------
# 要求(按下面的骨架写,自己补全细节):
#   假人血量 dummy_hp = 100,玩家蓝量 mana = 60,回合数从 1 开始
#
#   with Battle() as battle:
#       while dummy_hp > 0:
#           battle.rounds = 当前回合
#           try:
#               with stage(f"第 {回合} 回合"):
#                   1. input 让玩家输入技能编号
#                   2. 编号不在 skills 里 → raise InvalidSkillError
#                   3. dmg, mana = attack(skills[编号], mana)
#                   4. 命中判定:random.random() < 0.8
#                      命中:假人扣血,打印剩余血量
#                      未命中:调 miss(),打印 "未命中,连击中断"
#           except NotEnoughManaError as e:
#               打印异常;回合结束回复 5 点蓝量
#           except SkillOnCooldownError as e:
#               打印异常
#           except InvalidSkillError as e:
#               打印异常
#           except BattleError as e:
#               打印 "战斗错误:..."(兜底)
#           else:
#               打印 "回合顺利完成"
#           finally:
#               打印 "已进行 {回合} 回合",回合数 +1
#       循环结束后打印胜利信息
#
#   战斗结束后打印 "本场共释放技能 X 次"(用 attack.total())
#
# 注意点:
#   - except 的顺序:三个具体异常在前,BattleError 兜底在后
#   - 连击逻辑要想清楚:hit() 在 attack 里已经 +1 了,
#     未命中时 miss() 清零,顺序不能乱
#   - 想快速自动测试:临时把 input 换成固定列表,例如
#     for choice in ["3", "3", "x", "1", "1", "1", ...]:
#
# ============================================================
# 验收清单(全部跑通后,对照检查这些行为都出现过):
#   [ ] 连续两次选雷霆术 → 第二次打印冷却提示(2 秒内)
#   [ ] 输入不存在的编号 → 打印"不存在编号为 X 的技能"
#   [ ] 蓝量耗尽再放技能 → 打印蓝量不足 + 回蓝
#   [ ] 命中 3 次以上 → 连击伤害递增(30 → 35 → 40 ...)
#   [ ] 未命中 → 连击清零,下次命中从 x1 重新算
#   [ ] 回合出错时,"<<< 退出"仍先于 except 打印(清理先于处理)
#   [ ] 战斗结束打印总回合数、耗时、技能释放总次数
# ============================================================

import random

dummy_hp = 100; MANA = 60

# 战斗前清理数据
miss()
attack.history.clear()

with Battle() as battle:
    while dummy_hp > 0:
        battle.rounds += 1
        try:
            with stage(f"第 {battle.rounds} 回合"):
                number = input("输入技能编号：")
                if number not in skills:
                    raise InvalidSkillError(f"编号 {number} 技能不存在")
                else:
                    damage, MANA = attack(skills[number], MANA)
                if random.random() < 0.8:
                    if dummy_hp -damage > 0:
                        dummy_hp -= damage
                    else:
                        dummy_hp = 0
                    print(f"攻击命中，假人剩余血量：{dummy_hp}")
                else:
                    miss()
                    print("未命中，连击中断")
        except NotEnoughManaError as n:
            print("出现异常：", n)
            MANA += 5
            print("恢复5点蓝量")
        except SkillOnCooldownError as s:
            print("出现异常：", s)
        except InvalidSkillError as i:
            print("出现异常：", i)
        except BattleError as b:
            print("战斗错误：", b)
        else:
            print("回合结束")
        finally:
            print(f"已进行 {battle.rounds} 回合")

    print("战斗胜利")
print(f"本场共释放技能 {attack.total()} 次")            