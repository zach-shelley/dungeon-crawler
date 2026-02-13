import json
import random
from player import Player
from enemy import Enemy
from create_character import create_character
from extras import auto_save, display_menu

# combat, length check for max items, and item by item pickup are TODOs

def main():
    """
    Main application loop.
    Displays menu, gets user input, processes choices.
    """
    with open("data/rooms.json", "r") as f: 
        room_data = json.load(f)

    display_menu()
    ready_to_play = False
    while not ready_to_play:
        ready_var = input("Are you ready to begin your quest? y/n ")
        if ready_var.lower() == 'y':
            ready_to_play = True
    
    user = create_character()
    print(user.name + " has entered the dungeon!")

    playing = True
    while playing:
        
        print("\n")
        current_room = room_data[user.location]
        available_exits = current_room["exits"]
        paths = " or ".join(available_exits.keys())
        user_decision = input(f"{user.name} is in {user.location}, {current_room["description"]} - Choose {user.name}'s next action \n Pick a path: {paths}, \n View Inventory: 'v' \n Investigate Room : 'i' ")
        if user_decision.lower() == "i":
            if not current_room["items"]:
                print('\nRoom investigated, no items found...')
                continue
            print(f"\n{user.name} investigates {user.location} and finds items: {', '.join(current_room["items"])}")
            user.pick_up_items(current_room["items"])
            print(f"\nNew inventory: {user.view_inventory()}")
        elif user_decision.lower() == "v":
            print(f"\n{user.name}'s inventory: {user.view_inventory()}")

        elif user_decision in available_exits:
            if available_exits[user_decision] == "Escape":
                print(f"{user.name} escaped the dungeon!")
                playing = False
            elif available_exits[user_decision] == "trap":
                print(f"A hidden lever activates a trap and an arrow impales {user.name}. \n Game over")
                playing = False
            elif available_exits[user_decision].get("riddle"):
                riddle = random.choice(available_exits["user_decision"]["riddle"])
                user_answer = input(f"{riddle["question"]}")
                if user_answer.lower() == riddle["answer"]:
                    print("The lock clicks and the door creaks open as you enter a secret room")
                    user.location = available_exits[user_decision]
            else:
                user.location = available_exits[user_decision]
        else:
            print(f"{user.name} cannot go that direction.")

        auto_save(user, room_data)

    play_again = input("Would you like to play again? y/n ")
    if play_again.lower() == 'y': 
        main()
    elif play_again.lower() == 'n':
        exit()

if __name__ == "__main__":
    main()
