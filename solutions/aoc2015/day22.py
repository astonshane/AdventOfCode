from register import register_solution
import copy

class Player:
    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.cost = 0
        self.active_spells = []

    def __str__(self):
        return "- Player has %d hit points, %d mana, %d cost)" % (self.hp, self.mana, self.cost)

    def __repr__(self):
        return self.__str__()

    def dealDamage(self, dmg, armor_boost):
        self.hp -= max(1, dmg - (self.armor + armor_boost))

    def alreadyActive(self, tst):
        for spell in self.active_spells:
            if spell.name == tst.name:
                return True
        return False


class Boss:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.damage = dmg

    def __str__(self):
        return "- Boss has %d hit points" % self.hp

    def __repr__(self):
        return self.__str__()

    def dealDamage(self, spell):
        self.hp -= spell.damage


class Spell:
    def __init__(self, name=0, cost=0, damage=0, heal=0, mana=0, turns=0, shield=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.mana = mana
        self.turns = turns
        self.armor = shield

    def __str__(self):
        return "%s (%d)" % (self.name, self.turns)

    def __repr__(self):
        return self.__str__()

global min_cost
min_cost = None
all_costs = []
all_spells = []


def takeTurn(turn, player, boss, hardmode=False):
    global min_cost
    if turn and hardmode and boss.hp > 0:
        print("\n--- Player's turn:")
        player.hp -= 1
        if player.hp < 1:
            print("## player died... (hard mode)")
    else:
        print("\n--- Boss's turn:")
    print(player)
    print(boss)

    armor_boost = 0

    print("active spells:", player.active_spells)
    new_spells = []
    for spell in player.active_spells:
        spell.turns -= 1
        armor_boost = spell.armor
        boss.hp -= spell.damage
        player.hp += spell.heal
        player.mana += spell.mana

        if spell.turns > 0:
            new_spells.append(spell)
    player.active_spells = new_spells
    print("active spells:", player.active_spells)

    if player.hp < 1:
        print("## player died...")
        return
    elif boss.hp < 0:
        if min_cost is None or player.cost < min_cost:
            min_cost = player.cost
        print("#### boss died...")
        return

    if turn:
        if player.mana < 53:
            print("player died, not enough mana")
            return
        for spell in all_spells:
            n_spell = copy.deepcopy(spell)
            if player.alreadyActive(spell) or player.mana < spell.cost or (
                    min_cost is not None and player.cost + spell.cost >= min_cost):
                continue
            print("player using", spell)
            new_p = copy.deepcopy(player)
            new_b = copy.deepcopy(boss)
            new_p.cost += spell.cost
            new_p.mana -= spell.cost
            if n_spell.turns > 0:
                new_p.active_spells.append(n_spell)
            else:
                new_b.dealDamage(n_spell)

            if player.hp < 1:
                print("## player died...")
                return
            elif boss.hp < 0:
                if min_cost is None or player.cost < min_cost:
                    min_cost = player.cost
                print("#### boss died...")
                return
            else:
                takeTurn(not turn, new_p, new_b, hardmode)

    else:
        player.dealDamage(boss.damage, armor_boost)

        if player.hp < 1:
            print("## player died...")
            return
        elif boss.hp < 0:
            if min_cost is None or player.cost < min_cost:
                min_cost = player.cost
            print("#### boss died...")
            return
        else:
            takeTurn(not turn, player, boss, hardmode)

@register_solution(2015, 22, 1)
def part1(filename):

    # puzzle input
    boss = Boss(55, 8)

    player = Player(50, 500)
    all_spells.append(Spell("Magic Missile", 53, damage=4))
    all_spells.append(Spell("Drain", 73, damage=2, heal=2))
    all_spells.append(Spell("Shield", 113, shield=7, turns=6))
    all_spells.append(Spell("Poison", 173, turns=6, damage=3))
    all_spells.append(Spell("Recharge", 229, turns=5, mana=101))

    takeTurn(True, player, boss)
    print(min_cost)


@register_solution(2015, 22, 2)
def part2(filename):
    # puzzle input
    boss = Boss(55, 8)

    player = Player(50, 500)
    all_spells.append(Spell("Magic Missile", 53, damage=4))
    all_spells.append(Spell("Drain", 73, damage=2, heal=2))
    all_spells.append(Spell("Shield", 113, shield=7, turns=6))
    all_spells.append(Spell("Poison", 173, turns=6, damage=3))
    all_spells.append(Spell("Recharge", 229, turns=5, mana=101))

    takeTurn(True, player, boss, hardmode=True)
    print(min_cost)
