# Define the Character class.

class Character():
    """
    This class represents a character. A character is composed of a name, a description, an current location and a message.

    Attributes:
        name (str): The name of the player.
        description (str) : The description of the NPC.
        current_room (Room) : The room where the chracter is currently located.
        msgs(list) : The list of messages to print when the player interacts with the NPC.
        

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Get the next room from the exits dictionary of the current room, set it as the current room and return True. If the next room is None, print an error message and return False.
        get_history(self) : Return a string that contains a list of all the rooms that the player has visited, in order. If the history attribute is empty, return the corresponding message.
        move_back(self) : If the history is not empty, get the last object of the history attribute, removes it from self.history, set it as the current room and return True.
        get_inventory(self) : Return a string listing the contents of the player's inventory.
        teleport(self) : Teleports the player to the Room that is contained in the beamer_room attribute.

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

        #Set the current room to the last visited room.
        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        #print(self.get_history())
        return True

    #Define the get_inventory method.
    def get_inventory(self) :

        #If the inventory is empty, return a string indicating that no Item is present in the inventory.
        if len(self.inventory) == 0 :
            return "\nVotre inventaire est vide.\n"+f"\nVotre porte-monnaie contient {self.money} pièces.\n"

        inventory_string = "\nVous disposez des items suivants : \n"
        
        for item in self.inventory.values() :
            #For each Item in the inventory, list its name, description and weight.
            inventory_string += f"\t - {item.name} : {item.description} ({item.weight} kg)\n"
        inventory_string += f"\nVotre sac pèse {self.current_weight} kg\n"
        inventory_string += f"\nVotre porte-monnaie contient {self.money} pièces.\n"
        return inventory_string 
    
    # Define the teleport method.
    def teleport(self) :
        # Check if the beamer is charged.
        if self.beamer_room == None :
            print("\nVous n'avez pas chargé le beamer.\n")
            return False
        
        # Add the current_room to the history.
        self.history.append(self.current_room)
        # Change the current room to the "memorized" room.
        self.current_room = self.beamer_room
        print(self.current_room.get_long_description())
        self.beamer_room = None
        # Delete the beamer from the inventory because it has a one-time use.
        del self.inventory["beamer"]
        return True