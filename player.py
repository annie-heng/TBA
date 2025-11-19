# Define the Player class.
class Player():
    """
    This class represents a player. A player is composed of a name, and a current location.

    Attributes:
        name (str): The name of the player.
        current_room (Room) : The room where the player is currently located.
        history (list) : The list containing all the rooms that the player has visited, excluding the current one.
        inventory(dict) : The inventory of the player, in the form of a dict object where each key is the item's name and the value is the corresponding Item object.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Get the next room from the exits dictionary of the current room, set it as the current room and return True. If the next room is None, print an error message and return False.
        get_history(self) : Return a string that contains a list of all the rooms that the player has visited, in order. If the history attribute is empty, return the corresponding message.
        move_back(self) : Get the last object of the history attribute, removes it from self.history and set it as the current room.
        get_inventory(self) : Return a string of the contents of the player's inventory.

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
    True
    >>> sam.current_room.name
    "Bathroom"

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
    
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
        #print(self.get_history())
        return True
    
    #Define the get_history method.
    def get_history(self) :

        #If the player has not moved, return a string indicating that no moves have been made yet.
        if len(self.history) == 0 :
            return "\nVous n'avez pas encore d'historique, déplacez-vous !\n"

        history_string = "\nVotre parcours est le suivant : \n"
        #Add the Room description to history_string for each Room in self.history.
        for place in self.history :
            history_string += f"\t- {place.description}\n"
        return history_string

    #Define the move_back method
    def move_back(self) :

        #If the player has no history, print an error message and return False.
        if len(self.history) == 0 :
            print("\nImpossible de retourner en arrière ! Votre historique est vide.\n")
            return False

        #Set the current room to the previous room.
        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        #print(self.get_history())
        return True

    #Define the get_inventory method.
    def get_inventory(self) :

        #If the inventory is empty, return a string indicating that no Item is present in the inventory.
        if len(self.inventory) == 0 :
            return "\nVotre inventaire est vide.\n"

        inventory_string = "\nVous disposez des items suivants : \n"
        
        for item in self.inventory.values() :
            #For each Item in the inventory, list it's name, description and weight.
            inventory_string += f"\t - {item.name} : {item.description} ({item.weight} kg)"
        return inventory_string