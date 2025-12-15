# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest



class Game:
 
    """The Game class manages the overall game state and flow."""
    
    
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.exits = {}
        self.directions = {}
        self.characters = {}

    # Setup the game
    def setup(self, player_name=None):
        """Initialize the game with rooms, commands, and quests."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_player(player_name)
        self._setup_quests()
        self._setup_items()
        self._setup_characters()


    def _setup_commands(self):
        """Initialize all game commands."""
        self.commands["help"] = Command("help"
                                        , " : afficher cette aide"
                                        , Actions.help
                                        , 0)
        self.commands["quit"] = Command("quit"
                                        , " : quitter le jeu"
                                        , Actions.quit
                                        , 0)
        self.commands["go"] = Command("go"
                                      , "<N|E|S|O> : se déplacer dans une direction cardinale"
                                      , Actions.go
                                      , 1)
        self.commands["quests"] = Command("quests"
                                          , " : afficher la liste des quêtes"
                                          , Actions.quests
                                          , 0)
        self.commands["quest"] = Command("quest"
                                         , " <titre> : afficher les détails d'une quête"
                                         , Actions.quest
                                         , 1)
        self.commands["activate"] = Command("activate"
                                            , " <titre> : activer une quête"
                                            , Actions.activate
                                            , 1)
        self.commands["rewards"] = Command("rewards"
                                           , " : afficher vos récompenses"
                                           , Actions.rewards
                                           , 0)
        self.commands["history"] = Command("history"
                                          , " : afficher le parcours du joueur"
                                          , Actions.history
                                          , 0)
        self.commands["look"]     = Command("look"
                                            , " : afficher la liste des items et des personnages présents dans cette pièce"
                                            , Actions.look
                                            , 0)
        self.commands["back"]     = Command("back", " : revenir dans la dernière pièce visitée"
                                            , Actions.back
                                            , 0)
        self.commands["take"]     = Command("take"
                                            , ": prendre un Item présent dans la pièce où se situe le joueur"
                                            , Actions.take
                                            , 1)
        self.commands["drop"]     = Command("drop"
                                           , " : déposer un Item de l'inventaire dans la pièce actuelle"
                                           , Actions.drop
                                           , 1)
        self.commands["check"]     = Command("check"
                                            , " : afficher la liste des items présents dans l'inventaire du joueur"
                                            , Actions.check
                                            , 0)
        self.commands["talk"]     = Command("talk"
                                           , " : parler à un personnage présent dans la pièce"
                                           , Actions.talk
                                           , 1)
        self.commands["charge"]     = Command("charge"
                                            , " : mémoriser la pièce actuelle si le beamer est présent dans l'inventaire"
                                            , Actions.charge
                                            , 0)
        self.commands["use"]     = Command("use"
                                           , " : utiliser un objet présent dans votre inventaire"
                                           , Actions.use
                                           , 1)                        

    def _setup_rooms(self):
        """Initialize all rooms and their exits."""
        # Create rooms
        s = "dans la partie nord du village."
        villagenorth = Room("VillageNorth", s)

        s = "dans la partie sud du village."
        villagesouth = Room("VillageSouth", s)

        s = "à l'intérieur d'un château aux murs sombres."
        castle = Room("Castle", s)

        s = "dans un sous-terrain entièrement plongé dans l'obscurité"
        undercastle = Room("UnderCastle", s)

        s = "dans le hall d'une tour. Vous apercevez devant vous des escaliers menant au sommet, et d'autres cachés dans un recoin."
        tower = Room("Tower", s)

        s = "dans une pièce minuscule au sommet de la tour."
        toptower = Room("TopTower", s)
        
        s = "dans une cave encombrée d'objets poussiérieux."
        towercave = Room("BottomTower", s)

        s = "dans une grotte immense au sol inégal et dans laquelle vous entendez des bruits provenant du fond de celle-ci."
        cave = Room("Cave", s)

        s = "dans une barque sur un lac."
        lake = Room("Lake", s)

        s = "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres."
        forest = Room("Forest", s)

        s = "dans des écuries bien entretenues, où quelques chevaux se reposent."
        stable = Room("Stable", s)

        s = "sur un pont à l'aspect fragile."
        bridge = Room("Bridge", s)

        s = "dans un champ de hautes herbes."
        field = Room("Field", s)

        s = "dans une boutique d'items tenue par une vieille dame."
        shop = Room("Shop", s)

        # Add rooms to game
        for room in [villagenorth, villagesouth, forest, tower, toptower, towercave, cave, castle, undercastle, stable, bridge, lake, field, shop]:
            self.rooms.append(room)

        # Create exits
        villagesouth.exits = {"N" : villagenorth, "E" : field, "S" : lake, "O" : stable, "U" : None, "D" : None}
        villagenorth.exits = {"N" : forest, "E" : tower, "S" : villagesouth, "O" : shop, "U" : None, "D" : None}
        castle.exits = {"N" : stable, "E" : lake, "S" : None, "O" : stable, "U" : None, "D" : undercastle}
        undercastle.exits = {"N" : towercave, "E" : None, "S" : None, "O" : None, "U" : castle, "D" : None}
        tower.exits = {"N" : None, "E" : None, "S" : field, "O" : villagenorth, "U" : toptower, "D" : towercave}
        toptower.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : tower}
        towercave.exits = {"N" : None, "E" : None, "S" : undercastle, "O" : None, "U" : tower, "D" : None}
        cave.exits = {"N" : None, "E" : forest, "S" : None, "O" : None, "U" : None, "D" : None}
        lake.exits = {"N" : villagesouth, "E" : bridge, "S" : None, "O" : castle, "U" : None, "D" : None}
        forest.exits = {"N" : None, "E" : None, "S" : villagenorth, "O" : cave, "U" : None, "D" : None}
        stable.exits = {"N" : shop, "E" : villagesouth, "S" : castle, "O" : None, "U" : None, "D" : None}
        bridge.exits = {"N" : field, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        field.exits = {"N" : tower, "E" : None, "S" : None, "O" : villagesouth, "U" : None, "D" : None}
        shop.exits = {"N" : None, "E" : villagenorth, "S" : stable, "O" : None, "U" : None, "D" : None}

        # Create set of directions
        self.exits = {d for d in tower.exits.keys()}

        # Create dict object with compatible words for directions
        self.directions = {'N' : ['N', 'North', 'NORTH', 'north', 'n'], 'S' : ['S', 'South', 'SOUTH', 'south', 's'], 'E' : ['E', 'East', 'EAST', 'east', 'e'], 'O' : ['O', 'Ouest', 'OUEST', 'ouest', 'o'], 'U' : ['U', 'Up', 'UP', 'up', 'u'], 'D' : ['D', 'Down', 'DOWN', 'down', 'd']} 



    def _setup_player(self, player_name=None):
        """Initialize the player."""
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        self.player.current_room = self.rooms[1]  # villagesouth

    def _setup_items(self):
        """Initialize the Items and their locations"""
        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        money = Item("money", "une pièce d'argent", 0)
        potion = Item("potion", "une potion de soin", 2)
        shield = Item("shield", "un bouclier pour se défendre", 3)
        torch = Item("torch", "une torche qui permet d'éclairer les lieux sombres", 3)
        ring = Item("ring", "une bague de valeur qui semble appartenir à quelqu'un d'important", 3)
        key = Item("key", "uné clé qui ouvre des portes", 3)
        beamer = Item("beamer", "un objet permettant de \"mémoriser\" une pièce et de s'y téléporter", 1)
        magicmap = Item("magicmap", "une carte permettant de voir les localisations de tous les villageois", 1)
        
        #Setup item location
        self.rooms[13].inventory["potion"] = potion     # shop
        self.rooms[7].inventory["sword"] = sword        # castle
        self.rooms[7].inventory["shield"] = shield      # castle
        self.rooms[7].inventory["money"] = money        # castle
        self.rooms[5].inventory["ring"] = ring          #towercave
        self.rooms[1].inventory["money"] = money        # villagesouth
        self.rooms[9].inventory["money"] = money        # stable
        self.rooms[10].inventory["beamer"] = beamer     # bridge
        self.rooms[8].inventory["magicmap"] = magicmap  #undercastle
        
    def _setup_characters(self):
        """Initialize the Characters and their locations"""
        king = Character("King", "le roi du pays, un guerrier exceptionnel qui a conquis de nombreux territoires", self.rooms[7], ["Jeune aventurier, j'ai une mission pour toi.", "Retrouve ma bague, et je te ferai don d'un objet qui te sera indispensable pour ta quête."]) 
        self.rooms[7].characters["King"] = king     # castle
        self.characters["King"] = king

        timmy = Character("Timmy", "un enfant du village qui adore explorer et ne se trouve jamais longtemps au même endroit, au grand dam de ses parents", self.rooms[0], ["C'est parti pour l'aventure!", "J'ai envie de bonbons...", "Où est-ce que je peux aller?"])
        self.rooms[0].characters["Timmy"] = timmy   # villagenorth
        self.characters["Timmy"] = timmy

        shopkeeper = Character("Shopkeeper", "le seul vendeur du royaume, demandez lui n'importe quoi ça vous sera utile", self.rooms[13], ["Bonjour, que puis-je faire pour vous ?", "Tu peux aussi récolter des items à travers le pays."])
        self.rooms[13].characters["Shopkeeper"] = shopkeeper   # shop
        self.characters["Shopkeeper"] = shopkeeper

    def _setup_quests(self):
        """Initialize all quests."""
        talking_quest = Quest(
            title="Prévenir le peuple",
            description="Aller voir chaque membre du royaume pour les prévenir du danger.",
            objectives=["Parler avec Timmy", "Parler avec King", "Parler avec Shopkeeper" ],
            reward="Un paquet de bonbons"
        )

        ring_quest = Quest(
            title= "La requête du souverain",
            description= "Parler au roi qui a besoin de votre aide. Le roi se trouve dans le château.",
            objectives= ["Parler avec King", "Prendre ring"],
            reward="Un talisman puissant permettant de résister aux flammes"
        )

        self.player.quest_manager.add_quest(talking_quest)
        self.player.quest_manager.add_quest(ring_quest)
    
    """
    A EFFACER
    # Setup the game
    def to_delete_setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher le parcours du joueur", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : afficher la liste des items présents dans cette pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un Item présent dans la pièce où se situe le joueur", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : déposer un Item de l'inventaire dans la pièce actuelle", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : afficher la liste des items présents dans l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        charge = Command("charge", " : si le beamer est dans l'inventaire, la pièce actuelle est mémorisée", Actions.charge, 0)
        self.commands["charge"] = charge
        use = Command("use", " : utiliser un objet présent dans votre inventaire", Actions.use, 1)
        self.commands["use"] = use
        talk = Command("talk", " : parler à un personnage présent dans la pièce", Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms
        villagenorth = Room("VillageNorth", "dans la partie nord du village.")
        self.rooms.append(villagenorth)
        villagesouth = Room("VillageSouth", "dans la partie sud du village.")
        self.rooms.append(villagesouth)
        castle = Room("Castle", "à l'intérieur d'un château aux murs sombres.")
        self.rooms.append(castle)
        undercastle = Room("UnderCastle", "dans un sous-terrain faiblement éclairé par des torches.")
        self.rooms.append(undercastle)
        tower = Room("Tower", "dans le hall d'une tour. Vous apercevez devant vous des escaliers menant au sommet, et d'autres cachés dans un recoin.")
        self.rooms.append(tower)
        toptower = Room("TopTower", "dans une pièce minuscule au sommet de la tour.")
        self.rooms.append(toptower)
        towercave = Room("BottomTower", "dans une cave encombrée d'objets poussiérieux.")
        self.rooms.append(towercave)
        cave = Room("Cave", "dans une grotte immense au sol inégal et dans laquelle vous entendez des bruits provenant du fond de celle-ci.")
        self.rooms.append(cave)
        lake = Room("Lake", "dans une barque sur un lac.")
        self.rooms.append(lake)
        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        stable = Room("Stable", "dans des écuries bien entretenues, où quelques chevaux se reposent.")
        self.rooms.append(stable)
        bridge = Room("Bridge", "sur un pont à l'aspect fragile.")
        self.rooms.append(bridge)
        field = Room("Field", "dans un champ de hautes herbes.")
        self.rooms.append(field)
        shop = Room("Shop", "dans une boutique d'items tenue par une vieille dame.")
        self.rooms.append(shop)

        #tower = Room("Tower", "une immense tour en pierre qui s'élève au dessus des nuages.")
        #self.rooms.append(tower)
        #cave = Room("Cave", "une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        #self.rooms.append(cave)
        #cottage = Room("Cottage", "un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        #self.rooms.append(cottage)
        #swamp = Room("Swamp", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        #self.rooms.append(swamp)
        #castle = Room("Castle", "un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        #self.rooms.append(castle)

        # Create exits for rooms

        #forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None}
        #tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None}
        #cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        #cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        #swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        #castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}

        villagesouth.exits = {"N" : villagenorth, "E" : field, "S" : lake, "O" : stable, "U" : None, "D" : None}
        villagenorth.exits = {"N" : forest, "E" : tower, "S" : villagesouth, "O" : shop, "U" : None, "D" : None}
        castle.exits = {"N" : stable, "E" : lake, "S" : None, "O" : stable, "U" : None, "D" : undercastle}
        undercastle.exits = {"N" : towercave, "E" : None, "S" : None, "O" : None, "U" : castle, "D" : None}
        tower.exits = {"N" : None, "E" : None, "S" : field, "O" : villagenorth, "U" : toptower, "D" : towercave}
        toptower.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : tower}
        towercave.exits = {"N" : None, "E" : None, "S" : undercastle, "O" : None, "U" : tower, "D" : None}
        cave.exits = {"N" : None, "E" : forest, "S" : None, "O" : None, "U" : None, "D" : None}
        lake.exits = {"N" : villagesouth, "E" : bridge, "S" : None, "O" : castle, "U" : None, "D" : None}
        forest.exits = {"N" : None, "E" : None, "S" : villagenorth, "O" : cave, "U" : None, "D" : None}
        stable.exits = {"N" : shop, "E" : villagesouth, "S" : castle, "O" : None, "U" : None, "D" : None}
        bridge.exits = {"N" : field, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        field.exits = {"N" : tower, "E" : None, "S" : None, "O" : villagesouth, "U" : None, "D" : None}
        shop.exits = {"N" : None, "E" : villagenorth, "S" : stable, "O" : None, "U" : None, "D" : None}

        # Create set of directions
        self.exits = {d for d in tower.exits.keys()}

        # Create dict object with compatible words for directions
        self.directions = {'N' : ['N', 'North', 'NORTH', 'north', 'n'], 'S' : ['S', 'South', 'SOUTH', 'south', 's'], 'E' : ['E', 'East', 'EAST', 'east', 'e'], 'O' : ['O', 'Ouest', 'OUEST', 'ouest', 'o'], 'U' : ['U', 'Up', 'UP', 'up', 'u'], 'D' : ['D', 'Down', 'DOWN', 'down', 'd']} 

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = villagesouth

        #Setup item
        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
        money = Item("money", "une pièce d'argent", 0)
        potion = Item("potion", "une potion de soin", 2)
        shield = Item("shield", "un bouclier pour se défendre", 3)
        torch = Item("torch", "une torche qui permet d'éclairer les lieux sombres", 3)
        ring = Item("ring", "une bague de valeur qui semble appartenir à quelqu'un d'important", 3)
        key = Item("key", "uné clé qui ouvre des portes", 3)
        beamer = Item("beamer", "un objet permettant de \"mémoriser\" une pièce et de s'y téléporter", 1)
        
        #Setup item location
        shop.inventory["potion"] = potion
        castle.inventory["sword"] = sword
        castle.inventory["shield"] = shield
        castle.inventory["money"] = money
        villagesouth.inventory["money"] = money
        stable.inventory["money"] = money
        bridge.inventory["beamer"] = beamer

        #Setup player inventory

        #Setup characters
        king = Character("King", "le roi du pays, un guerrier exceptionnel qui a conquis de nombreux territoires", castle, ["Jeune aventurier, j'ai une mission pour toi. \nRetrouve ma bague, et je te ferai don d'un objet qui te sera indispensable pour ta quête."]) 
        castle.characters["King"] = king
        self.characters["King"] = king 
        timmy = Character("Timmy", "un enfant du village qui adore explorer et ne se trouve jamais longtemps au même endroit, au grand dam de ses parents", villagenorth, ["C'est parti pour l'aventure!", "J'ai envie de bonbons...", "Où est-ce que je peux aller?"])
        villagenorth.characters["Timmy"] = timmy
        self.characters["Timmy"] = timmy
    """

    # Play the game
    def play(self):
        """Main game loop."""

        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """Process the command entered by the player."""

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # command empty
        if command_word == "":
            print(">")
        # If the command is not recognized, print an error message
        elif command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
            # Characters move only if the player uses the command "go". 
            if command_word == "go":
                self.characters.get("Timmy").move()


    # Print the welcome message
    def print_welcome(self):
        """Print the welcome message."""

        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
