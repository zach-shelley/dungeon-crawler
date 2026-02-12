"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""
import json
from player import Player
from enemy import Enemy
import os



def display_menu():
    print("=" * 60)
    print("Welcome to the Dungeon of Doom!".center(60))
    print("=" * 60)

def auto_save(player_obj, game_data):
    save = {
        "player" : {
            "name" : player_obj.name,
            "location" : player_obj.location,
            "items" : player_obj.items
        },
        "rooms" : game_data
        }
    os.makedirs("data/saves", exist_ok=True)
    with open(f"data/saves/autosave.json", "w") as json_file:
        json.dump(save, json_file)

#     print("3. Show information")
#     print("help - Show this menu")
#     print("quit - Exit application")
        
#     elif choice == "help":
#         display_menu()
        
#     elif choice == "quit":
#         print("Thanks for using the application. Goodbye!")
#         return False
        
#     else:
#         print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")

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
    
    # character_name = input("Choose a name for your hero")
    user = Player(input("What is your hero's name? "), "Foyer")
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
            print(f"\nItems picked up: {', '.join(current_room["items"])}'")
            current_room["items"].clear()
        elif user_decision.lower() == "v":
            print(f"\n{user.name}'s inventory: {user.view_inventory()}")

        elif user_decision in available_exits:
            if current_room["exits"][user_decision] == "Escape":
                print(f"{user.name} escaped the dungeon!")
                playing = False
            elif current_room["exits"][user_decision] == "trap":
                print(f"A hidden lever activates a trap and an arrow impales {user.name}. \n Game over")
                playing = False
            else:
                user.location = current_room['exits'][user_decision]
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
