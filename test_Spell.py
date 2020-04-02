import unittest
from Spell import Spell

class test_Spell(unittest.TestCase):

	def test_validate_init(self):
		e1, e2, e3, e4, e5, e6 = None, None, None, None, None, None
		
		try: # VALID
			Spell.validate_init(name = "Fireball", damage = 30, mana_cost = 50, cast_range = 2)
		except Exception as exc:
			e1 = exc
		try: # DAMAGE = 0
			Spell.validate_init(name = "Fireball", damage = 0, mana_cost = 50, cast_range = 2)
		except ValueError as exc:
			e2 = exc
		try: # DAMAGE < 0
			Spell.validate_init(name = "Fireball", damage = -1, mana_cost = 0, cast_range = 2)
		except ValueError as exc:
			e3 = exc
		try: # MANA_COST = 0
			Spell.validate_init(name = "Fireball", damage = 30, mana_cost = 0, cast_range = 2)
		except ValueError as exc:
			e4 = exc
		try: # MANA_COST < 0
			Spell.validate_init(name = "Fireball", damage = 30, mana_cost = -1, cast_range = 2)
		except ValueError as exc:
			e5 = exc
		try: # CAST_RANGE < 0
			Spell.validate_init(name = "Fireball", damage = 30, mana_cost = 50, cast_range = -1)
		except ValueError as exc:
			e6 = exc	

		self.assertIsNone(e1) 	 # VALID
		self.assertIsNotNone(e2) # DAMAGE = 0
		self.assertIsNotNone(e3) # DAMAGE < 0
		self.assertIsNotNone(e4) # MANA_COST = 0
		self.assertIsNotNone(e5) # MANA_COST < 0
		self.assertIsNotNone(e6) # CAST_RANGE < 0

		self.assertEqual(str(e2), "Spell with negative or no damage value.")
		self.assertEqual(str(e3), "Spell with negative or no damage value.")
		self.assertEqual(str(e4), "Spell with negative or no mana cost.")
		self.assertEqual(str(e5), "Spell with negative or no mana cost.")
		self.assertEqual(str(e6), "Spell with negative cast range.")

if __name__ == '__main__':
	unittest.main()