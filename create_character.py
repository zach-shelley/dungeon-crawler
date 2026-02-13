from player import Ranger, Elf, Dwarf


def create_character():

    classes = {
        "dwarf" : Dwarf,
        "ranger" : Ranger,
        "elf" : Elf
    }

    character_name = input("Choose a name for your hero")
    
    character_created = False
    while not character_created:
        character_class = input("Choose a class for your hero: Dwarf, Ranger, Elf")

        if character_class.lower() in classes:
            user = classes[character_class.lower()](character_name, "Foyer")
            character_created = True
        else:
            print("Invalid input. Please enter one of the available class options.")

    return user