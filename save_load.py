# save_load.py
# This file contains save and load functionalities for the Endless Story Game.

import json
import os

def save_story(file_name, story):
    """
    Saves the current story to a JSON file.
    
    Args:
        file_name (str): The name of the file to save the story.
        story (str): The story to save.
    """
    try:
        with open(file_name, 'w') as file:
            json.dump({"story": story}, file)
        print(f"Story saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred while saving the story: {e}")

def load_story(file_name):
    """
    Loads a story from a JSON file.
    
    Args:
        file_name (str): The name of the file to load the story from.

    Returns:
        str: The loaded story, or an empty string if an error occurs.
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
    
    Args:
        directory (str): The directory to search for save files. Defaults to the current directory.

    Returns:
        list: A list of save file names.
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
    
    # Save the story
    save_story(file_name, current_story)
    
    # Load the story
    loaded_story = load_story(file_name)
    print("Loaded story:", loaded_story)
    
    # List available saves
    saves = list_saves()
    print("Available save files:", saves)
