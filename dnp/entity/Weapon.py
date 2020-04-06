class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @staticmethod
    def validate_init(name, damage):
        return type(name) is str and type(damage) is int and damage > 0
