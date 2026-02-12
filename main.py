"""
Week 2 Final Project - Starter Code
Console Application Template

This is a basic structure to get you started. Modify it for your project!
"""
import keyboard

def display_menu():
    """
    Show the main menu to the user.
    Customize this for your application.
    """
    print("\n" + "="*40)
    print("  My Console Application")
    print("="*40)
    print("1. Do something")
    print("2. Do something else")
    print("3. Show information")
    print("help - Show this menu")
    print("quit - Exit application")
    print()


def handle_choice(choice):
    """
    Process the user's choice and call appropriate functions.
    
    Args:
        choice (str): The user's input
        
    Returns:
        bool: True to continue, False to exit
    """
    if choice == "1":
        print("You chose option 1!")
        # TODO: Call your function here
        
    elif choice == "2":
        print("You chose option 2!")
        # TODO: Call your function here
        
    elif choice == "3":
        print("You chose option 3!")
        # TODO: Call your function here
        
    elif choice == "help":
        display_menu()
        
    elif choice == "quit":
        print("Thanks for using the application. Goodbye!")
        return False
        
    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")
    
    return True


def main():
    """
    Main application loop.
    Displays menu, gets user input, processes choices.
    """
    print("Welcome to the Dungeon of Doom!")
    print("PRESS SPACEBAR TO START!")
    display_menu()
    
    running = True
    while running:
        choice = input("Enter your choice: ").strip().lower()
        running = handle_choice(choice)


if __name__ == "__main__":
    main()
