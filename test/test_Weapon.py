import unittest
#from Weapon import Weapon


class Test_weapon(unittest.TestCase):
    def test_validate_weapon_currect(self):
        name = "Skullcrusher"
        damage = 25
        self.assertTrue(Weapon.validate_init(name, damage))

    def test_validate_weapon_incurrect_name(self):
        name = 1234
        damage = 25
        self.assertFalse(Weapon.validate_init(name, damage))

    def test_validate_weapon_incurrect_damage(self):
        name = "Skullcrusher"
        damage = '25'
        self.assertFalse(Weapon.validate_init(name, damage))


if __name__ == '__main__':
    unittest.main()
