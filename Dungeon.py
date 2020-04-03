from Hero import Hero
from Weapon import Weapon
from Spell import Spell

class Dungeon:
	def __init__(self, text_file, lootListPath):
		self.matrix = []
		with open(str(text_file)) as f:
			self.matrix = f.readlines()
		self.matrix = [x.strip() for x in self.matrix]
		self.hero = None
		self.borders = [len(self.matrix), len(self.matrix[0])]
		self.hero_place = []

		self.loot_dict = self.__class__.extract_loot_dictionary(lootListPath)
		#self.symbol_under_hero = ""

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
		returtn [0,0]

	def get_end(self):
		for i in range(len(self.matrix)):
			if 'G' in self.matrix[i]:
				return [i, self.matrix[i].index('G')]
		returtn [0,0]

	def spawn(self, hero):
		self.hero = hero
		if hero.is_alive():
			self.hero_place = self.get_start()
			self.change_map("H")
		else:
			print('End')

	def change_map(self,ch):
		self.symbol_under_hero = self.matrix[self.hero_place[0]][self.hero_place[1]]
		s = list(self.matrix[self.hero_place[0]])
		s[self.hero_place[1]]= ch
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
					#attack
					pass
				elif self.matrix[next_point][self.hero_place[1]] == "T":
					self.change_map(".")
					self.hero_place[0] = next_point
					self.change_map("H")
					#add treasure
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
					#attack
					pass
				elif self.matrix[self.hero_place[0]][next_point] == "T":
					self.change_map(".")
					self.hero_place[1] = next_point
					self.change_map("H")
					#add treasure
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

	def hero_atack(self, by = None):
		pass

		

def main():
	d = Dungeon('map.txt')
	d.print_map()
	print('==========')
	d.spawn(Hero("nz","nz",200,120,2))
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