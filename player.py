import random

class Player:
    def __init__(self, name, location):
        self._items = []
        self.name = name
        self.location = location
        self.to_hit_bonus = 0
        self.bide_bonus = 1
        self.ac = 0
        self.bide_counter = 0

    @property
    def items(self):
        return self._items
    
    def add_starting_items(self, items):
        self.items.extend(items)
        
    def drop_item(self, item):
        self.items.remove(item)

    def pick_up_items(self, items):
        pickup_choice = input("Pickup all items ('a') or item by item ('i')")
        individual = False
        if pickup_choice == "i":
            individual = True
        items_to_remove = []
        for item in items:
            if len(self.items) >= self.max_items:
                print("Inventory full - must drop items")
                break
            if individual:
                choice = input("y/n")
                if choice != "y":
                    continue
            
            self.items.append(item)
            items_to_remove.append(item)
        for i in items_to_remove:
            items.remove(i)
            
    def view_inventory(self):
        return ", ".join(self.items)
    
    def check_hit(self, bide_count, target):
        roll = random.randint(1, 20)
        is_crit = roll == 20
        is_hit = (roll + self.to_hit_bonus + bide_count) >= target.ac
        return is_hit, is_crit
    
    def attack(self):
        return self.damage  

    def critical_attack(self):
        raise NotImplementedError("Critical attack must be defined at the subclass level for class based multipliers.")
    
class Elf(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = "elf"
        self.max_items = 5
        self.add_starting_items(["Bow"])
        self.hp = 50
        self.damage = 4
        self.to_hit_bonus = 3
        self.ac = 13

    def critical_attack(self):
        return self.damage * 3
    

class Dwarf(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = "dwarf"
        self.max_items = 10
        self.add_starting_items(["Great axe"])
        self.hp = 100
        self.damage = 8
        self.to_hit_bonus = 0
        self.ac = 8
    
    def critical_attack(self):
        return self.damage * 2


class Ranger(Player):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.type = "ranger"
        self.max_items = 8
        self.add_starting_items(["Longsword"])
        self.hp = 75
        self.damage = 6
        self.to_hit_bonus = 1
        self.bide_bonus = 2
        self.ac = 12
        
    
    def critical_attack(self):
        return self.damage * 1.75