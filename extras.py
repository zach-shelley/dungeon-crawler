import json
import os
from create_character import create_character

def display_menu():
    print("=" * 60)
    print("Welcome to the Dungeon of Doom!".center(60))
    print("=" * 60)

def auto_save(player_obj, game_data):
    save = {
        "player" : {
            "type" : player_obj.type,
            "name" : player_obj.name,
            "location" : player_obj.location,
            "items" : player_obj.items,
            "hp" : player_obj.hp,
        },
        "rooms" : game_data
        }
    os.makedirs("data/saves", exist_ok=True)
    with open(f"data/saves/autosave.json", "w") as json_file:
        json.dump(save, json_file)

def load_save(json_file):
    with open(json_file, "r") as saved_data:
        save = json.load(saved_data)
        player = create_character(save)
        saved_room_data = save["rooms"]

        return player, saved_room_data
    
def initiate_game(room_data):
    display_menu()
    ready_to_play = False
    while not ready_to_play:
        ready_var = input("Are you ready to begin your quest? y/n ")
        if ready_var.lower() == 'y':
            ready_to_play = True
    load_game = input("Load save? Y/N")
    if load_game.lower() == "y":
        if os.path.exists("data/saves/autosave.json"):
            user, room_data = load_save("data/saves/autosave.json")
            print(f"Welcome back {user.name}!")
    else:
        user = create_character()
        print(user.name + " has entered the dungeon!")

    return user, room_data

def play_again():

    while True:
        user_choice = input("Would you like to play again? y/n ")
        if user_choice.lower() == 'y': 
            return True
        elif user_choice.lower() == 'n':
            return False
        else:
            print("Invalid input: Please answer Y/N")