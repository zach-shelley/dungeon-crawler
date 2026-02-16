import json
import random
from player import Player
from enemy import Enemy
from create_character import create_character
from create_enemy import create_enemy
from extras import auto_save, load_save, display_menu
from battle_system import combat

def main():
    """
    Main application loop.
    Displays menu, gets user input, processes choices.
    """
    while True:

        with open("data/rooms.json", "r") as f: 
            room_data = json.load(f)

        display_menu()
        ready_to_play = False
        while not ready_to_play:
            ready_var = input("Are you ready to begin your quest? y/n ")
            if ready_var.lower() == 'y':
                ready_to_play = True
        load_game = input("Load save? Y/N")
        if load_game.lower() == "y":
            user, room_data = load_save("data/saves/autosave.json")
        else:
            user = create_character()
            print(user.name + " has entered the dungeon!")

        playing = True
        while playing:
            
            print("\n")
            current_room = room_data[user.location]
            available_exits = current_room["exits"]
            paths = " or ".join(available_exits.keys())
            if current_room.get("enemy"):
                enemy_data = current_room["enemy"]
                print(enemy_data["description"])
                enemy = create_enemy(enemy_data["type"], enemy_data["items"])
                result = combat(user, enemy)
                if result == "dead":
                    playing = False
                    continue
            user_decision = input(f"{user.name} is in {user.location}, {current_room["description"]} - Choose {user.name}'s next action \n Pick a path: {paths}, \n View Inventory: 'v' \n Investigate Room : 'i' ")
            if user_decision.lower() == "i":
                if current_room.get("hidden_chest"):
                    print("While investigating the room, you find a chest!")
                    if 'bronze key' in user.items:
                        print("You insert the key and the chest clicks open...")
                        user.pick_up_items(current_room["hidden_chest"])
                        current_room["hidden_chest"].clear()
                    else:
                        print("It appears the chest is locked...")
                if not current_room["items"]:
                    print('\nAfter investigating the room, no loose items were found...')
                    continue
                print(f"\n{user.name} investigates {user.location} and finds items: {', '.join(current_room['items'])}")
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
                elif room_data[available_exits[user_decision]].get("riddle"):
                    riddle = random.choice(room_data[available_exits[user_decision]]["riddle"])
                    user_answer = input(f"{riddle['question']}")
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
            continue
        elif play_again.lower() == 'n':
            break

if __name__ == "__main__":
    main()
