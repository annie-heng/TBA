from game import DEBUG

# Define the Item class.

class Item:
    """
    This class represents a Item. A Item is composed of a name, a description, and a weight.

    Attributes :
        name (str) : The name of the Item.
        description (str) : A detailed description of the Item.
        weight (float) : A float that represents the weight of the item.

    Methods : 
        __init__(self, name, description) : The constructor.
        __str__(self) : Return a string containing a full description of the Item.

    Examples :

    >>> knife = Item("Knife", "un couteau bien aiguisé.", 2)
    >>> knife.name
    'Knife'
    >>> knife.description
    'un couteau bien aiguisé.'
    >>> print(knife)
    Knife : un couteau bien aiguisé. (2 kg)

    """

    # Define the constructor. 
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    # Redefine the __str__() method.
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
