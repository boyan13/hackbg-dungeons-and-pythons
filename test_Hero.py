import unittest
from Hero import Hero

class Test_hero(unittest.TestCase):
	def test_known_as(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		result = h.known_as()
		self.assertEqual(result, "Geralt the White wolf")
	def test_get_health(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		result = h.get_health
		self.assertEqual(result, 100)
	def test_get_mana(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		result = h.get_mana
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
	#TODO more test for can_cast()
	def test_get_demage(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		result = h.get_damage(25)
		self.assertEqual(h.get_health, 75)
	def test_get_healing_lt_max_health(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		h.get_damage(50)
		result = h.get_healing(25)
		self.assertEqual(h.get_health, 75)
		self.assertTrue(result)
	def test_get_healing_mt_max_health(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		h.get_damage(10)
		result = h .get_healing(20)
		self.assertTrue(result)
		self.assertEqual(h.get_health, 100)
	def test_get_healing_hero_is_dead(self):
		h = Hero("Geralt", "White wolf", 100, 100, 5)
		h.get_damage(110)
		result = h.get_healing(100)
		self.assertFalse(result)
	#TODO test for take_mana() eqipt() learn() attack()
	

if __name__ == '__main__':
	unittest.main()