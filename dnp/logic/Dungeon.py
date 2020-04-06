#from Hero import Hero
#from Weapon import Weapon
#from Spell import Spell
#from Fight import Fight
#from Enemy import Enemy


class Dungeon:
    def __init__(self, text_file, lootListPath):
        self.matrix = []
        with open(str(text_file)) as f:
            self.matrix = f.readlines()
        self.matrix = [x.strip() for x in self.matrix]
        self.hero = None
        self.fight = Fight()
        self.borders = [len(self.matrix), len(self.matrix[0])]
        self.hero_place = []
        self.end_of_game = False
        self.enemy = Enemy(100, 120, 20)
        self.enemy.equip(Weapon("Sword", 40))
        self.enemy.learn(Spell("Fire", 30, 20, 3))

        self.loot_dict = self.__class__.extract_loot_dictionary(lootListPath)

    @classmethod
    def extract_loot_dictionary(cls, filePath):
        with open(filePath, 'r') as f:
            loot_dict = json.load(f)
        return loot_dict

    def print_map(self):
        for line in self.matrix:
            print(line)

    def get_start(self):
        for i in range(len(self.matrix)):
            if 'S' in self.matrix[i]:
                return [i, self.matrix[i].index('S')]
        return [0, 0]

    def get_end(self):
        for i in range(len(self.matrix)):
            if 'G' in self.matrix[i]:
                return [i, self.matrix[i].index('G')]
        return [0, 0]

    def spawn(self, hero):
        self.hero = hero
        if hero.is_alive():
            self.hero_place = self.get_start()
            self.change_map("H")
        else:
            print('End')

    def change_map(self, ch):
        s = list(self.matrix[self.hero_place[0]])
        s[self.hero_place[1]] = ch
        self.matrix[self.hero_place[0]] = "".join(s)

    def move_hero(self, direction):
        directions_vertical = {'up': -1, 'down': 1}
        directions_horisontal = {'left': -1, 'right': 1}
        if direction in directions_vertical.keys():
            next_point = self.hero_place[0] + directions_vertical[direction]
            if next_point > 0 or next_point < self.borders[0]:
                if self.matrix[next_point][self.hero_place[1]] == "#":
                    return False
                elif self.matrix[next_point][self.hero_place[1]] == "E":
                    self.hero_atack(direction)
                elif self.matrix[next_point][self.hero_place[1]] == "T":
                    self.change_map(".")
                    self.hero_place[0] = next_point
                    self.change_map("H")
                    # add treasure
                    print("Found treasure!")
                elif self.matrix[next_point][self.hero_place[1]] == ".":
                    self.change_map(".")
                    self.hero_place[0] = next_point
                    self.change_map("H")
                else:
                    print("End of the game!")
                    print("You won!!!")
            else:
                return False
        if direction in directions_horisontal.keys():
            next_point = self.hero_place[1] + directions_horisontal[direction]
            if next_point > 0 or next_point < self.borders[1]:
                if self.matrix[self.hero_place[0]][next_point] == "#":
                    return False
                elif self.matrix[self.hero_place[0]][next_point] == "E":
                    self.hero_atack(direction)
                elif self.matrix[self.hero_place[0]][next_point] == "T":
                    self.change_map(".")
                    self.hero_place[1] = next_point
                    self.change_map("H")
                    # add treasure
                    print("Found treasure!")
                elif self.matrix[self.hero_place[0]][next_point] == ".":
                    self.change_map(".")
                    self.hero_place[1] = next_point
                    self.change_map("H")
                else:
                    print("End of the game!")
                    print("You won!!!")
            else:
                return False
        return False

    def hero_atack(self, direction):
        distance = self.check_for_enemy(direction)
        if distance == 0:
            print("There is no enemy in hero's ramge")
        else:
            self.hero = self.fight.start_fight(self.hero, self.enemy, distance)
            if not self.hero.is_alive():
                self.end_of_game = True

    def check_for_enemy(self, direction):
        directions_vertical = {'up': -1, 'down': 1}
        directions_horisontal = {'left': -1, 'right': 1}
        spell_range = self.hero.spell.cast_range

        distance = 0

        if direction in directions_vertical.keys():
            for i in range(spell_range + 1):
                index = self.hero_place[0] + i * directions_vertical[direction]
                if index <= 0 or index >= self.borders[1] - 1:
                    break
                if self.matrix[index][self.hero_place[1]] == "#":
                    distance = 0
                    break
                elif self.matrix[index][self.hero_place[1]] == "E":
                    break
                else:
                    distance += 1
            return distance
        if direction in directions_horisontal.keys():
            for i in range(spell_range + 1):
                index = self.hero_place[1] + i * directions_horisontal[direction]
                if index <= 0 or index >= self.borders[1] - 1:
                    break
                if self.matrix[self.hero_place[0]][index] == "#":
                    return 0
                elif self.matrix[self.hero_place[0]][index] == "E":
                    return distance
                else:
                    distance += 1
        return 0


def main():
    d = Dungeon('map.txt')
    d.print_map()
    print('==========')
    d.spawn(Hero("nz", "nz", 200, 120, 2))
    d.print_map()
    print('==========')
    print(d.move_hero('up'))
    d.move_hero('right')
    d.print_map()
    print('==========')
    d.move_hero('down')
    d.print_map()
    print('==========')


if __name__ == '__main__':
    main()
