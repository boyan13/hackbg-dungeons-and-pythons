import unittest
from Hero import Hero
from Spell import Spell
from Weapon import Weapon


class Test_hero(unittest.TestCase):
    def test_validate_init_currect(self):
        name = "Geralt"
        title = "White wolf"
        health = 100
        mana = 100
        mana_rate = 2
        result = Hero.validate_init(name, title, health, mana, mana_rate)
        self.assertTrue(result)

    def test_validate_init_incurect_name(self):
        name = 11111
        title = "White wolf"
        health = 100
        mana = 100
        mana_rate = 2
        result = Hero.validate_init(name, title, health, mana, mana_rate)
        self.assertFalse(result)

    def test_validate_init_title(self):
        name = "Geralt"
        title = 11111
        health = 100
        mana = 100
        mana_regeneration_rate = 2
        self.assertFalse(Hero.validate_init(name, title, health, mana,mana_regeneration_rate))

    def test_validate_init_incurect_mana(self):
        name = "Geralt"
        title = "White wolf"
        health = 100
        mana = '100'
        mana_regeneration_rate = 2
        self.assertFalse(Hero.validate_init(name, title, health, mana,mana_regeneration_rate))

    def test_validate_init_incurect_health(self):
        name = "Geralt"
        title = "White wolf"
        health = -100
        mana = 100
        mana_regeneration_rate = 2
        self.assertFalse(Hero.validate_init(name, title, health, mana,mana_regeneration_rate))

    def test_validate_init_incurect_mana_regeneration_rate(self):
        name = "Geralt"
        title = "White wolf"
        health = 100
        mana = 100
        mana_regeneration_rate = -2
        self.assertFalse(Hero.validate_init(name, title, health, mana,mana_regeneration_rate))

    def test_known_as(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        result = h.known_as()
        self.assertEqual(result, "Geralt the White wolf")

    def test_get_health(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        result = h.get_health()
        self.assertEqual(result, 100)

    def test_get_mana(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        result = h.get_mana()
        self.assertEqual(result, 100)

    def test_is_alive_true(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        self.assertTrue(h.is_alive())

    def test_is_alive_false(self):
        h = Hero("Geralt", "White wolf", 0, 100, 5)
        self.assertFalse(h.is_alive())

    def test_can_cast(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        self.assertFalse(h.can_cast())

    def test_can_cast_no_spell(self):
        h = Hero("Geralt", "White wolf", 0, 100, 5)
        self.assertFalse(h.can_cast())

    def test_can_cast_not_enough_damage(self):
        h = Hero("Geralt", "White wolf", 0, 100, 5)
        h.learn(Spell("Raining death", 50, 120, 5))
        self.assertFalse(h.can_cast())

    def test_can_cast_true(self):
        h = Hero("Geralt", "White wolf", 0, 100, 5)
        h.learn(Spell("Raining death", 50, 20, 5))
        self.assertTrue(h.can_cast())

    def test_take_demage(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.take_damage(25)
        self.assertEqual(h.get_health(), 75)

    def test_take_healing_lt_max_health(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.take_damage(50)
        result = h.take_healing(25)
        self.assertEqual(h.get_health(), 75)
        self.assertTrue(result)

    def test_take_healing_mt_max_health(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.take_damage(10)
        result = h .take_healing(20)
        self.assertTrue(result)
        self.assertEqual(h.get_health(), 100)

    def test_take_healing_hero_is_dead(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.take_damage(110)
        result = h.take_healing(100)
        self.assertFalse(result)

    # TODO test for take_mana() eqipt() learn() attack()
    def test_take_mana_no_arg(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.mana = 0
        h.take_mana()
        self.assertEqual(h.mana, 5)

    def test_take_mana_mt_max_mana(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.mana = 99
        h.take_mana()
        self.assertEqual(h.mana, 100)

    def test_take_mana(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.mana = 0
        h.take_mana()
        self.assertEqual(h.mana, 5)

    def test_take_mana_with_atr(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        h.mana = 0
        h.take_mana(50)
        self.assertEqual(h.mana, 50)

    def test_equip(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        w = Weapon("Skullcrusher", 15)
        h.equip(w)
        self.assertEqual(h.weapon, w)

    def test_learn(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        s = Spell("Raining death", 50, 20, 5)
        h.learn(s)
        self.assertEqual(h.spell, s)

    def test_attack_by_spell(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        s = Spell("Raining death", 50, 20, 5)
        h.learn(s)
        self.assertEqual(h.attack(by='spell'), s.damage)

    def test_attack_no_arg(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        s = Spell("Raining death", 50, 20, 5)
        h.learn(s)
        self.assertEqual(h.attack(), s.damage)

    def test_attack_no_arg_no_spell_no_weapon(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        self.assertEqual(h.attack(), 0)

    def test_attack_no_arg_no_spell(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        w = Weapon("Skullcrusher", 15)
        h.equip(w)
        self.assertEqual(h.attack(), 15)

    def test_attack_by_weapon(self):
        h = Hero("Geralt", "White wolf", 100, 100, 5)
        w = Weapon("Skullcrusher", 15)
        h.equip(w)
        self.assertEqual(h.attack(by='weapon'), 15)


if __name__ == '__main__':
    unittest.main()
