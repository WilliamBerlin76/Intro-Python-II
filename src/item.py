class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LightSource(Item):
    def __init__(self, name, description, light_type):
        super().__init__(name, description)
        self.light_type = light_type