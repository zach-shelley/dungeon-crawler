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

    def pick_up_items(self, items):
        self.items.extend(items)

    def view_inventory(self):
        return ", ".join(self.items)