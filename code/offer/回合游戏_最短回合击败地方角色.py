'''
你在玩一个回合游戏制决策扮演的游戏,现在你准备一个策略，以便在最短回合内击败敌方角色，在战斗开始时，敌人拥有HP格血量，
当血量小于等于0时，敌人死去，一个缺乏经验的玩家可能简单地尝试每个回合都攻击，但是你知道辅助技能的重要性，
在你的每个回合开始时你可以选择一下两个动作之一： 聚力或者攻击
    聚力会提高你下个回合攻击的伤害
    攻击会对敌人造成一定量的伤害，如果你上个回合使用了聚力，那这次攻击会对敌人造成buffedAttack点伤害，否则，会造成normalAttack点伤害。
给出血量HP和不同攻击的伤害，buffedAttack和normalAttack，返回你能杀死敌人的最小回合数

第一行是一个数字HP
第二行是一个数字normalAttack
第三行是一个数字buffedAttack
1 <= Hp, buffedAttack, normalAttack <= 10^9

输出：
    输出一个数字表示回合数
    
示例1
    输入
        13
        3
        5
    输出
        5

'''

import math
# 血量
HP = int(input().split()[0])
normal = float(input().split()[0])
buffed = float(input().split()[0])

if normal >= HP:
    print(1)
elif buffed >= HP:
    print(2)
elif buffed >= 2 * normal:
    if HP % buffed ==0:
        print(int((HP / buffed) * 2 ))
    else:
        if HP % buffed >= normal:
            print(math.ceil((HP / buffed) * 2))
        else:
            print((math.ceil(HP / buffed) -1)*2 +1)
else:
    print(math.ceil(HP / normal))