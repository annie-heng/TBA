# Define the Player class.
class Player():
    """
    This class represents a player. A player is composed of a name, and a current location.

    Attributes:
        name (str): The name of the player.
        current_room (Room) : The room where the player is currently located.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Get the next room from the exits dictionary of the current room, set it as the current room and return True. If the next room is None, print an error message and return False.

    Examples:
    >>> from room import Room
    >>> sam = Player("Sam")
    >>> sam.name
    "Sam"
    >>> kitchen = Room("cuisine", "Kitchen", "dans une cuisine moderne et bien illuminée.")
    >>> sam.current_room = kitchen
    >>> bathroom = Room("Bathroom", "dans une salle de bain assez petite, pourvue d'une douche.")
    >>> kitchen.exits['N'] = bathroom
    >>> bathoom.exits['S'] = kitchen
    >>> sam.move('N')
    >>> sam.current_room.name
    "Bathroom"

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True
    
    #Define the get_history method.
    def get_history(self) :

        #If the player has not moved, return a string indicating that no moves have been made yet.
        if len(self.history) == 0 :
            return "Vous n'avez pas encore d'historique, déplacez-vous !\n"

        history_string = "Votre parcours est le suivant : \n"
        #Add the Room description to history_string for each Room in self.history.
        for place in self.history :
            history_string += f"\t- {place.description}\n"
        return history_string