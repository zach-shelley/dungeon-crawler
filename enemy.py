import random

class Enemy:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.hp = 45
        self.ac = 10
        self.damage = 15
        self.to_hit_bonus = 0
        # moving skeleton up bc I did not create enemy dictionary to map enemy object creation
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

    def check_to_hit(self, bide_counter, user):
        roll = random.randint(1, 20)
        is_crit = roll == 20
        is_hit = (roll + self.to_hit_bonus - bide_counter) >= user.ac

        return is_hit, is_crit
    
    def attack(self):
        return self.damage 

    def critical_attack(self):
        return self.damage * 2

class Skeleton(Enemy):
    def __init__(self, name, items):
        super().__init__(name, items)
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
        


# skeleton_portrait_strike = """  
#                    ／  ⌒ ＼
#         　　　　\/  l_0..0_l
#         　　　　/\　  l冊l
# 　　　　　　　　-=-v=-
# 　　　　　　　　}{ 彡ミﾉ{
# 　　　　　　　　}{　非　}{
# 　　　　　　　 匁 OTO) 匁
# 　　　　　　　　　}{　}{
# 　　　　　　　　　}{　}{
# 　　　　　　　　  及  及"""
