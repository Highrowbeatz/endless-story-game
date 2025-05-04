import random
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    exit(1)

# Instantiate the OpenAI client
client = OpenAI(api_key=api_key)

def generate_ai_story_segment(client, current_story):
    """
    Generates the next part of the story using OpenAI's GPT model.
    Falls back to a predefined story segment in case of an error.
    """
    try:
        # Use the best available model for story generation
        response = client.chat.completions.create(
            model="gpt-4.1",  # Replace this with a model available to you
            messages=[
                {
                    "role": "system",
                    "content": "You are a creative storytelling AI. Continue the story in an immersive and engaging way."
                },
                {
                    "role": "user",
                    "content": f"Continue the following story: {current_story}"
                }
            ],
            max_tokens=150  # Adjust token limit as needed
        )
        # Extract the AI-generated story segment
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error generating AI story segment: {e}")
        # Fallback predefined story segments
        return random.choice([
            "The sun set beautifully as the horizon painted itself in hues of orange and purple.",
            "A mysterious figure appeared in the distance, carrying a lantern that flickered in the wind.",
            "Suddenly, a loud roar echoed through the forest, sending chills down their spine.",
        ])

def main():
    current_story = "Once upon a time, in a land far, far away..."
    next_segment = generate_ai_story_segment(client, current_story)
    print("Next segment of the story:")
    print(next_segment)

if __name__ == "__main__":
    main()
