# Define the Character class.

class Character():
    """
    This class represents a character. A character is composed of a name, a description, an current location and a list of messages.

    Attributes:
        name (str): The name of the NPC.
        description (str) : The description of the NPC.
        current_room (Room) : The room where the character is currently located.
        msgs(list) : The list of messages to print when the player interacts with the NPC.
        

    Methods:
        __init__(self, name) : The constructor.
        

    Examples:
    >>> from room import Room
    >>> sam = Character("Sam")
    >>> sam.name
    "Sam"
    >>> kitchen = Room("cuisine", "Kitchen", "dans une cuisine moderne et bien illuminée.")
    >>> sam.current_room = kitchen
    >>> bathroom = Room("Bathroom", "dans une salle de bain assez petite, pourvue d'une douche.")
    >>> kitchen.exits['N'] = bathroom
    >>> bathoom.exits['S'] = kitchen
    >>> sam.current_room.name
    "Bathroom"

    """

    # Define the constructor.
    def __init__(self, name, description,current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"{self.name} : {self.description}"