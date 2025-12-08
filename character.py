from game import DEBUG
import random 
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
        move(self) : Move the character to an adjacent room with a one in two chance. If the randomly chosen room is the cave, cancel the movement.
        

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

    # Define the move method
    def move(self):
        l = [x for x in self.current_room.exits.values() if x != None]
        r = random.choice([0, 1])
        if r == 0 :
            next_room = random.choice(l)
            #A NPC can not go inside the cave.
            if next_room.name == "Cave":
                return False
            #Remove the NPC from the current room.
            del self.current_room.characters[self.name]

            self.current_room = next_room
            #Add the NPC to the new room.
            self.current_room.characters[self.name] = self
            return True
        return False