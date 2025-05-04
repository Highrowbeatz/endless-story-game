from game_mechanics import add_to_story, is_valid_sentence
from save_load import list_saves, load_game, save_story
from dotenv import load_dotenv
import os
import random
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Instantiate the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_story_segment(current_story):
    """
    Generates the next part of the story using OpenAI's GPT model.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a storytelling AI that continues stories in an engaging and immersive way."
                },
                {
                    "role": "user",
                    "content": f"Continue the following story in an immersive and engaging way: {current_story}"
                }
            ],
            max_tokens=150
        )
        # Extract the AI response text
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating AI story segment: {e}")
        # Fallback to a predefined story segment in case of an error
        return random.choice([
            "The sun set beautifully as the horizon painted itself in hues of orange and purple.",
            "A mysterious figure appeared in the distance, carrying a lantern that flickered in the wind.",
            "Suddenly, a loud roar echoed through the forest, sending chills down their spine.",
        ])

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
