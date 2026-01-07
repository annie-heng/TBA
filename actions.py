# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted 
#with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    The Actions class contains static methods that define the actions
    that can be performed in the game.
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.go(game, ["go", "N"], 1)
        <BLANKLINE>
        Vous êtes dans la partie nord du village.
        <BLANKLINE>
        Sorties: N, E, S, O
        <BLANKLINE>
        True
         >>> Actions.go(game, ["go", "W"], 1)
        <BLANKLINE>
        Direction 'W' non reconnue.
        <BLANKLINE>
        Vous êtes dans la partie nord du village.
        <BLANKLINE>
        Sorties: N, E, S, O
        <BLANKLINE>
        True
        >>> Actions.go(game, ["go", "N", "E"], 1)
        <BLANKLINE>
        La commande 'go' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.go(game, ["go"], 1)
        <BLANKLINE>
        La commande 'go' prend 1 seul paramètre.
        <BLANKLINE>
        False
        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        #A supprimer si trop contraignant
        if player.current_room.is_dark :
            print("\nSe déplacer dans le noir est trop dangereux, il faudrait de quoi s'éclairer...\n") 
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        #Check if the provided direction is part of the valid words list of one possible direction
        for d in game.directions.keys() :
            if direction in game.directions.get(d) :
                player.move(d)
                # Characters move only if the player uses the command "go". 
                for character in game.characters :
                    if character in ["King", "Shopkeeper", "Dragon"]:
                        continue
                    npc = game.characters.get(character)
                    if npc :
                        npc.move()
                # Condition de défaite
                if player.current_room.name == "Cave" and ("sword" or "shield") not in player.inventory :
                    print("\n💀 Vous vous êtes aventuré dans un lieu trop dangereux pour survivre sans équipement.\n")
                    print(f"Votre mission s'arrête ici, vos blessures vous ont emporté. Merci {player.name} pour votre dévouement.\n")
                    # Set the finished attribute of the game object to True.
                    game.finished = True
                return True
                
        else:
            print(f"\nDirection '{direction}' non reconnue.")
            print(player.current_room.get_long_description())
            return False

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        game.setup("TestPlayer")
        >>> Actions.quit(game, ["quit"], 0)
        <BLANKLINE>
        Merci TestPlayer d'avoir joué. Au revoir.
        <BLANKLINE>
        True
         >>> Actions.quit(game, ["quit", "N"], 0)
        <BLANKLINE>
        La commande 'quit' ne prend pas de paramètre.
        False
        <BLANKLINE>
         >>> Actions.quit(game, ["quit", "N", "E"], 0)
        <BLANKLINE>
        La commande 'quit' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
       >>> game.setup("TestPlayer")
        >>> Actions.help(game, ["help"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Voici les commandes disponibles:
            - help : afficher cette aide
            - quit : quitter le jeu
            - go <direction> : se déplacer dans une direction cardinale (N, E, S, O)
            - quests : afficher la liste des quêtes
            - quest <titre> : afficher les détails d'une quête
            - activate <titre> : activer une quête
            - rewards : afficher vos récompenses
        <BLANKLINE>
        True
        >>> Actions.help(game, ["help", "N"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
         >>> Actions.help(game, ["help", "N", "E"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        print("Veuillez les réaliser dans l'ordre.\n")
        return True


    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True


    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False


    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.history(game, ["history"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous n'avez pas encore d'historique, déplacez-vous !
        <BLANKLINE>
        True
        >>> Actions.go(game, ["go", "N"], 1)
        <BLANKLINE>
        Vous êtes dans la partie nord du village.
        <BLANKLINE>
        Sorties: N, E, S, O
        <BLANKLINE>
        True
        >>> Actions.history(game, ["history"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Votre parcours est le suivant : 
            - dans la partie sud du village
        <BLANKLINE>
        True
        >>> Actions.history(game, ["history", "N"], 0)
        <BLANKLINE>
        La commande 'history' ne prend pas de paramètre.
        <BLANKLINE>
        False
         >>> Actions.history(game, ["history", "N", "E"], 0)
        <BLANKLINE>
        La commande 'history' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
    
        player = game.player
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the history of the player.
        print(player.get_history())
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):

        """
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.back(game, ["back"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Impossible de retourner en arrière ! Votre historique est vide.
        <BLANKLINE>
        False
        >>> Actions.go(game, ["go", "N"], 1)
        <BLANKLINE>
        Vous êtes dans la partie nord du village.
        <BLANKLINE>
        Sorties: N, S, E, O
        <BLANKLINE>
        True
        >>> Actions.back(game, ["back"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Vous êtes dans la partie sud du village.
        <BLANKLINE>
        Sorties: N, E, S, O
        <BLANKLINE>
        True
        >>> Actions.back(game, ["back", "N"], 0)
        <BLANKLINE>
        La commande 'back' ne prend pas de paramètre.
        <BLANKLINE>
        False
         >>> Actions.back(game, ["back", "N", "E"], 0)
        <BLANKLINE>
        La commande 'back' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

        player = game.player
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Move the player to the previous room.
        player.move_back()
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Print the description and the list of items in the current room. 

            Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

            Returns:
            bool: True if the command was executed successfully, False otherwise.

            Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.look(game, ["look"], 0)
        <BLANKLINE>
        Vous êtes dans la partie sud du village.
        <BLANKLINE>
        Sorties: N, E, S, O
        <BLANKLINE>
        On voit : 
            - money : une pièce d'argent (0 kg)
        <BLANKLINE>
        True
        >>> Actions.look(game, ["look", "N"], 0)
        <BLANKLINE>
        La commande 'look' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.look(game, ["look", "N", "E"], 0)
        <BLANKLINE>
        La commande 'look' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # If the room is dark, print the corresponding message and return False.
        if player.current_room.is_dark :
            print("\nCette pièce est beaucoup trop sombre pour y voir quoi que ce soit !\n")
            return False 

        # Print the description and the list of items in the current room.
        print(f"{player.current_room.get_long_description()} {player.current_room.get_inventory()}")
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Take an Item from the current room and place it in the player's inventory. 
        The parameter must be the name of an Item that is present in the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.take(game, ["take", "money"], 1)
        <BLANKLINE>
        Votre porte-monnaie a été incrémenté.
        <BLANKLINE>
        True
        >>> Actions.take(game, ["take", "sword"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'sword'.
        <BLANKLINE>
        True
        >>> Actions.take(game, ["take", "shield"], 1)
        <BLANKLINE>
        L'objet 'shield' ne rentre pas dans votre sac. Il n'y a plus de place.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take", "pi"], 1)
        <BLANKLINE>
        Aucun objet nommé pi ne se trouve dans la pièce. Tapez look pour avoir la liste des objets disponibles dans cette pièce.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take", "sword", "shield"], 1)
        <BLANKLINE>
        La commande 'take' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take"], 1)
        <BLANKLINE>
        La commande 'take' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # If the room is dark, print the corresponding message and return False.
        if player.current_room.is_dark :
            print("\nLa pièce est plongée dans le noir, impossible d'attraper un objet dans ces conditions.\n")
            return False 

        # Get the item name from the list of words.
        item_name = list_of_words[1]

        #Get the item from the current room.
        item = player.current_room.inventory.get(item_name)

        #Check if the requested item is present in the room.
        if item is None :
            print(f"\nAucun objet nommé {item_name} ne se trouve dans la pièce. Tapez look pour avoir la liste des objets disponibles dans cette pièce.\n")
            return False
        elif player.current_weight + item.weight > player.max_weight:
            print(f"\nL'objet '{item_name}' ne rentre pas dans votre sac. Il n'y a plus de place.\n")
            return False
        else :
            # if the item is 'money', it is not added to the inventory but the attribute 'money' of the player is incremented.
            if item_name == "money":
                player.money += 1
                del player.current_room.inventory[item_name]
                print(f"\nVotre porte-monnaie a été incrémenté.\n")
                return True
            else :
                player.inventory[item_name] = item
                player.current_weight += item.weight
                del player.current_room.inventory[item_name]
                print(f"\nVous avez pris l'objet '{item_name}'.\n")
                player.quest_manager.check_action_objectives("Prendre", item_name)
                return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an Item from the player's inventory in the current room. 
        The parameter must be the name of an Item that is present in player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.drop(game, ["drop", "money"], 1)
        <BLANKLINE>
        Aucun objet nommé money ne se trouve dans votre inventaire. Tapez check pour avoir le détail de votre inventaire.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take", "sword"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'sword'.
        <BLANKLINE>
        True
        >>> Actions.drop(game, ["drop", "sword"], 1)
        <BLANKLINE>
        Vous avez déposé l'objet 'sword'.
        <BLANKLINE>
        True
        >>> Actions.drop(game, ["drop", "sword", "shield"], 1)
        <BLANKLINE>
        La commande 'drop' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.drop(game, ["drop"], 1)
        <BLANKLINE>
        La commande 'drop' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the item name from the list of words.
        item_name = list_of_words[1]

        # Get the item from the player's inventory.
        item = player.inventory.get(item_name)

        # Check if the requested item is present in the player's inventory.
        if item is None :
            print(f"\nAucun objet nommé {item_name} ne se trouve dans votre inventaire. Tapez check pour avoir le détail de votre inventaire.\n")
            return False
        else :
            del player.inventory[item_name]
            player.current_weight -= item.weight
            player.current_room.inventory[item_name] = item
            print(f"\nVous avez déposé l'objet '{item_name}'.\n")
            return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Print the list of items in the player's inventory. 

            Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

            Returns:
            bool: True if the command was executed successfully, False otherwise.

            Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.check(game, ["check"], 0)
        <BLANKLINE>
        Votre inventaire est vide.
        <BLANKLINE>
        Votre porte-monnaie contient 2 pièces.
        <BLANKLINE>
        True
        >>> Actions.take(game, ["take", "sword"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'sword'.
        <BLANKLINE>
        True
        >>> Actions.check(game, ["check"], 0)
        <BLANKLINE>
        Vous disposez des items suivants : 
            - sword : une épée au fil tranchant comme un rasoir (2 kg)
        <BLANKLINE>
        Votre sac pèse 2 kg
        <BLANKLINE>
        Votre porte-monnaie contient 2 pièces.
        <BLANKLINE>
        True
        >>> Actions.check(game, ["check", "N"], 0)
        <BLANKLINE>
        La commande 'check' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.check(game, ["check", "N", "E"], 0)
        <BLANKLINE>
        La commande 'check' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        player = game.player
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the description and the list of items in the current room.
        print(player.get_inventory())
        return True
    
    @staticmethod
    def charge(game, list_of_words, number_of_parameters):
        """
        Charge the beamer if it is present in the player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.charge(game, ["charge"], 0)
        <BLANKLINE>
        Vous ne possédez aucun beamer à charger.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take", "beamer"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'beamer'.
        <BLANKLINE>
        True
        >>> Actions.charge(game, ["charge"], 0)
        <BLANKLINE>
        Le beamer a été chargé. Tapez "use beamer" pour vous téléporter dans la pièce mémorisée.
        <BLANKLINE>
        True
        >>> Actions.charge(game, ["charge", "beamer"], 0)
        <BLANKLINE>
        La commande 'charge' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.charge(game, ["charge", "N", "E"], 0)
        <BLANKLINE>
        La commande 'charge' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        #Check if the beamer Item is present in the inventory.
        player = game.player
        if "beamer" not in player.inventory :
            print("\nVous ne possédez aucun beamer à charger.\n")
            return False
        else :
            player.beamer_room = player.current_room
            print("\nLe beamer a été chargé. Tapez \"use beamer\" pour vous téléporter dans la pièce mémorisée.\n")
            return True
    
    @staticmethod
    def use(game, list_of_words, number_of_parameters):
        """
        Use the specified Item. 
        The parameter must be the name of an Item that is present in player's inventory.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.take(game, ["take", "beamer"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'beamer'.
        <BLANKLINE>
        True
        >>> Actions.use(game, ["use", "beamer"], 1)
        <BLANKLINE>
        Vous n'avez pas chargé le beamer.
        <BLANKLINE>
        False
        >>> Actions.charge(game, ["charge"], 0)
        <BLANKLINE>
        Le beamer a été chargé. Tapez "use beamer" pour vous téléporter dans la pièce mémorisée.
        <BLANKLINE>
        True
        >>> Actions.use(game, ["use", "beamer"], 1)
        <BLANKLINE>
        Vous êtes sur un pont à l'aspect fragile.
        <BLANKLINE>
        Sorties: N
        <BLANKLINE>
        <BLANKLINE>
        Le beamer a été utilisé et a disparu.
        <BLANKLINE>
        True
        >>> Actions.use(game, ["use", "pi"], 1)
        <BLANKLINE>
        Aucun objet nommé pi ne se trouve dans votre inventaire. Tapez check pour avoir le détail de votre inventaire.
        <BLANKLINE>
        False
        >>> Actions.take(game, ["take", "sword"], 1)
        <BLANKLINE>
        Vous avez pris l'objet 'sword'.
        <BLANKLINE>
        True
        >>> Actions.use(game, ["use", "sword"], 1)
        <BLANKLINE>
        L'objet 'sword' n'est pas utilisable.
        <BLANKLINE>
        False
        >>> Actions.use(game, ["use", "sword", "shield"], 1)
        <BLANKLINE>
        La commande 'use' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.use(game, ["use"], 1)
        <BLANKLINE>
        La commande 'use' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Check if the given Item name is correct.
        item_name = list_of_words[1]

        # Get the item from the player's inventory.
        item = player.inventory.get(item_name)

        # Check if the requested item is present in the player's inventory.
        if item is None :
            print(f"\nAucun objet nommé {item_name} ne se trouve dans votre inventaire. Tapez check pour avoir le détail de votre inventaire.\n")
            return False

        #Check if the requested item has an use.
        if item_name == "beamer" :
            # Check if the beamer is charged.
            if player.beamer_room == None :
                print("\nVous n'avez pas chargé le beamer.\n")
                return False  
            player.teleport()
            print("\nLe beamer a été utilisé et a disparu.\n")
            return True

        elif item_name == "magicmap" :
            if player.current_room.is_dark :
                print("\nVous ne pouvez pas lire votre magicmap dans le noir, il faudrait de quoi s'éclairer...\n") 
                return False
            else :
                location_list = ""
                for charac in game.characters.values() :
                    location_list += charac.get_location()
                print(location_list)
                return True

        elif item_name == "torch" :
            room = game.player.current_room
            if room.is_dark :
                room.is_dark = False
                print("\nVous avez allumé la torche.\n")
                return True
            else :
                print("\nLa pièce est déjà illuminée.\n")
                return False

        elif item_name == "sword" :
            if player.current_room.is_dark :
                print("\nManier une épée est trop dangereux dans le noir vous risqueriez de vous blesser, il faudrait de quoi s'éclairer...\n") 
                return False
            room = game.player.current_room 
            if room.name == "Cave" :
                player.quest_manager.check_action_objectives("Utiliser", item_name)
                print("\n🙌 🎊 Vous avez sauvé le royaume en éliminant la menace, le dragon est hors d'état de nuire.\n")
                print(f"Votre mission s'arrête ici, merci {player.name} pour votre aide. Au revoir.\n")
                # Set the finished attribute of the game object to True.
                game.finished = True
                return True
            else : 
                print("\nVous ne pouvez pas utiliser la sword dans le royaume. Vous risquez de blesser quelqu'un attendez le bon moment.\n")
                return False

        else :
            print(f"\nL'objet '{item_name}' n'est pas utilisable.\n")
            return False
    
    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Talk to a NPC that is present in the current room.
        The parameter must be a present NPC's name.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.talk(game, ["talk", "King"], 1)
        <BLANKLINE>
        Jeune aventurier, j'ai une mission pour toi.
        <BLANKLINE>
        True
        >>> Actions.talk(game, ["talk", "King"], 1)
        <BLANKLINE>
        Retrouve ma bague, et je te ferai don d'un objet qui te sera indispensable pour ta quête.
        <BLANKLINE>
        True
        >>> Actions.talk(game, ["talk", "pi"], 1)
        <BLANKLINE>
        Aucun personnage nommé pi ne se trouve dans la pièce. Tapez look pour avoir la liste des personnages présents dans cette pièce.
        <BLANKLINE>
        False
        >>> Actions.talk(game, ["talk", "Timmy", "Tommy"], 1)
        <BLANKLINE>
        La commande 'talk' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.talk(game, ["talk"], 1)
        <BLANKLINE>
        La commande 'talk' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the character name from the list of words.
        character_name = list_of_words[1]

        # Find the NPC in the current room.
        character = player.current_room.characters.get(character_name)

        #Check if the NPC is present in the room.
        if character is None :
            print(f"\nAucun personnage nommé {character_name} ne se trouve dans la pièce. Tapez look pour avoir la liste des personnages présents dans cette pièce.\n")
            return False
        else :
            print(f"\n{character.get_msg()}\n")
            player.quest_manager.check_action_objectives("Parler", character.name)
            return True
