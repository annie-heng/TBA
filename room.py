# Define the Room class.

class Room:
    """
    This class represents a room. A room is composed of a name, a description, and at least one exit.

    Attributes :
        name (str) : The name of the room.
        description (str) : A detailed description of the room.
        exits (dict) : a dict object. The keys are the directions, and the value associated with a key is the corresponding room.
        inventory(dict) : The inventory of the player, in the form of a dict object where each key is the item's name and the value is the corresponding Item object.

    Methods : 
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : If the requested direction is available, return the corresponding room. If not, returns None.
        get_exit_string(self) : The string listing all of the available exits/directions. 
        get_long_description(self) : The detailed description of the room, followed by the exits list. 
        get_inventory(self) : Return a string of the contents of the player's inventory.

    Examples :

    >>> kitchen = Room("Kitchen", "dans une cuisine moderne et bien illuminée.")
    >>> livingroom = Room("LivingRoom", "dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.")
    >>> kitchen.exits['N'] = livingroom
    >>> livingroom.exits['S'] = kitchen
    >>> kitchen.name
    'cuisine'
    >>> kitchen.description
    'dans une cuisine moderne, bien illuminée et adjacente au salon.'
    >>> livingroom.exits
    {'S' : kitchen}
    >>> kitchen.get_exit_string()
    "Sorties : N"
    >>> livingroom.get_long_description() 
    "Vous êtes dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.

    Sorties : S
    "

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    #Define the get_inventory method.
    def get_inventory(self) :

        #If the inventory is empty, return a string indicating that no Item is present in the Room.
        if len(self.inventory) == 0 :
            return "\nIl n'y a rien ici.\n"

        inventory_string = "\nLa pièce contient : \n"
        
        for item in self.inventory.values() :
            #For each Item in the Room, list it's name, description and weight.
            inventory_string += f"\t - {item.name} : {item.description} ({item.weight} kg)"
        return inventory_string
