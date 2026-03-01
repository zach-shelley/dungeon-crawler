
def handle_items_pickup(player, items, individual):
    """
    Standalone function handling item pickup based on user input for individual item pickup or batch. 
    Inputs: the player object, the selected items, user_input on batch/individual
    """
    
    if not individual:
        for item in items[:]:
            if len(player.items) >= player.max_items:
                print("Inventory full. Must drop items")
                break
          
            player.items.append(item)
            items.remove(item)
            
    else:
        for item in items[:]:
            if len(player.items) >= player.max_items:
                print("Inventory full. Must drop items.")
                break

            pickup_item = input(f"Pickup {item}? y/n")
            if pickup_item.lower() == "y":
                player.items.append(item)
                items.remove(item)
            
            continue
        
  

        