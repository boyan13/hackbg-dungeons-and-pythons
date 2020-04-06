class Spell():

    # Spell class that defines all mana-based weapons ("spells")

    # Constraints:
    #
    #   - mana_cost defines the amount of mana needed to cast the spell
    #   - Casting spells consumes mana
    #   - cast_range defines the max distance (squares away) a hero can engage
    #     an enemy from; cast_range = 1 means a hero can attack an enemy next to them
    #   - Casting range is only calculated in a straight line. Spells cannot be curved

    def __init__(self, name, damage, mana_cost, cast_range):

        self.__class__.validate_init(name, damage, mana_cost, cast_range)

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    @classmethod
    def validate_init(cls, name, damage, mana_cost, cast_range):

        if damage < 1:
            raise ValueError("Spell with negative or no damage value.")
        if mana_cost < 1:
            raise ValueError("Spell with negative or no mana cost.")
        if cast_range < 0:
            raise ValueError("Spell with negative cast range.")