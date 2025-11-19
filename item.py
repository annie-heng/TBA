# Define the Item class.

class Item:
    """
    This class represents a Item. A Item is composed of a name, a description, and at least one exit.

    Attributes :
        name (str) : The name of the Item.
        description (str) : A detailed description of the Item.
        exits (dict) : a dict object. The keys are the directions, and the value associated with a key is the corresponding Item.

    Methods : 
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : If the requested direction is available, return the corresponding Item. If not, returns None.
        get_exit_string(self) : The string listing all of the available exits/directions. 
        get_long_description(self) : The detailed description of the Item, followed by the exits list. 

    Examples :

    >>> kitchen = Item("Kitchen", "dans une cuisine moderne et bien illuminée.")
    >>> livingItem = Item("LivingItem", "dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.")
    >>> kitchen.exits['N'] = livingItem
    >>> livingItem.exits['S'] = kitchen
    >>> kitchen.name
    'cuisine'
    >>> kitchen.description
    'dans une cuisine moderne, bien illuminée et adjacente au salon.'
    >>> livingItem.exits
    {'S' : kitchen}
    >>> kitchen.get_exit_string()
    "Sorties : N"
    >>> livingItem.get_long_description() 
    "Vous êtes dans un salon où se trouve une table basse et un grand canapé en face d'un téléviseur.

    Sorties : S
    "

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.weight = 0