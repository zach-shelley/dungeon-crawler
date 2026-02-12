class Player:
    def __init__(self, name, location):
        # self.hp = hp
        self._items = []
        self.name = name
        self.location = location

    @property
    def items(self):
        return self._items
    
    
    def drop_item(self, item):
        self.items.remove(item)

    def pick_up_item(self, item):
        self.items.append(item)

    def view_inventory(self):
        return self.items