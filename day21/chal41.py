import sys
import itertools
import copy


class Player:
    def __init__(self, name, hp, dmg, arm):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.arm = arm
        self.cost = 0

    def __str__(self):
        return "%s(%d %d %d)" % (self.name, self.hp, self.dmg, self.arm)


class AddOn:
    def __init__(self, cost, dmg, armor):
        self.cost = cost
        self.dmg = dmg
        self.arm = armor

    def __str__(self):
        return "(%d %d %d)" % (self.cost, self.dmg, self.arm)

    def __repr__(self):
        return self.__str__()


def findWinner(player, boss):
    # True == Player
    turn = True
    while (player.hp > 0 and boss.hp > 0):
        if turn:
            damage = player.dmg - boss.arm
            if damage < 1:
                damage = 1
            boss.hp -= damage
            if boss.hp < 1:
                return True
            turn = False
        else:
            damage = boss.dmg - player.arm
            if damage < 1:
                damage = 1
            player.hp -= damage
            if player.hp < 1:
                return False
            turn = True

# ######################
if len(sys.argv) != 2:
    print "need an input file"
    exit(1)

f = open(sys.argv[1])
boss_hp = boss_damage = boss_armor = None
for line in f:
    line = line.split(':')
    if line[0] == "Hit Points":
        boss_hp = int(line[1])
    elif line[0] == "Damage":
        boss_damage = int(line[1])
    elif line[0] == "Armor":
        boss_armor = int(line[1])

boss = Player("boss", boss_hp, boss_damage, boss_armor)

f.close()
f = open("store.txt")
weapons = []
armor = [AddOn(0, 0, 0)]
rings = [AddOn(0, 0, 0)]
kind = None
for line in f:
    if ":" in line:
        kind = line.split(":")[0]
    else:
        line = line.split()
        if len(line) == 0:
            continue
        cost = int(line[-3])
        dmg = int(line[-2])
        arm = int(line[-1])
        add = AddOn(cost, dmg, arm)
        if kind == "Weapons":
            weapons.append(add)
        elif kind == "Armor":
            armor.append(add)
        else:
            rings.append(add)

rings1 = itertools.permutations(rings, 1)
rings2 = itertools.permutations(rings, 2)
rings = [None]
for ring in rings1:
    rings.append(ring)
for ring in rings2:
    rings.append(ring)

min_cost = None

for weapon in weapons:
    for arm in armor:
        for ringset in rings:
            player = Player("player", 100, 0, 0)
            player.dmg += weapon.dmg
            player.cost += weapon.cost
            if arm is not None:
                player.arm += arm.arm
                player.cost += arm.cost
            if ringset is not None:
                for ring in ringset:
                    if ring is not None:
                        player.cost += ring.cost
                        player.dmg += ring.dmg
                        player.arm += ring.arm
            boss1 = copy.deepcopy(boss)
            print player, boss
            tmp = findWinner(player, boss1)
            if tmp:
                print "Player Won"
                if min_cost is None or player.cost < min_cost:
                    min_cost = player.cost
            else:
                print "Boss Won"

print min_cost
