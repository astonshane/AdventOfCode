class Player:
    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.cost = 0
        self.active_spells = []

    def __str__(self):
        return "- Player has %d hit points, %d armor, %d mana)" % (self.hp, self.armor, self.mana)

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
