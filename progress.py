# progress.py
# This file contains functionality to track and display game progress.

def track_progress(player_turns, current_story):
    """
    Tracks the progress of the game by displaying player turns and the story length.
    
    Args:
        player_turns (int): The number of turns players have taken.
        current_story (str): The current state of the story.

    Returns:
        str: A summary of the game progress.
    """
    story_length = len(current_story.split())
    progress_summary = (
        f"Player turns taken: {player_turns}\n"
        f"Current story length: {story_length} words\n"
    )
    return progress_summary

def display_progress_summary(player_turns, current_story):
    """
    Displays the game progress summary to players.
    
    Args:
        player_turns (int): The number of turns players have taken.
        current_story (str): The current state of the story.
    """
    print("=== Game Progress ===")
    print(track_progress(player_turns, current_story))

if __name__ == "__main__":
    # Example usage of progress tracking
    player_turns = 5
    current_story = "Once upon a time, there was a coder who loved storytelling."
    
    display_progress_summary(player_turns, current_story)
