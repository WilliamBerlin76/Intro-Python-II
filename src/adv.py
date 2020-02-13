from room import Room
# pylint throws error here, but imports work fine
from player import Player
from item import Item
from item import LightSource
from item import Treasure
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    
    'better_treasure': Room("Chamber of the Wise", """Congratulations, you were not fooled
by the false chamber, and have been rewarded with the Wise Man's treasure! The walls are lined 
with gold. Here is where the true treasure resides""")
}

item = {
    'candles': Item("Candles", """These can light the way, but you need something to light them"""),
    'hatchet': Item('Hatchet', 'This could be used to chop something open...'),
    'flint': Item('Flint', 'Creates a spark, need something to keep the flame...'),
    'burning-candle': LightSource('Burning-candle', 'You can see more clearly now with the light!!', 'flame'),
    'map': Item('Map', 'This map is old, weathered, and slightly transluscent.'),
    'glasses': Item('Glasses', 'Cracked lense, wearing them makes everything blurry'),
    'gold': Treasure('Gold', 'These look valuable!', False),
    'grail': Treasure('Grail', 'Only the rich would drink from this', False),
    'chest': Treasure('Chest', 'There must be something valuable inside', True)
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
room['better_treasure'].s_to = room['overlook']

#
# Main
#
room['outside'].add_item(item['candles'])
room['foyer'].add_item(item['hatchet'])
room['overlook'].add_item(item['flint'])
room['narrow'].add_item(item['map'])
room['treasure'].add_item(item['glasses'])
room['better_treasure'].add_item(item['gold'])
room['better_treasure'].add_item(item['grail'])
room['better_treasure'].add_item(item['chest'])

current_room = 'outside'
explorer = Player('Gary', room['outside'])

def move_msg(c):
    direction = {
        'n': 'north',
        's': 'south',
        'e': 'east',
        'w': 'west'
    }
    print(f'\n\n\n(You proceed {direction[c]}...)\n\n\n\n\n')


# Write a loop that:
while True:
    visible_items = []

    def display_list(items):
        for i in range(len(items)):
            item = items[i].name.lower()
            visible_items.append(item)
    display_list(explorer.cur_room.item_list)
    
    visible_inv = []
    invisible_inv = []
    def display_inv(items):
        for i in range(len(items)):
            item = {"NAME": items[i].name.lower(), 'DESCRIPTION': items[i].description}
            visible_inv.append(item)
            invisible_inv.append(items[i].name.lower())
    
    display_inv(explorer.inventory)
    
        

    print('type q to quit')
    print('type i or "inventory" to see your inventory')
    print('Movement Controls: n,s,e,w = move north,south,east,west')
    print('Item Controls: type [get/drop] [item] with one space between to get or drop an item')

    print(f'\n      **current location: ***{explorer.cur_room.location}*** \n         **visible items: {visible_items}')
    print(f'\n      --{explorer.cur_room.description} ')
    
    if explorer.cur_room is room['overlook'] and item['hatchet'] in room['treasure'].item_list:
        room['overlook'].n_to = room['better_treasure']
        print("""\n         -- Where there was once just an empty chasm,
                there is now a silver moonlit bridge leading to the north""")

    if explorer.cur_room is room['treasure'] and 'burning-candle' in invisible_inv and 'map' in invisible_inv and 'glasses' in invisible_inv and 'hatchet' in invisible_inv:
        explorer.on_drop(item['hatchet'])
        explorer.cur_room.add_item(item['hatchet'])
        print("""\n\nYou feel warmth emanating from the map...
        
        You pull out the map and put on the glasses.
        An arrow appears on the map, pointing to an empty mount shaped for a hatchet,

        You place the hatchet on the mount and hear a low rumble...
        The entire cave shakes, then, silence...
        """)
    
    if item['gold'] in explorer.inventory and item['grail'] in explorer.inventory and item['chest'] in explorer.inventory and explorer.complete == False:
        print("\n\n         You have found the Wise Man;s Treasure!")
        ccmd = input('          Do you wish to continue exploring?[y/n]: ')
        explorer.on_continue(ccmd)
    cmd = input(" \nEnter command: ").lower().split(' ')

    


    if cmd[0] in ['n', 's', 'e', 'w']:
        move_msg(cmd[0])
        explorer.move(cmd[0])
    elif cmd[0] == 'q':
        print('Goodbye! Hope you had fun!')
        break
    elif cmd[0] == 'i' or cmd[0] == 'inventory':
        print(f'\n\n\n******** my inventory: ************\n{visible_inv} \n\n')
    elif cmd[0] == 'get' and cmd[1] != None:
        if cmd[1].lower() in visible_items:
            explorer.on_take(item[cmd[1].lower()])
            explorer.cur_room.remove_item(item[cmd[1].lower()])
        else:
            print('\n\n\nThat item is not in this room!\n\n\n')
    elif cmd[0] == 'drop' and cmd[1] != None:
        if cmd[1].lower() in invisible_inv:
            explorer.on_drop(item[cmd[1].lower()])
            explorer.cur_room.add_item(item[cmd[1].lower()])
        else:
            print('\n\n\nYou do not have that item!\n\n\n')
    else:
        print('invalid entry, refer to the movement and item controls')
    
    if 'candles' in invisible_inv and 'flint' in invisible_inv:
        explorer.on_drop(item['candles'.lower()])
        explorer.on_take(item['burning-candle'.lower()])
        pop_index = invisible_inv.index('candles')
        pop_vindex = visible_inv.index({"NAME": item['candles'].name.lower(), 'DESCRIPTION': item['candles'].description})
        visible_inv.pop(pop_vindex)
        invisible_inv.pop(pop_index)
        display_inv(explorer.inventory)
        print('\n\n\nYou use your flint, to light a candle\n\n\n')
        print(f'******** candles in inventory replaced by: ***********\n{visible_inv[-1]} \n\n')
    

    
    
    