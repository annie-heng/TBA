# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.exits = {}
        self.directions = {}
    
    # Setup the game
    def setup(self):

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
        money = Item("money", "une bourse pour débuter votre aventure", 2)
        potion = Item("potion", "une potion de soin", 2)
        shield = Item("shield", "un bouclier pour se défendre", 3)
        
        #Setup item location
        shop.inventory["potion"] = potion
        castle.inventory["sword"] = sword
        castle.inventory["shield"] = shield

        #Setup item player
        self.player.inventory["money"] = money
        player.current_weight += money.weight

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

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

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
