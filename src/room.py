# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        # the below attributes are defined in adv.py, but leaving this just in case
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
        self.item_list = []
    def add_item(self, item):
        self.item_list.append(item)
    def remove_item(self, item):
        item_index = self.item_list.index(item)
        self.item_list.pop(item_index)