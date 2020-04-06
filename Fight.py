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
        print("Fight is started")
        self.hero = hero
        self.enemy = enemy
        self.distance = distance
        '''
        print(self.hero.get_health(), self.enemy.get_health())
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
        '''

    def hero_attack(self):
        # gets hero's move/attack
        command = self.get_hero_command()
        print(command)
        s = ""
        if command == "pass":
            self.hero.take_mana()
            return"Pass the turn."
        if command == "move":
            if self.distance > 1:
                self.distance -= 1
            self.hero.take_mana()
            return"Hero moves one position."
        if command == "weapon" or command == "spell":
            print('hereeeeee')
            if command == "spell":
                if self.hero.can_cast():
                    return self.hero_attack_by(command)
                else:
                    s = "Hero can not cast spell. \n"
                    command = "weapon"
            if (command == "weapon"):
                if self.distance > 1:
                    self.hero.take_mana()
                    return s + "Pass the turn."
                else:
                    return s + self.hero_attack_by(command)

    def enemy_attack(self):
        attack_type = "magic" # self.enemy.attack_type()
        if attack_type == "magic":
            if self.enemy.can_cast():
                return self.enemy_attack_by(attack_type)
            else:
                if self.distance > 1:
                    return self.enemy_move()
                attack_type = random.choice(["weapon", None])
        if attack_type is None:
            if self.distance > 1:
                return self.enemy_move()
            return self.enemy_attack_by(attack_type)
        if attack_type == "weapon":
            if self.distance > 1:
                return self.enemy_move()
            return self.enemy_attack_by(attack_type)

    def enemy_move(self):
        self.distance -= 1
        return "Enemy moves one position."

    def enemy_attack_by(self, type=None):
        dmg = self.enemy.attack(type)
        self.hero.take_damage(dmg)
        hero_health = self.hero.get_health()
        if type is None:
            return "Enemy hits hero for {}. Hero health is {}".format(dmg, hero_health)
        if type == "magic":
            spell = self.enemy.spell.name
            return "Enemy cast a {}, hits hero for {} dmg. Hero health is {}".format(spell, dmg, hero_health)
        if type == "weapon":
            weapon = self.enemy.weapon.name
            return "Enemy hits with {} hero for {}. Hero health id {}".format(weapon, dmg, hero_health)

    def get_hero_command(self, comm):
        command_list = {1: "spell", 2: "weapon", 3: "move", 4: "pass"}
        command = int(comm)
        return command_list[command]

    def hero_attack_by(self, type):
        dmg = self.hero.attack(type)
        self.enemy.take_damage(dmg)
        enemy_health = self.enemy.get_health()
        if type == "spell":
            spell = self.hero.spell.name
            return "Hero cast a {}, hits enemy for {} dmg. Enemy health is {}".format(spell, dmg, enemy_health)
        if type == "weapon":
            weapon = self.hero.weapon.name
            return "Hero hits with {} for {} dmg. Enemy health is {}".format(weapon, dmg, enemy_health)
