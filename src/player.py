# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
        self.inventory = []
    def move(self, cmd):
        next_room = getattr(self.cur_room, f'{cmd}_to')
        if next_room != None:
            self.cur_room = next_room
        else:
            print('\nPath blocked! Try again...\n\n\n\n')
    def on_take(self, item):
        self.inventory.append(item)
    def on_drop(self, item):
        item_index = self.inventory.index(item)
        self.inventory.pop(item_index)