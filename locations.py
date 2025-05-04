# locations.py
# This file contains functionality to manage story locations.

class Location:
    """
    Represents a location in the story.
    """
    def __init__(self, name, description):
        """
        Initializes a new location.
        
        Args:
            name (str): The name of the location.
            description (str): A brief description of the location.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the location.
        """
        return f"{self.name}: {self.description}"


def add_location(locations, name, description):
    """
    Adds a new location to the list of locations.
    
    Args:
        locations (list): The list of existing locations.
        name (str): The name of the new location.
        description (str): A brief description of the new location.

    Returns:
        list: The updated list of locations.
    """
    new_location = Location(name, description)
    locations.append(new_location)
    return locations


def list_locations(locations):
    """
    Lists all the locations in the game.
    
    Args:
        locations (list): The list of locations.

    Returns:
        None
    """
    print("=== Story Locations ===")
    for location in locations:
        print(location)


if __name__ == "__main__":
    # Example usage of locations
    story_locations = []
    story_locations = add_location(story_locations, "Enchanted Forest", "A mystical forest full of magical creatures.")
    story_locations = add_location(story_locations, "Deserted Island", "An isolated island surrounded by turquoise waters.")
    
    list_locations(story_locations)
