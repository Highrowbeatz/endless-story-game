from story_generator_with_npcs import generate_story_with_npcs, interact_with_npc, NPC

def main():
    # Initialize NPCs
    npc_list = [
        NPC(name="Alex", gender="Male"),
        NPC(name="Sophia", gender="Female"),
    ]

    # Initial story setup
    current_story = "Once upon a time in a magical kingdom, a brave adventurer set out on a quest."

    while True:
        # Display the NPCs
        print("\nNPCs:")
        for i, npc in enumerate(npc_list, 1):
            print(f"{i}. {npc.name} ({npc.get_relationship_status()})")

        # Ask the user to choose an NPC to interact with
        npc_choice = input("Choose an NPC to interact with (1-2 or 'q' to quit): ").strip()
        if npc_choice.lower() == 'q':
            print("Thanks for playing!")
            break

        try:
            npc_index = int(npc_choice) - 1
            selected_npc = npc_list[npc_index]

            # Display interaction choices
            print("\nHow would you like to interact?")
            print("1. Be kind")
            print("2. Be rude")
            print("3. Flirt")
            interaction_choice = int(input("Enter your choice (1-3): ").strip())

            # Process the interaction
            interaction_result = interact_with_npc(selected_npc, interaction_choice)
            print(interaction_result)

            # Generate the next part of the story
            print("\nStory Continuation:")
            current_story = generate_story_with_npcs(current_story, selected_npc)
            print(current_story)

        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
