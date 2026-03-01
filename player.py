import random

class Character:
    def __init__(self, name, location = "Unknown"):
        self._items = []
        self.max_items = -1
        self.name = name
        self.location = location
        self.to_hit_bonus = 0
        self.bide_bonus = 1
        self.ac = -1
        self.bide_counter = -1
        self.damage = -1
        self.portrait = ""

    @property
    def items(self):
        return self._items
    
    def add_starting_items(self, items):
        self.items.extend(items)
        
    def drop_item(self, item):
        self.items.remove(item)
            
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
    
class Elf(Character):
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
    

class Dwarf(Character):
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


class Ranger(Character):
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
    
class Skeleton(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 5
        self.ac = 9
        self.damage = 15
        self.to_hit_bonus = 1
        self.portrait = """ 
               ／  ⌒ ＼
　　　　　　　　 l_0..0_l
　　　　　　　　　 l冊l
　　　　　　　　-=-v=-
　　　　　　　　}{ 彡ミﾉ{
　　　　　　　　}{　非　}{
　　　　　　　 匁 OTO) 匁
　　　　　　　　　}{　}{
　　　　　　　　　}{　}{
　　　　　　　　  及  及"""
        
    def critical_attack(self):
        return self.damage * 1.5
    
class Zombie(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 5
        self.ac = 8
        self.damage = 9
        self.to_hit_bonus = 1
        self.portrait = """
      (()))
                               /|x x|
                              /\( - )
                      ___.-._/\/
                     /=`_'-'-'/  !!
                     |-{-_-_-}     !
                     (-{-_-_-}    !
                      \{_-_-_}   !
                       }-_-_-}
                       {-_|-_}
                       {-_|_-}
                       {_-|-_}
                       {_-|-_}  ZOT
                   ____%%@ @%%_______
"""

    def critical_attack(self):
        return self.damage * 1.5

class Vampire(Character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 20
        self.ac = 14
        self.damage = 15
        self.to_hit_bonus = 2
        self.portrait = """
                /######\
               /##########\
              /   \###/    \
             /     \#/      \
          /\|               |/\
          | | \ ==\    /== / | |
           \|  \<|>\  /<|>/  |/     /|
    \__     |    -   \  -    |     /#|
     \#\     |        |      |   /###|
      \##\   |       \|     |  /#####|
       \###\  |   _______  | /######|
        \####\ | / \/ \/ \|/#######|
        |######\|        |#########|
        |########\______/##########|
        |#########\    /##########/
        |##########\  |#########/\
        /###########\/########/###\
    /################\######/########\
   /##################\###/###########\
  /###################\#/##############\
 /####################/#################\
/###################/####################\
"""


    def critical_attack(self):
        return self.damage * 2