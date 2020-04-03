import unittest
from Dungeon import Dungeon

class test_Dungeon(unittest.TestCase):
	
	def test_extract_loot(self):
		e = None
		expected = {
			"loot": {
				"weapons" : {
					"0" : {
						"name" : "Winter",
						"damage" : 45
					},
					"1" : {
						"name" : "Quickfang",
						"damage" : "AARD"
					}
				},
				"spells" : {
					"0" : {
						"name" : "AARD",
						"damge" : 20,
						"mana_cost" : 10,
						"cast_range" : 3
					},
					"1" : {
						"name" : "IGNI",
						"damge" : 50,
						"mana_cost" : 30,
						"cast_range" : 1
					}
				}
			}
		}

		try:
			res = Treasure.extract_loot_dictionary("basic_loot_list_example.json")
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()