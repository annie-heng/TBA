# Define the Player class.

from quest import QuestManager

class Player():
    """
    This class represents a player. A player is composed of a name, a history, an inventory and a current location.

    Attributes:
        name (str): The name of the player.
        current_room (Room) : The room where the player is currently located.
        history (list) : The list containing all the rooms that the player has visited, excluding the current one.
        inventory(dict) : The inventory of the player, in the form of a dict object where each key is the item's name and the value is the corresponding Item object.
        max_weight (int) : The maximum total weight of Items that the player can carry.
        current_weight (int) : The sum of each Item's weight from the player's inventory.
        money (int) : The number of coins that the player owns.
        beamer_room (Room) : The memorised room in the beamer.
        move_count : The number of moves the player has made.
        quest_manager (QuestManager) : The player's quest manager, which checks if objectives or tasks have been completed.
        rewards (list) : A list that contains all the rewards (String objects) the player has received.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Get the next room from the exits dictionary of the current room, set it as the current room and return True. If the next room is None, print an error message and return False.
        get_history(self) : Return a string that contains a list of all the rooms that the player has visited, in order. If the history attribute is empty, return the corresponding message.
        move_back(self) : If the history is not empty, get the last object of the history attribute, removes it from self.history, set it as the current room and return True.
        get_inventory(self) : Return a string listing the contents of the player's inventory.
        teleport(self) : Teleports the player to the Room that is contained in the beamer_room attribute.
        add_reward (self, reward) : Add a reward to the player's rewards list.
        show_rewards (self) : Display all rewards earned by the player.

    Examples:
    >>> from room import Room
    >>> sam = Player("Sam")
    >>> sam.name
    'Sam'
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
        """

        The constructor.

        Args : 
            name(str) : The name entered by the player.

        Examples :
        
        >>> player = Player("Bob")
        >>> player.name
        Bob

        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 8
        self.current_weight = 0
        self.money = 2
        self.beamer_room = None
        self.move_count = 0
        self.quest_manager = QuestManager(self)
        self.rewards = []  # List to store earned rewards
    
    # Define the move method.
    def move(self, direction):
        """
        Get the next room from the exits dictionary of the current room, 
        set it as the current room and return True. If the next room is None, 
        print an error message and return False.

        Args :
            direction (str) : The direction entered by the player. (N | S | E | O | U |D)


        Returns:
            bool: True if the move was successful, False otherwise.
            
        Examples:
        
        >>> from room import Room
        >>> player = Player("Dave")
        >>> room1 = Room("Room1", "in room 1")
        >>> room2 = Room("Room2", "in room 2")
        >>> room3 = Room("Room3", "in room 3")
        >>> room1.exits = {"N": room2, "E": None, "S": None, "O": None}
        >>> room2.exits = {"S": room1, "E": room3, "S": None, "O": None}
        >>> player.current_room = room1
        >>> player.move_count
        0
        >>> player.move("N")
        <BLANKLINE>
        Vous êtes in room 2
        <BLANKLINE>
        Sorties: E
        <BLANKLINE>
        True
        >>> player.move_count
        1
        >>> player.current_room.name
        'Room2'
        >>> player.move("E")
        <BLANKLINE>
        Vous êtes in room 3
        <BLANKLINE>
        Sorties:
        <BLANKLINE>
        True
        >>> player.move_count
        2
        """

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

        
        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True
    
    #Define the get_history method.
    def get_history(self) :

        """
        Provides a history of the player's movements.

        Returns : 
            string : contains the descriptions of all of the rooms that the player has visited, 
            in order. If the history attribute is empty, contains the corresponding message.

        Examples :
        >>> from room import Room
        >>> alice = Player("Alice")
        >>> alice.history()  # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous n'avez pas encore d'historique, déplacez-vous !
        <BLANKLINE>
        >>> room1 = Room("Room1", "in room 1")
        >>> room2 = Room("Room2", "in room 2")
        >>> room1.exits = {"N": room2, "E": None, "S": None, "O": None}
        >>> room2.exits = {"S": room1, "E": room3, "S": None, "O": None}
        >>> alice.current_room = room1
        >>> alice.move('N')
        <BLANKLINE>
        Vous êtes in room 2
        <BLANKLINE>
        Sorties: E
        <BLANKLINE>
        True
        >>> alice.get_history()
        '\nVotre parcours est le suivant :\n\t- in room 1\n'
        """


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
        """ 
        Move the player in the last room they visited.

        Returns :
            bool : True if the move was successful, False otherwise.

        Examples : 

        >>> from room import Room
        >>> player = Player("Dave")
        >>> room1 = Room("Room1", "in room 1")
        >>> room2 = Room("Room2", "in room 2")
        >>> room1.exits = {"N": room2, "E": None, "S": None, "O": None}
        >>> player.current_room = room1
        >>> player.move_count
        0
        >>> player.history
        []
        >>> player.move("N")
        <BLANKLINE>
        Vous êtes in room 2
        <BLANKLINE>
        Sorties: E
        <BLANKLINE>
        True
        >>> player.move_count
        1
        >>> player.current_room.name
        'Room2'
        >>> player.history
        [Room1]
        >>> player.move_back()
        <BLANKLINE>
        Vous êtes in room 1
        <BLANKLINE>
        Sorties: N
        <BLANKLINE>
        True
        >>> player.move_count
        2
        >>> player.history
        []

        """
 

        #If the player has no history, print an error message and return False.
        if len(self.history) == 0 :
            print("\nImpossible de retourner en arrière ! Votre historique est vide.\n")
            return False

        #Set a inter room 
        inter_room = self.history[-1]
        if inter_room in self.current_room.exits.values() :
            #Set the current room to the last visited room.
            self.current_room = self.history.pop()
            print(self.current_room.get_long_description())
            #print(self.get_history())

            # Check room visit objectives
            self.quest_manager.check_room_objectives(self.current_room.name)

            # Increment move counter and check movement objectives
            self.move_count += 1
            self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

            return True

        else : 
            print("\nImpossile de retourner en arrière, le passage est à sens unique !\n")
            return False

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
        # Add the current_room to the history.
        self.history.append(self.current_room)
        # Change the current room to the "memorized" room.
        self.current_room = self.beamer_room
        print(self.current_room.get_long_description())
        self.beamer_room = None
        # Delete the beamer from the inventory because it has a one-time use.
        del self.inventory["beamer"]

         # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True

    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()