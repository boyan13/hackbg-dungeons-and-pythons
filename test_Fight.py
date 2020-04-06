import unittest
from Fight import Fight
from Hero import Hero
from Weapon import Weapon
from Spell import Spell
from Enemy import Enemy


class TestFight(unittest.TestCase):
    def test_start_fight(self):
        f = Fight()
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.equip(Weapon("Axe", 40))
        h.learn(Spell("Storm", 30, 50, 3))
        e = Enemy(100, 200, 30)
        e.equip(Weapon("Sword", 40))
        e.learn(Spell("Fire", 30, 20, 3))
        d = 2
        h = f.start_fight(h, e, d)
        print('=======================')
        print(h.known_as(), h.get_health())


if __name__ == '__main__':
    unittest.main()

"""
from Fight import Fight
from Hero import Hero
from Weapon import Weapon
from Spell import Spell
from Enemy import Enemy
f = Fight()
h = Hero("Geralt", "White wolf", 200, 100, 5)
h.equip(Weapon("Axe", 40))
h.learn(Spell("Storm", 30, 50, 3))
e = Enemy(100, 40, 10)
e.equip(Weapon("Sword", 40))
e.learn(Spell("Fire", 30, 20, 3))
d = 2
h = f.start_fight(h, e, d)

"""
