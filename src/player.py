# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, cur_room):
        self.name = name
        self.cur_room = cur_room
    def move(self, new_room):
        self.cur_room = new_room