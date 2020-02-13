# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
        self.inventory = []
    def move(self, new_room):
        self.cur_room = new_room
    def on_take(self, item):
        self.inventory.append(item)
    def on_drop(self, item):
        item_index = self.inventory.index(item)
        self.inventory.pop(item_index)