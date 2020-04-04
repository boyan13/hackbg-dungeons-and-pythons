import random
from Hero import Hero
from Weapon import Weapon
from Spell import Spell
#from Dungeon import Dungeon
from Enemy import Enemy


class Fight:
    def __init__(self):
        self.hero = None
        self.enemy = None
        self.distance = 0

    def start_fight(self, hero, enemy, distance):
        self.hero = hero
        self.enemy = enemy
        self.distance = distance
        while self.hero.is_alive() and self.enemy.is_alive():
            # the desition of the player
            if self.hero.is_alive():
                if self.enemy.is_alive():
                    print(self.hero_attack())
                    if not self.enemy.is_alive():
                        print("Enemy is dead.")
            if self.enemy.is_alive():
                if self.hero.is_alive():
                    print(self.enemy_attack())
                    if not self.hero.is_alive():
                        print("Hero is dead")
        return self.hero

    def hero_attack(self):
        # gets hero's move/attack
        command_list = {1: "spell", 2: "weapon", 3: "move", 4: "pass"}
        command = 0
        while int(command) not in command_list.keys():
            command = int(input("Enter on of:\n\
                1 to cast a spell,\n\
                2 to hit with weapon,\n\
                3 to move closer to the enemy,\n\
                4 to pass\n>>>"))
        command = command_list[command]# "spell"# get_move()
        s = ""
        print(1, command)
        if command == "pass":
            self.hero.take_mana()
            return"Pass the turn."
        if command == "move":
            if self.distance > 1:
                self.distance -= 1
            self.hero.take_mana()
            return"Hero moves one position."
        if command == "weapon" or command == "spell":
            if command == "spell":
                if self.hero.can_cast():
                    spell = self.hero.spell.name
                    dmg = self.hero.attack(command)
                    self.enemy.take_damage(dmg)
                    enemy_health = self.enemy.get_health()
                    return "Hero cast a {}, hits enemy for {} dmg. Enemy health is {}".format(spell, dmg, enemy_health)
                else:
                    s = "Hero can not cast spell. \n"
                    command = "weapon"
            if (command == "weapon"):
                if self.distance > 1:
                    self.hero.take_mana()
                    return s + "Pass the turn."
                else:
                    dmg = self.hero.attack("weapon")
                    self.enemy.take_damage(dmg)
                    weapon = self.hero.weapon.name
                    enemy_health = self.enemy.get_health()
                    return s + "Hero hits with {} for {} dmg. Enemy health is {}".format(weapon, dmg, enemy_health)
        print(command)

    def enemy_attack(self):
        attack_type = "magic" # self.enemy.attack_type()
        if attack_type == "magic":
            if self.enemy.can_cast():
                spell = self.enemy.spell.name
                dmg = self.enemy.attack("magic")
                self.hero.take_damage(dmg)
                hero_health = self.hero.get_health()
                return "Enemy cast a {}, hits hero for {} dmg. Hero health is {}".format(spell, dmg, hero_health)
            else:
                if self.distance > 1:
                    self.distance -= 1
                    return "Enemy moves one position."
                else:
                    attack_type = random.choice(["weapon", None])
        if attack_type is None:
            if self.distance > 1:
                self.distance -= 1
                return"Enemy moves one position."
            else:
                dmg = self.enemy.attack()
                self.hero.take_damage(dmg)
                hero_health = self.hero.get_health()
                return "Enemy hits hero for {}. Hero health is {}".format(dmg, hero_health)
        if attack_type == "weapon":
            if self.distance > 1:
                self.distance -= 1
                return "Enemy moves one position."
            else:
                weapon = self.enemy.weapon.name
                dmg = self.enemy.attack("weapon")
                self.hero.take_damage(dmg)
                hero_health = self.hero.get_health()
                return "Enemy hits with {} hero for {}. Hero health id {}".format(weapon, dmg, hero_health)
