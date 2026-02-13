import json
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