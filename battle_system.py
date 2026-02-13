from enemy import Enemy

def combat(user, target):
    print("""
___________.___  ________  ___ ______________._.
╲_   _____╱│   │╱  _____╱ ╱   │   ╲__    ___╱│ │
 │    __)  │   ╱   ╲  ___╱    ~    ╲│    │   │ │
 │     ╲   │   ╲    ╲_╲  ╲    Y    ╱│    │    ╲│
 ╲___  ╱   │___│╲______  ╱╲___│_  ╱ │____│    __
     ╲╱                ╲╱       ╲╱            ╲╱ """)

    print(f'\n\n {target.portrait}')
    print(f'{user.name} is attacked by a {target.name}')

    user.bide_counter = 0
    while user.hp > 0 and target.hp > 0:
        battle_round(user, target)
    
    if user.hp <= 0:
        return "dead"
    return "won"

def battle_round(user, target):

    player_turn(user, target)
    if target.hp > 0:
        enemy_turn(user, target)

def player_turn(user, target):

    battle_choice = input('user.name will...\n\nFight - Attack The Creature!\n\nBide - Watch and wait, look for a good time to strike! ')

    if battle_choice.lower() == 'fight':
    
        is_hit, is_crit = user.check_hit(user.bide_counter, target)
        user.bide_counter = 0
        if is_crit:
            print(f'{user.name} hit the {target.name}!\n \n CRITICAL HIT!')
            target.hp -= user.critical_attack()
            if target.hp <= 0:
                print(f"The {target.name} dies")
                return
        elif is_hit:
            print(f'{user.name} hit the {target.name}!')
            target.hp -= user.attack()
            if target.hp <= 0:
                print(f"The {target.name} dies")
                return
        elif not is_hit:
            print(f'{user.name} missed!')
    
    elif battle_choice.lower() == 'bide':
        print(f'{user.name} watches his prey closely, keeping light on his feet')
        user.bide_counter += user.bide_bonus
        print(f"{user.name}'s next attack will get + {user.bide_counter} to hit!")

def enemy_turn(user, target):
    is_hit, is_crit = target.check_to_hit(user.bide_counter, user)
    if is_crit:
        print(f'{target.name} has landed a critical hit!')
        critical_hit = target.critical_attack()
        user.hp -= critical_hit
        if user.hp <= 0:
            print("Player has died")
            return 
        print(f'{user.name} takes {critical_hit} damage\nRemaining health: {user.hp}')
    
    elif is_hit:
        print(f'{target.name} has hit {user.name}!')
        attack = target.attack()
        user.hp -= attack
        if user.hp <= 0:
            print("Player has died")
            return 
        print(f'{user.name} takes {attack} damage!\nRemaining health: {user.hp}')

    elif not is_hit:
        print(f'{user.name} dodges the attack!')

