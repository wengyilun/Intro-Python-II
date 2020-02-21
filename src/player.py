# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room
		self.inventory = []
		print(self.__str__())
		print(self.current_room.get_items())

	def move_to(self, room):
		self.current_room = room
		print(f'!!!Player has moved to {self.current_room.name}')
		print(self.current_room.get_items())

	def take_item(self, item):
		print(item)
		self.inventory.append(item)
		item.on_take()

	def drop_item(self, item):
		self.inventory.remove(item)
		item.on_drop()

	def get_items(self):
		if len(self.inventory) > 0:
			print(f'!!!{self.name} now has these items:')
			for item in self.inventory:
				print(f'{item}')
		else:
			print(f'!!!{self.name} does not have any item left')


		return self.inventory

	def __str__(self):
		return f'{self.name} is at {self.current_room.name}'