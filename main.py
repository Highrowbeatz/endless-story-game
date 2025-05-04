from game_mechanics import add_to_story, is_valid_sentence
from save_load import list_saves, load_game, save_story
import random

def generate_ai_story_segment(current_story):
    """
    Generates the next part of the story using AI or predefined logic.
    This function simulates an AI-generated story segment.
    """
    # Example predefined story continuations. Replace with an AI model for dynamic generation.
    story_segments = [
        "The sun set beautifully as the horizon painted itself in hues of orange and purple.",
        "A mysterious figure appeared in the distance, carrying a lantern that flickered in the wind.",
        "Suddenly, a loud roar echoed through the forest, sending chills down their spine.",
        "The journey ahead seemed treacherous, but determination burned brightly in their heart.",
        "The ancient map hinted at treasures untold, but danger lurked in every corner."
    ]
    return random.choice(story_segments)

def start_game():
    """
    Starts a new story and manages the game loop with AI-generated story segments.
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
            ai_segment = generate_ai_story_segment(story)
            story = add_to_story(story, ai_segment)
            print("Updated story:")
            print(story)
        else:
            print("Invalid sentence. Please try again!")
