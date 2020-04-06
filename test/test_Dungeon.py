import unittest
#from Dungeon import Dungeon
#from Hero import Hero
#from Weapon import Weapon
#from Spell import Spell


class test_Dungeon(unittest.TestCase):
    def test_extract_loot(self):
        e = None
        expected = {
            "loot": {
                "weapons": {
                    "0": {
                        "name": "Winter",
                        "damage": 45
                    },
                    "1": {
                        "name": "Quickfang",
                        "damage": "AARD"
                    }
                },
                "spells": {
                    "0": {
                        "name": "AARD",
                        "damge": 20,
                        "mana_cost": 10,
                        "cast_range": 3
                    },
                    "1": {
                        "name": "IGNI",
                        "damge": 50,
                        "mana_cost": 30,
                        "cast_range": 1
                    }
                }
            }
        }

        try:
            res = Dungeon.extract_loot_dictionary("basic_loot_list_example.json")
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(res, expected)

    def test_move_hero_wrong_direction(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        self.assertFalse(d.move_hero("up"))

    def test_move_hero_(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.move_hero("right")
        d.move_hero("down")
        d.move_hero("right")
        d.move_hero("down")
        self.assertEqual(d.hero_place, [2, 1])

    def test_check_for_enemy_right(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.hero.learn(Spell("idk", 20, 20, 2))
        d.hero_place = [3, 1]
        d.change_map("H")
        result = d.check_for_enemy("right")
        self.assertEqual(result, 1)

    def test_check_for_enemy_left(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.hero.learn(Spell("idk", 20, 20, 2))
        d.hero_place = [3, 4]
        d.change_map("H")
        result = d.check_for_enemy("left")
        self.assertEqual(result, 2)

    def test_check_for_enemy_up(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.hero.learn(Spell("idk", 20, 20, 2))
        d.hero_place = [3, 5]
        d.change_map("H")
        result = d.check_for_enemy("up")
        self.assertEqual(result, 1)

    def test_check_for_enemy_down(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.hero.learn(Spell("idk", 20, 20, 2))
        d.hero_place = [0, 5]
        d.change_map("H")
        result = d.check_for_enemy("down")
        self.assertEqual(result, 2)
    """
    def test_check_for_enemy_down(self):
        d = Dungeon('map.txt', 'basic_loot_list_example.json')
        d.spawn(Hero("nz", "nz", 200, 120, 2))
        d.hero.learn(Spell("idk", 20, 20, 2))
        d.hero_place = [0, 5]
        d.change_map("H")
        result = d.check_for_enemy("up")
        self.assertEqual(result, 0)
    """
    

if __name__ == '__main__':
    unittest.main()
