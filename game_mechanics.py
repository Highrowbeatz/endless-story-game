# game_mechanics.py
# This file contains the core mechanics for the Endless Story Game.

def add_to_story(current_story, new_sentence):
    """
    Adds a new sentence to the current story.
    
    Args:
        current_story (str): The story so far.
        new_sentence (str): The sentence to add to the story.

    Returns:
        str: The updated story.
    """
    if not new_sentence.endswith(('.', '!', '?')):
        new_sentence += '.'
    
    return current_story + " " + new_sentence

def is_valid_sentence(sentence):
    """
    Validates the new sentence to ensure it meets game rules.
    
    Args:
        sentence (str): The sentence to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return bool(sentence.strip())

if __name__ == "__main__":
    # Example usage of the game mechanics
    story = "Once upon a time"
    print("Current story:", story)

    while True:
        new_sentence = input("Add to the story: ")
        if is_valid_sentence(new_sentence):
            story = add_to_story(story, new_sentence)
            print("Updated story:", story)
        else:
            print("Invalid sentence. Please try again!")
