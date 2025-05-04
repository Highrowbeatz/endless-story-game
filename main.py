from game_mechanics import add_to_story
from save_load import list_saves, load_game
import random

def main_menu():
    print("Welcome to the Endless Story Game!")
    print("1. Start a new story")
    print("2. Load a saved game")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        start_game()
    elif choice == "2":
        saves = list_saves()
        if not saves:
            print("No saved games available. Starting a new story.")
            start_game()
        else:
            print("Available saves:")
            for i, save_name in enumerate(saves):
                print(f"{i + 1}. {save_name}")
            save_choice = input("Enter the number of the save to load: ")
            if save_choice.isdigit() and 1 <= int(save_choice) <= len(saves):
                save_name = saves[int(save_choice) - 1]
                load_game(save_name)
            else:
                print("Invalid choice. Returning to main menu.")
                main_menu()
    else:
        print("Invalid choice. Exiting game.")

if __name__ == "__main__":
    main_menu()
