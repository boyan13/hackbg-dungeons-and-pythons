import arcade
import os
import copy
from Dungeon import Dungeon
from Fight import Fight
from Hero import Hero
from Weapon import Weapon
from Spell import Spell
from Enemy import Enemy

COLUMN_SPACING = 40
ROW_SPACING = 40
LEFT_MARGIN = 120
BOTTOM_MARGIN = 530
SPRITE_SCALING = 1

# Important constants for this example

# Speed limit
MAX_SPEED = 3.0

# How fast we accelerate
ACCELERATION_RATE = 0.1

# How fast to slow down after we letr off the key
FRICTION = 0.02


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.dungeon = None
        self.hero = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.move_char = (".", [0, 0])
        self.fight = Fight()
        arcade.set_background_color((59, 68, 75))

    def setup(self):
        self.dungeon = Dungeon("map.txt")
        self.hero = Hero("Geralt", "white wolf", 150, 150, 5)
        self.hero.equip(Weapon("Sword", 30))
        self.hero.learn(Spell("wolf's attack", 20, 20, 2))
        self.dungeon.spawn(self.hero)
        self.command = None

    def on_draw(self):
        arcade.start_render()

        x = self.dungeon.borders[1] * 20 + LEFT_MARGIN - 20
        y = 260
        arcade.draw_rectangle_filled(x, y, 410, 410, (135, 169, 107))
        arcade.draw_rectangle_outline(x , y, 420, 420, (105, 53, 156), 10)
        arcade.draw_text("To move pres the keybord arrows.\nTo attack first you should choose\ndirection. Press on of the keys:\n 'u' for up, 'd' for down,\n 'l' for left, 'r' for right\n......................................",\
            x - 200, y + 100, (55, 3, 106), 14)

        # Prints the map
        for row in range(self.dungeon.borders[0]):
            # Loop for each column
            for column in range(self.dungeon.borders[1]):
                # Calculate our location
                x = column * COLUMN_SPACING + LEFT_MARGIN
                y = (self.dungeon.borders[0] - row - 1) * ROW_SPACING + BOTTOM_MARGIN

                # Draw the item
                if (self.dungeon.matrix[row][column] == "#"):
                    arcade.draw_rectangle_filled(x, y, 30, 30, (191, 79, 81))
                elif (self.dungeon.matrix[row][column] == "-"):
                    if row == 0 or row == self.dungeon.borders[0] - 1:
                        if column == 0 or column == self.dungeon.borders[1] - 1:
                            arcade.draw_rectangle_filled(x, y, 30, 30, (59, 68, 75))
                        else:
                            arcade.draw_rectangle_filled(x, y, 50, 30, (59, 68, 75))
                    if column == 0 or column == self.dungeon.borders[1] - 1:
                        if row == 0 or row == self.dungeon.borders[0] - 1:
                            arcade.draw_rectangle_filled(x, y, 30, 30, (59, 68, 75))
                        else:
                            arcade.draw_rectangle_filled(x, y, 30, 50, (59, 68, 75))
                elif (self.dungeon.matrix[row][column] == "H"):
                    arcade.draw_rectangle_filled(x, y, 30, 30, (79, 134, 247))
                    arcade.draw_text("H", x - 10, y - 20, arcade.color.BLUE, 28)
                elif (self.dungeon.matrix[row][column] == "E"):
                    arcade.draw_rectangle_filled(x, y, 30, 30, (255, 117, 24))
                    arcade.draw_text("E", x - 10, y - 20, arcade.color.RED, 28)
                elif (self.dungeon.matrix[row][column] == "T"):
                    arcade.draw_rectangle_filled(x, y, 30, 30, (150, 120, 182))
                    arcade.draw_text("T", x - 10, y - 20, (55, 3, 106), 28)
                elif (self.dungeon.matrix[row][column] == "G"):
                    arcade.draw_rectangle_filled(x, y, 30, 30, (153, 230, 179))
                    arcade.draw_text("G", x - 10, y - 20, (0, 130, 127), 28)
                else:
                    arcade.draw_rectangle_filled(x, y, 30, 30, (135, 169, 107))

        x = self.dungeon.borders[1] * 20 + LEFT_MARGIN - 20
        y = self.dungeon.borders[1] * 10 + BOTTOM_MARGIN
        arcade.draw_rectangle_outline(x , y, 420, 220, (105, 53, 156), 10)

    def on_update(self, delta_time):
        """
        if self.up_pressed and not self.down_pressed:
            self.dungeon.move_hero("up")
        elif self.down_pressed and not self.up_pressed:
            self.dungeon.move_hero("down")
        if self.left_pressed and not self.right_pressed:
            self.dungeon.move_hero("left")
        elif self.right_pressed and not self.left_pressed:
            self.dungeon.move_hero("left")
        """

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:

            self.move_char = self.dungeon.move_hero("up")
            print("HERREEEEERERERER")#, self.move_hero)

            self.check_move()
            #self.up_pressed = True
        elif key == arcade.key.DOWN:

            self.move_char = self.dungeon.move_hero("down")
            self.check_move()
            #self.down_pressed = True
        elif key == arcade.key.LEFT:

            self.move_char = self.dungeon.move_hero("left")
            self.check_move()
            # self.left_pressed = True
        elif key == arcade.key.RIGHT:

            self.move_char = self.dungeon.move_hero("right")
            self.check_move()
            # self.right_pressed = True

        elif key == arcade.key.NUM_1 or key == arcade.key.KEY_1:
            self.command = self.fight.get_hero_command(1)

        elif key == arcade.key.NUM_2 or key == arcade.key.KEY_2:
            print('hhhhhhh')
            self.command = self.fight.get_hero_command(2)
            print(self.command)

        elif key == arcade.key.NUM_3 or key == arcade.key.KEY_3:
            self.command = self.fight.get_hero_command(3)

        elif key == arcade.key.NUM_4 or key == arcade.key.KEY_4:
            self.command = self.fight.get_hero_command(4)


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def check_move(self):
        print("nznznz", self.move_char)
        if self.move_char[0] == "E":
            print("WTF???")
            #fight = Fight()
            self.dungeon.hero = self.battle(1)
            if self.dungeon.hero.is_alive():
                self.dungeon.change_map(".")
                self.dungeon.hero_place[self.move_char[1]] = self.move_char[2]
                self.dungeon.change_map("H")
        else :
            return "Hero made move."

    def battle(self, distance):
        enemy = self.dungeon.enemies.pop()
        self.fight.start_fight(self.dungeon.hero, enemy, distance)
        while self.dungeon.hero.is_alive() and enemy.is_alive():
            # the desition of the player
            # self.fight.distance = distance
            if self.dungeon.hero.is_alive():
                print(self.command)
                if self.command is not None:

                    if enemy.is_alive():
                        print(self.fight.hero_attack())
                        if not enemy.is_alive():
                            print("Enemy is dead.")
                if self.enemy.is_alive():
                    if self.hero.is_alive():
                        print(self.fight.enemy_attack())
                        if not self.dungeon.hero.is_alive():
                            print("Hero is dead")
        return self.hero

def main():
        window = MyGame(700, 800, "Dungeon and pythons")
        window.setup()
        arcade.run()

if __name__ == '__main__':
    main()
