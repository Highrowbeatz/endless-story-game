# save_load.py
# This file contains save and load functionalities for the Endless Story Game.

import json

def save_story(file_name, story):
    """
    Saves the current story to a JSON file.
    """
    try:
        with open(file_name, 'w') as file:
            json.dump({"story": story}, file)
        print(f"Story saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred while saving the story: {e}")

def load_game(file_name):  # Renamed from load_story
    """
    Loads a story from a JSON file.
    """
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data.get("story", "")
    except FileNotFoundError:
        print(f"No saved story found in {file_name}. Starting a new story.")
        return ""
    except Exception as e:
        print(f"An error occurred while loading the story: {e}")
        return ""

def list_saves(directory="."):
    """
    Lists all available save files (JSON files) in the specified directory.
    """
    try:
        return [f for f in os.listdir(directory) if f.endswith(".json")]
    except Exception as e:
        print(f"An error occurred while listing save files: {e}")
        return []

if __name__ == "__main__":
    # Example usage of save and load functionality
    file_name = "story.json"
    current_story = "Once upon a time, there was a brave coder."
    
    save_story(file_name, current_story)
    loaded_story = load_game(file_name)  # Updated to use load_game
    print("Loaded story:", loaded_story)
    
    saves = list_saves()
    print("Available save files:", saves)
