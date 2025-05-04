from game_mechanics import add_to_story, is_valid_sentence
from save_load import list_saves, load_game, save_story
import random

def start_game():
    """
    Starts a new story and manages the game loop.
    """
    story = "Once upon a time"
    print("Your story begins:")
    print(story)

    while True:
        new_sentence = input("Add to the story (or type 'exit' to quit): ")
        if new_sentence.lower() == "exit":
            save_choice = input("Would you like to save your story? (yes/no): ").strip().lower()
            if save_choice == "yes":
                save_name = input("Enter a name for your save file: ").strip()
                save_story(save_name, story)
            print("Thank you for playing!")
            break

        if is_valid_sentence(new_sentence):
            story = add_to_story(story, new_sentence)
            print("Updated story:")
            print(story)
        else:
            print("Invalid sentence. Please try again!")

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
