from Weapon import Weapon

class Hero:
	def __init__(self, name, title, health, mana, mana_regeneration_rate):
		self.name = name
		self.title = title
		self.health = health
		self.MAX_HEALTH = health
		self.mana = mana
		self.MAX_MANA = mana
		self.mana_regeneration_rate = mana_regeneration_rate
		self.spell = None
		self.weapon = None


	def known_as(self):
		return f"{self.name} the {self.title}"

	@property
	def get_health(self):
		return self.health
	@property
	def get_mana(self):
		return self.mana

	def is_alive(self):
		if self.health > 0:
			return True
		return False

	def can_cast(self):
		if self.spell == None:
			return False
		if self.mana >= spell.mana_cost:
			return True
		return False

	def get_damage(self, damege_points):
		self.health -= damege_points

	def get_healing(self, healing_points):
		if self.is_alive():
			self.health += healing_points
			if self.health> self.MAX_HEALTH:
				self.health = self.MAX_HEALTH
			return True
		return False

	def take_mana(self):
		pass

	def equip(self, weapon):
		self.weapon = weapon

	def learn(self, spell):
		self.spell = spell

	def attack(self, by = None):
		if  by == "spell":
			if self.can_cast():
				self.mana -= self.spell.mana_cost
				return self.spell.damage
			return 0
		if by == "weapon":
			if self.weapon != None:
				return self.weapon.damage
			return 0
		return 0
	