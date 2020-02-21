from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
items = {
    'money':Item('money','One million dollar'),
    'cat':Item('cat','Two cute cate'),
    'dog':Item('dog','Three big dog'),
}

def addItemsToRooms():
    print('Adding Items to Room')
    room['outside'].add_item(items['money'])
    room['outside'].add_item(items['cat'])
    room['outside'].add_item(items['dog'])

addItemsToRooms()

#room['foyer'].add_item(Item('money','One million dollar'))

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

#current_room.get_items()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

def movePlayer(player, dir):
    if dir == 'n':
        if player.current_room.n_to:
            player.move_to(player.current_room.n_to)
        else:
            print('There is no more room to the north')
    elif dir == 's':
        if player.current_room.s_to:
            player.move_to(player.current_room.s_to)
        else:
            print('There is no more room to the south')
    elif dir == 'e':
        if player.current_room.e_to:
            player.move_to(player.current_room.e_to)
        else:
            print('There is no more room to the east')
    elif dir == 'w':
        if player.current_room.w_to:
            player.move_to(player.current_room.w_to)
        else:
            print('There is no more room to the west')
    elif dir == 'i' or dir == 'inventory':
        player.get_items()
    else:
        print('Only "n","e","w","s" keys are allowed')

def take_item(player, item):
    current_room = player.current_room
    if len(current_room.get_items()) > 0:
        current_room.remove_item(item)
        player.take_item(item)
        #print(f'{current_room.name} does not have {item}')



def drop_item(player, item):
    current_room = player.current_room
    if len(player.get_items()) > 0:
        player.drop_item(item)
        current_room.add_item(item)
        #print(f'{player.name} does not have {item}')


actions = {'take': take_item, 'drop': drop_item}

def start():
    print('>>>>>>>>>>>>  Starting game')

    player = Player('ellen', room['outside'])
    while True:
        dir = (input('What do you want to do?').lower())
        if dir == 'q':
            return False
        keywords = dir.split()
        if len(keywords) == 1:
            movePlayer(player, dir)
        else:
            key = keywords[0]
            item_name = keywords[1]
            if items[item_name]:
                actions[key](player, items[item_name])
            else:
                print('This item is not in the list')


start()
