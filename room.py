# Define the Room class.

class Room:
    """
    This class represents a room. A room is composed of a name, a description, an inventory and at least one exit.

    Attributes :
        name (str) : The name of the room.
        description (str) : A detailed description of the room.
        exits (dict) : a dict object. The keys are the directions, and the value associated with a key is the corresponding room.
        inventory(dict) : a dict object that lists all the Items that are present in the room. Keys are the names of the Items, and the values are the corresponding Item objects.
        characters(dict) : a dict object that lists the characters that are present in the room. Keys are the names of the characters, and the values are the corresponding Character objects.
        is_dark (bool) : Indicates if the room is dark; if so, the player cannot use certain commands in this Room.
        image (str) : Path to image file (PNG/JPG) for this room

    Methods : 
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : If the requested direction is available, return the corresponding room. If not, returns None.
        get_exit_string(self) : The string listing all of the available exits/directions. 
        get_long_description(self) : The detailed description of the room, followed by the exits list. 
        get_inventory(self) : Return a string listing the Items and the Characters that are in the room.

    Examples :

    >>> kitchen = Room("Kitchen", "une cuisine moderne et bien illuminée.")
    >>> livingroom = Room("LivingRoom", "un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.")
    >>> kitchen.exits['N'] = livingroom
    >>> livingroom.exits['S'] = kitchen
    >>> kitchen.name
    'Kitchen'
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
    def __init__(self, name, description, is_dark, image = None):
        """
        Initialize a Room with a name and description.
        
        >>> room = Room("Hall", "dans un grand hall")
        >>> room.name
        'Hall'
        >>> room.description
        'dans un grand hall'
        >>> room.exits
        {}
        >>> room.image is None
        True
        """
        self.name = name
        self.description = description
        self.is_dark = is_dark
        self.image = image
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Return the room in the given direction if it exists.
        
        >>> room1 = Room("Room1", "dans une pièce")
        >>> room2 = Room("Room2", "dans une autre pièce")
        >>> room1.exits["N"] = room2
        >>> room1.get_exit("N") == room2
        True
        >>> room1.get_exit("S") is None
        True
        """

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Return a string describing the room's exits.
        
        >>> room1 = Room("Room1", "dans une pièce")
        >>> room2 = Room("Room2", "dans une autre pièce")
        >>> room3 = Room("Room3", "dans une troisième pièce")
        >>> room1.exits["N"] = room2
        >>> room1.exits["E"] = room3
        >>> room1.get_exit_string() # doctest: +ELLIPSIS
        'Sorties: N'
        """
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Return a long description of this room including exits.
        
        >>> room1 = Room("Hall", "dans un grand hall")
        >>> room2 = Room("Kitchen", "dans une cuisine")
        >>> room1.exits["N"] = room2
        >>> print(room1.get_long_description()) # doctest: +ELLIPSIS
        <BLANKLINE>
        Vous êtes dans un grand hall
        <BLANKLINE>
        Sorties: N
        <BLANKLINE>
        """
        if self.is_dark :
            return f"\nVous êtes {self.description}\n\nImpossible de se repérer, il fait trop sombre.\n"
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    #Define the get_inventory method.
    def get_inventory(self) :

        #If the inventory is empty, return a string indicating that no Item is present in the Room.
        if len(self.inventory) == 0 and len(self.characters) == 0 :
            return "\nIl n'y a rien ici.\n"

        inventory_string = "\nOn voit : \n"
        
        for item in self.inventory.values() :
            #For each Item in the Room, list its name, description and weight.
            inventory_string += f"\t - {item.name} : {item.description} ({item.weight} kg)\n"

        for character in self.characters.values() :
            #For each character in the Room, list their name and description.
            inventory_string += f"\t - {character.name} : {character.description}\n"
        return inventory_string
