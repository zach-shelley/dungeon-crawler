from player import Ranger, Elf, Dwarf

def create_character(save_data = None):

    classes = {
        "dwarf" : Dwarf,
        "ranger" : Ranger,
        "elf" : Elf
    }

    if save_data:
        player_data = save_data["player"]
        player = classes[player_data["type"]](player_data["name"], player_data["location"])
        player._items = player_data["items"]
        player.hp = player_data["hp"]
        return player
    
    character_name = input("Choose a name for your hero ")
    
    character_created = False
    while not character_created:
        character_class = input("Choose a class for your hero: Dwarf, Ranger, Elf ")

        if character_class.lower() in classes:
            user = classes[character_class.lower()](character_name, "The Mouth of the Hall")
            character_created = True
        else:
            print("Invalid input. Please enter one of the available class options.")

    return user