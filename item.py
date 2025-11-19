# Define the Item class.

class Item:
    """
    This class represents a item. A item is composed of a name, a description, and at least one exit.

    Attributes :
        name (str) : The name of the item.
        description (str) : A detailed description of the item.
        exits (dict) : a dict object. The keys are the directions, and the value associated with a key is the corresponding item.

    Methods : 
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : If the requested direction is available, return the corresponding item. If not, returns None.
        get_exit_string(self) : The string listing all of the available exits/directions. 
        get_long_description(self) : The detailed description of the item, followed by the exits list. 

    Examples :

    >>> kitchen = item("Kitchen", "dans une cuisine moderne et bien illuminée.")
    >>> livingitem = item("Livingitem", "dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.")
    >>> kitchen.exits['N'] = livingitem
    >>> livingitem.exits['S'] = kitchen
    >>> kitchen.name
    'cuisine'
    >>> kitchen.description
    'dans une cuisine moderne, bien illuminée et adjacente au salon.'
    >>> livingitem.exits
    {'S' : kitchen}
    >>> kitchen.get_exit_string()
    "Sorties : N"
    >>> livingitem.get_long_description() 
    "Vous êtes dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.

    Sorties : S
    "

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the item in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the item's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this item including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
