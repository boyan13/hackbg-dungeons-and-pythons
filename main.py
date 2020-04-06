from Hero import Hero
from Weapon import Weapon
from Spell import Spell
from Dungeon import Dungeon

def print_commands():
    print("\nEnter command:")
    print("    -move up: mu, move down: md, move left: ml, move right: mr")
    print("    -attack up: au, attack down: ad, attack left: al, attack right: ar\n")
    print("    -command menu: h")

def main():
    hero_name = input("Enter hero's name: ")
    hero_title = input("Enter hero's title: ")
    hero = Hero(hero_name, hero_title, 150, 150, 5)
    hero.equip(Weapon("Sword", 30))
    hero.learn(Spell("KillALL", 35, 30, 3))
    dungeon = Dungeon("map.txt", "basic_loot_list_example.json")
    dungeon.spawn(hero)


    dict_commands = {"mu": "up", "md": "down", "ml": "left", "mr": "right", "au": "up", "ad": "down", "al": "left", "ar": "right", "h": "help"}
    dict_commands_move = {"mu": "up", "md": "down", "ml": "left", "mr": "right"}
    dict_commands_attack = {"au": "up", "ad": "down", "al": "left", "ar": "right"}

    index_of_hero = [1, 1]

    print_commands()

    while not dungeon.end_of_game:
        dungeon.print_map()
        print()
        player_input = ""
        while player_input not in dict_commands.keys():

            player_input = str(input(">>> "))
        if player_input == "h":
            print_commands()
        if player_input in dict_commands_move.keys():
            dungeon.move_hero(dict_commands_move[player_input])
        if player_input in dict_commands_attack.keys():
            dungeon.hero_atack(dict_commands_attack[player_input])
        if dungeon.end_of_game:
            break


    

if __name__ == '__main__':
    main()
