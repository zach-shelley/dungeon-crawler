from player import Skeleton, Zombie, Vampire

enemy_dict = {
    "vampire" : Vampire, 
    "skeleton" : Skeleton,
    "zombie" : Zombie
}

def create_enemy(enemy_type, items):

    return enemy_dict[enemy_type](enemy_type.title(), items)