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