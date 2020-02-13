from room import Room
# pylint throws error here, but imports work fine
from player import Player
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
room['outside'].add_item('candles')
room['foyer'].add_item('hatchet')
room['overlook'].add_item('flint')
room['narrow'].add_item('map')
room['treasure'].add_item('glasses')
# Make a new player object that is currently in the 'outside' room.
current_room = 'outside'
explorer = Player('Gary', room['outside'])
choices = ['n', 's', 'e', 'w']
def blocked():
    print('\nPath blocked! Try again...\n\n\n\n')
# Write a loop that:
while True:
    print('type q to quit')
    print('Movement Controls: n,s,e,w = move north,south,east,west')
    print('Item Controls: type [get/drop] [item] with one space between to get or drop an item')
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
    print(f'\n      current location: ***{explorer.cur_room.location}*** \n         **visible items: {explorer.cur_room.item_list}')
    print(f'\n      --{explorer.cur_room.description} ')
    
# * Waits for user input and decides what to do.
    cmd = input(" \nEnter command: ").split(' ')
    

    if cmd[0] == 'n':
        print('\n\n\n(You proceed north...)\n\n\n\n\n')
        if hasattr(explorer.cur_room, 'n_to'):
            explorer.move(explorer.cur_room.n_to)
        else:
            blocked()  
    elif cmd[0] == 's':
        print('\n\n\n(You proceed south...)\n\n\n\n\n')
        if hasattr(explorer.cur_room, 's_to'):
            explorer.move(explorer.cur_room.s_to)
        else:
            blocked()
    elif cmd[0] == 'e':
        print('\n\n\n(You proceed east...)\n\n\n\n\n')
        if hasattr(explorer.cur_room, 'e_to'):
            explorer.move(explorer.cur_room.e_to)
        else:
            blocked()
    elif cmd[0] == 'w':
        print('\n\n\n(You proceed west...)\n\n\n\n\n')
        if hasattr(explorer.cur_room, 'w_to'):
            explorer.move(explorer.cur_room.w_to)
        else:
            blocked()
    elif cmd[0] == 'q':
        print('Goodbye! Hope you had fun!')
        break
    elif cmd[0] == 'i' or cmd[0] == 'inventory':
        print(f'\n\n\n******** my inventory: {explorer.inventory} **************')
    elif cmd[0] == 'get' and cmd[1] != None:
        if cmd[1] in explorer.cur_room.item_list:
            explorer.on_take(cmd[1])
            explorer.cur_room.remove_item(cmd[1])
        else:
            print('\n\n\nThat item is not in this room!\n\n\n')
    elif cmd[0] == 'drop' and cmd[1] != None:
        if cmd[1] in explorer.inventory:
            explorer.on_drop(cmd[1])
            explorer.cur_room.add_item(cmd[1])
        else:
            print('\n\n\nYou do not have that item!\n\n\n')
    else:
        print('invalid entry, refer to the movement and item controls')
    
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
