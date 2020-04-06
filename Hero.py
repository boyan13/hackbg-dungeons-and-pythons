from Weapon import Weapon
from Spell import Spell


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.MAX_HEALTH = health
        self.mana = mana
        self.MAX_MANA = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.spell = None
        self.weapon = None

    @staticmethod
    def validate_init(name, title, health, mana, mana_rate):
        strings = type(name) is str and type(title) is str
        health = type(health) is int and health > 0
        mana = type(mana) is int and mana > 0
        mana_regeneration_rate = type(mana_regeneration_rate) is int and mana_rate > 0
        return strings and health and mana and mana_regeneration_rate

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        if self.health < 0:
            self.health = 0
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def can_cast(self):
        if self.spell is None:
            return False
        if self.mana >= self.spell.mana_cost:
            return True
        return False

    def take_damage(self, damege_points):
        self.health -= damege_points

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
            if self.health > self.MAX_HEALTH:
                self.health = self.MAX_HEALTH
            return True
        return False

    def take_mana(self, mana_points=0):
        if mana_points == 0:
            mana_points += self.mana_regeneration_rate
        self.mana += mana_points
        if self.mana > self.MAX_MANA:
            self.mana = self.MAX_MANA

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=None):
        if by == "spell" or by is None:
            if self.can_cast():
                self.mana -= self.spell.mana_cost
                return self.spell.damage
        if by == "weapon" or by is None:
            if self.weapon is not None:
                return self.weapon.damage
        return 0
