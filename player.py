class Player:
    def __init__(self, name, location):
        self._items = []
        self.name = name
        self.location = location

    @property
    def items(self):
        return self._items
        
    def drop_item(self, item):
        self.items.remove(item)

# work through length check w/ testing
    def pick_up_items(self, items):
        for item in items:
            if self.items > self.max_items:
                print("Inventory full - must drop items")
                return 
            else:
                self.items.append(item)
        
    def view_inventory(self):
        return ", ".join(self.items)
    
class Elf(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.pick_up_items(["Bow"])
        self.hp = 50
        self.mana  = 50
        self.max_item = 5

class Dwarf(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.pick_up_items(["Great axe"])
        self.hp = 100
        self.mana = 30
        self.max_items = 10

class Ranger(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.pick_up_items(["Longsword"])
        self.hp = 75
        self.mana = 40
        self.max_items = 8
        