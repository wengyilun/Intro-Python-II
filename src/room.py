# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description,
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.items = []


	def n_to(self, room):
		self.n_to = room

	def s_to(self, room):
		self.s_to = room

	def e_to(self, room):
		self.e_to = room

	def w_to(self, room):
		self.w_to = room

	def add_item(self, item):
		self.items.append(item)
		print(f'{item.name} ({item.description}) is added to {self.name}')

	def remove_item(self, item):
		self.items.remove(item)

	def get_items(self):
		if len(self.items) > 0:
			print(f'{self.name} has these items before:')
			for item in self.items:
				print(f'{item.name}:{item.description}')
		else:
			print(f'{self.name} has no items')

		return self.items

	def __str__(self):
		return f'{self.name}{self.description} \n {self.get_items}'