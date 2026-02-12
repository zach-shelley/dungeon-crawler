"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""
import json
from player import Player
from enemy import Enemy


def display_menu():
    print("=" * 60)
    print("Welcome to the Dungeon of Doom!".center(60))
    print("=" * 60)
#     print("1. Do something")
#     print("2. Do something else")
#     print("3. Show information")
#     print("help - Show this menu")
#     print("quit - Exit application")

# def handle_choice(choice):
#     """
#     Process the user's choice and call appropriate functions.
#   
#     """
#     if choice == "1":
#         print("You chose option 1!")
#         # TODO: Call your function here
        
#     elif choice == "2":
#         print("You chose option 2!")
#         # TODO: Call your function here
        
#     elif choice == "help":
#         display_menu()
        
#     elif choice == "quit":
#         print("Thanks for using the application. Goodbye!")
#         return False
        
#     else:
#         print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")
    
#     return True


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
        user_decision = input(f"{user.name} is in {user.location}, {current_room["description"]} - Choose {user.name} next action \n Pick a path: {paths}, \n View Inventory: 'v' \n Investigate Room : 'i' ")
        if user_decision.lower() == "i":
            if not current_room["items"]:
                print('\nRoom investigated, no items found...')
                continue
            print(f"\n{user.name} investigates {user.location} and finds items: {', '.join(current_room["items"])}")
            user.pick_up_items(current_room["items"])
            print(f"\nYou got {current_room["items"]}!")
            current_room["items"].clear()
        if user_decision.lower() == "v":
            print(f"\n{user.name}'s inventory: {user.view_inventory()}")


            
        elif user_decision in available_exits:
            if current_room["exits"][user_decision] == "Escape":
                print(f"{user.name} escaped the dungeon!")
                playing = False
            else:
                user.location = current_room['exits'][user_decision]
        else:
            print(f"{user.name} cannot go that direction.")


    play_again = input("Would you like to play again? y/n ")
    if play_again.lower() == 'y': 
        main()
    elif play_again.lower() == 'n':
        exit()



if __name__ == "__main__":
    main()
