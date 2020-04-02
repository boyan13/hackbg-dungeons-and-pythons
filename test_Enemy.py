import unittest
from Enemy import Enemy	
#from Weapon import Weapon
from Spell import Spell

class test_Enemy(unittest.TestCase):

	def test_validate_init(self):
		e1, e2, e3, e4, e5, e6 = None, None, None, None, None, None

		try: # VALID
			Enemy.validate_init(health = 100, mana = 100, damage = 20) 
		except Exception as exc:
			e1 = exc
		try: # HEALTH = 0
			Enemy.validate_init(health = 0, mana = 100, damage = 20) 
		except ValueError as exc:
			e2 = exc
		try: # HEALTH < 0
			Enemy.validate_init(health = -1, mana = 100, damage = 20) 
		except ValueError as exc:
			e3 = exc
		try: # MANA < 0
			Enemy.validate_init(health = 100, mana = -1, damage = 20) 
		except ValueError as exc:
			e4 = exc
		try: # DAMAGE = 0
			Enemy.validate_init(health = 100, mana = 100, damage = 0) 
		except ValueError as exc:
			e5 = exc
		try: # DAMAGE < 0
			Enemy.validate_init(health = 100, mana = 100, damage = -1) 
		except ValueError as exc:
			e6 = exc

		self.assertIsNone(e1) 	 # VALID
		self.assertIsNotNone(e2) # HEALTH = 0
		self.assertIsNotNone(e3) # HEALTH < 0
		self.assertIsNotNone(e4) # MANA < 0
		self.assertIsNotNone(e5) # DAMAGE = 0
		self.assertIsNotNone(e6) # DAMAGE < 0

		self.assertEqual(str(e2), "Enemy with negative or zero health points.")
		self.assertEqual(str(e3), "Enemy with negative or zero health points.")
		self.assertEqual(str(e4), "Enemy with negative mana points.")
		self.assertEqual(str(e5), "Enemy with negative or no base damage.")
		self.assertEqual(str(e6), "Enemy with negative or no base damage.")

	def test_is_alive(self):
		enemy1 = Enemy(100, 200, 30)
		enemy2 = Enemy(100, 200, 30)
		enemy2.__dict__["health"] = 0

		self.assertTrue(enemy1.is_alive())
		self.assertFalse(enemy2.is_alive())

	def test_can_cast(self):
		spell = Spell(name = "IGNI", damage = 15, mana_cost = 40, cast_range = 1)

		enemy1 = Enemy(100, 50, 30) # Has enough mana
		enemy2 = Enemy(100, 40, 30) # Has just enough mana
		enemy3 = Enemy(100, 30, 30) # Does not have enough mana
		enemy4 = Enemy(100, 0, 30) # Has no mana at all

		enemy1.learn(spell)
		enemy2.learn(spell)
		enemy3.learn(spell)
		enemy4.learn(spell)

		self.assertTrue(enemy1.can_cast())
		self.assertTrue(enemy2.can_cast())
		self.assertFalse(enemy3.can_cast())
		self.assertFalse(enemy4.can_cast())

	def test_attack(self):
		e = None

		sword = Weapon(name = "Viper Sword", damage = 10)
		spell = Spell(name = "IGNI", damage = 15, mana_cost = 40, cast_range = 1)

		enemy = Enemy(100, 200, 5)
		enemy.equip(sword)
		enemy.learn(spell)

		try:
			base_dmg = enemy.attack()
			weapon_dmg = enemy.attack(by = "weapon")
			spell_dmg = enemy.attack(by = "magic")
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(base_dmg, 5)
		self.assertEqual(weapon_dmg, 10)
		self.assertEqual(spell_dmg, 15)

	def test_attack_by_when_enemy_has_no_weapon_or_spell(self):
		e = None
		enemy = Enemy(100, 200, 5)

		try:
			base_dmg = enemy.attack()
			weapon_dmg = enemy.attack(by = "weapon")
			spell_dmg = enemy.attack(by = "magic")
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(base_dmg, 5)
		self.assertEqual(weapon_dmg, 0)
		self.assertEqual(spell_dmg, 0)

	def test_attack_with_bad_key(self):
		e = None
		enemy = Enemy(100, 200, 5)

		try:
			enemy.attack(by = "charisma")
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Failed to execute attack!")

	def test_take_damage(self):
		e = None
		enemy1 = Enemy(100, 50, 30)
		enemy2 = Enemy(100, 50, 30)
		enemy3 = Enemy(100, 50, 30)
		enemy4 = Enemy(100, 50, 30)
		enemy5 = Enemy(100, 50, 30)

		try:
			enemy1.take_damage(10)
			enemy2.take_damage(100)
			enemy3.take_damage(1000)
			enemy4.take_damage(77.44)
			enemy5.take_damage(101.98)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(enemy1.health, 90)
		self.assertEqual(enemy2.health, 0)
		self.assertEqual(enemy3.health, 0)
		self.assertEqual("%.3f" % enemy4.health, "22.560")
		self.assertEqual(enemy5.health, 0)

	def test_equip(self):
		e = None
		sword = Weapon(name = "Viper Sword", damage = 10)
		enemy = Enemy(100, 50, 30)

		try:
			enemy.equip(sword)
		except Exception as exc:
			e = exc 

		self.assertIsNone(e)
		self.assertTrue(enemy.__dict__["weapon"] != None)
		self.assertTrue(enemy.__dict__["weapon"] is sword)

	def test_learn(self):
		e = None
		spell = Spell(name = "IGNI", damage = 15, mana_cost = 40, cast_range = 1)
		enemy = Enemy(100, 50, 30)

		try:
			enemy.learn(spell)
		except Exception as exc:
			e = exc 

		self.assertIsNone(e)
		self.assertTrue(enemy.__dict__["spell"] != None)
		self.assertTrue(enemy.__dict__["spell"] is spell)

if __name__ == '__main__':
	unittest.main()