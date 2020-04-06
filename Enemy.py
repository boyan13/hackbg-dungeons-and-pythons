from Weapon import Weapon
from Spell import Spell


class Enemy():

    # Base Enemy Type Class

    # To be derived in the future?

    # Constraints:
    #
    #   - Enemies cannot regenerate mana!
    #   - Enemies can attack without a weapon or a spell (they have base damage)
    #   - Enemies can also equip, learn and utilize weapons and spells

    def __init__(self, health, mana, damage):

        self.__class__.validate_init(health, mana, damage)

        self.MAX_HEALTH = health
        self.health = health
        self.mana = mana
        self.damage = damage

        self.weapon = None
        self.spell = None

    @classmethod
    def validate_init(cls, health, mana, damage):

        if health < 1:
            raise ValueError("Enemy with negative or zero health points.")
        if mana < 0:
            raise ValueError("Enemy with negative mana points.")
        if damage < 1:
            raise ValueError("Enemy with negative or no base damage.")

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        if self.spell is None:
            return False
        else:
            return self.mana - self.spell.mana_cost >= 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, amount):
        if amount < 1:
            raise ValueError("Enemy taking negative or zero healing.")

        if self.health + amount >= self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        else:
            self.health += amount

    def get_strongest_attack(self):
        pass

    def attack(self, by=None):
        if by is None:
            return self.damage

        elif by == "weapon":
            if self.weapon is None:
                return 0
            else:
                return self.weapon.damage

        elif by == "magic":
            if self.spell is None:
                return 0
            else:
                self.mana -= self.spell.mana_cost
                return self.spell.damage

        else:
            raise Exception("Failed to execute attack!")

    def take_damage(self, damage_points):
        if self.health - damage_points <= 0:
            self.health = 0
        else:
            self.health -= damage_points

    def equip(self, weapon):
        if type(weapon) is Weapon:
            self.weapon = weapon
        else:
            raise TypeError("Expected a weapon.")

    def learn(self, spell):
        if type(spell) is Spell:
            self.spell = spell
        else:
            raise TypeError("Expected a spell.")