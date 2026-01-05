# Description: Game class

# Import modules
from pathlib import Path
import sys

# Tkinter imports for GUI
import tkinter as tk
from tkinter import ttk, simpledialog


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
                                      , "<N|E|S|O|U|D> : se déplacer dans une direction cardinale"
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
                                            , " <objet> : prendre un Item présent dans la pièce où se situe le joueur"
                                            , Actions.take
                                            , 1)
        self.commands["drop"]     = Command("drop"
                                           , " <objet> : déposer un Item de l'inventaire dans la pièce actuelle"
                                           , Actions.drop
                                           , 1)
        self.commands["check"]     = Command("check"
                                            , " : afficher la liste des items présents dans l'inventaire du joueur"
                                            , Actions.check
                                            , 0)
        self.commands["talk"]     = Command("talk"
                                           , " <personnage> : parler à un personnage présent dans la pièce"
                                           , Actions.talk
                                           , 1)
        self.commands["charge"]     = Command("charge"
                                            , " : mémoriser la pièce actuelle si le beamer est présent dans l'inventaire"
                                            , Actions.charge
                                            , 0)
        self.commands["use"]     = Command("use"
                                           , " <objet> : utiliser un objet présent dans votre inventaire"
                                           , Actions.use
                                           , 1)                        

    def _setup_rooms(self):
        """Initialize all rooms and their exits."""
        # Create rooms
        s = "dans la partie nord du village."
        villagenorth = Room("VillageNorth", s, False, image = "villagenorth.png")

        s = "dans la partie sud du village."
        villagesouth = Room("VillageSouth", s, False, image="villagesouth.png")

        s = "à l'intérieur d'un château aux murs sombres."
        castle = Room("Castle", s, False, image = "castle.png")

        s = "dans un sous-terrain entièrement plongé dans l'obscurité"
        undercastle = Room("UnderCastle", s, True, image = "undercastle.png")

        s = "dans le hall d'une tour. Il y a des escaliers menant au sommet, et d'autres cachés dans un recoin."
        tower = Room("Tower", s, False, image = "tower.png")

        s = "dans une pièce minuscule au sommet de la tour."
        toptower = Room("TopTower", s, False, image = "toptower.png")
        
        s = "dans une cave encombrée d'objets poussiérieux."
        towercave = Room("BottomTower", s, True, image = "towercave.png")

        s = "dans une grotte immense au sol inégal et dans laquelle vous entendez des bruits provenant du fond de celle-ci."
        cave = Room("Cave", s, True, image = "cave.png")

        s = "dans une barque sur un lac."
        lake = Room("Lake", s, False, image = "lake.png")

        s = "dans une forêt enchantée. On y entend une brise légère à travers la cime des arbres."
        forest = Room("Forest", s, False, image = "forest.png")

        s = "dans des écuries bien entretenues, où quelques chevaux se reposent."
        stable = Room("Stable", s, False, image = "stable.png")

        s = "sur un pont à l'aspect fragile."
        bridge = Room("Bridge", s, False, image = "bridge.png")

        s = "dans un champ de hautes herbes."
        field = Room("Field", s, False, image = "field.png")

        s = "dans une boutique d'items tenue par un vieil homme."
        shop = Room("Shop", s, False, image = "shop.png")

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

        #Setup Player's inventory
        self.player.inventory["torch"] = torch
        
    def _setup_characters(self):
        """Initialize the Characters and their locations"""
        king = Character("King", "le roi du pays, un guerrier exceptionnel qui a conquis de nombreux territoires", self.rooms[7], ["Jeune aventurier, j'ai une mission pour toi.", "Retrouve ma bague, et je te ferai don d'un objet qui te sera indispensable pour ta quête."]) 
        self.rooms[7].characters["King"] = king     # castle
        self.characters["King"] = king

        timmy = Character("Timmy", "un enfant du village qui adore explorer et ne se trouve jamais longtemps au même endroit, au grand dam de ses parents", self.rooms[0], ["Moi j'ai pas peur des dragons ! Je peux aller où je veux !", "C'est parti pour l'aventure!", "J'ai envie de bonbons...", "Où est-ce que je peux aller?"])
        self.rooms[0].characters["Timmy"] = timmy   # villagenorth
        self.characters["Timmy"] = timmy

        shopkeeper = Character("Shopkeeper", "le seul vendeur du royaume, demandez lui n'importe quoi ça vous sera utile", self.rooms[13], ["Quoi, un dragon qui rôde autour ? Ce n'est pas bon pour les affaires, ça...", "Bonjour, que puis-je faire pour vous ?", "Tu peux aussi récolter des items à travers le pays."])
        self.rooms[13].characters["Shopkeeper"] = shopkeeper   # shop
        self.characters["Shopkeeper"] = shopkeeper

        dad = Character("Dad", "le botaniste du village, toujours à la recherche de nouvelles plantes ou des matériaux rares. Il est également le père de Timmy", self.rooms[12], ["Un dragon ?! Ce n'est pas vrai, Timmy est encore dehors ! Je dois vite le retrouver!", "Où est-ce qu'il a bien pu se fourrer, cette fois...", "Ces fleurs protègent du mal, selon les légendes."])
        self.rooms[12].characters["Dad"] = dad          # field
        self.characters["Dad"] = dad

        witch = Character("Witch", "une sorcière ayant plus de 150 ans mais qui n'en fait pas plus de 40, sa magie est d'un niveau plutôt moyen contrairement à ce qu'elle prétend", self.rooms[4], ["Face à mes sorts, un dragon ne fait pas le poids ! Mais merci tout de même de m'avoir prévenue.", "Sauriez-vous s'il existe un abri bien protégé ? C'est pour un ami, bien sûr, je m'en sortirai très bien...", "Emp ots nacydobon enoon ! C'est mon sortilège favori."])
        self.rooms[4].characters["Witch"] = witch
        self.characters["Witch"] = witch

        troubadour = Character("Troubadour", "un musicien talentueux qui ne peut s'empêcher de chantonner et de rimer", self.rooms[0], ["🎶​ Une créature terrifiante serait dans le coin ? J'ai intérêt à fuir bien loin 🎶​", " 🎶​ Même les plus braves et les plus fous, prendraient leurs jambes à leur cou ! 🎶​"])
        self.rooms[0].characters["Troubadour"] = troubadour
        self.characters["Troubadour"] = troubadour


    def _setup_quests(self):
        """Initialize all quests."""
        talking_quest = Quest(
            title="Prévenir le peuple",
            description="Aller voir chaque membre du royaume pour les prévenir du danger : un dragon qui se serait établi dans les environs et qui est connu pour sa violence.",
            objectives=["Parler avec Timmy", "Parler avec Shopkeeper", "Parler avec Dad", "Parler avec Witch", "Parler avec Troubadour"],
            reward="Un paquet de bonbons"
        )

        ring_quest = Quest(
            title= "La requête du souverain",
            description= "Parler au roi qui a besoin de votre aide. Le roi se trouve dans le château.",
            objectives= ["Parler avec King", "Prendre ring"],
            reward="Un talisman puissant permettant de résister aux flammes"
        )

        walking_quest = Quest(
            title ="Le tour du pays",
            description ="Parcourir le pays entier, et découvrir tous les lieux qui le composent.",
            objectives = ["Visiter VillageNorth", "Visiter VillageSouth", "Visiter Castle", "Visiter UnderCastle", 
                        "Visiter Tower", "Visiter TopTower", "Visiter BottomTower", "Visiter Cave", "Visiter Lake", 
                        "Visiter Forest", "Visiter Stable", "Visiter Bridge", "Visiter Field", "Visiter Shop"],
            reward="Une paire de bottes confortables, parfaites pour de longues distances"
        )

        suit_up_quest = Quest(
            title="L'habit fait le chevalier",
            description="Récupérer le nécessaire pour aller vaincre le dragon",
            objectives=["Prendre sword", "Prendre shield"],
            reward="Une médaille d'honneur"
        )

        self.player.quest_manager.add_quest(talking_quest)
        self.player.quest_manager.add_quest(ring_quest)
        self.player.quest_manager.add_quest(walking_quest)
        self.player.quest_manager.add_quest(suit_up_quest)

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

    # Print the welcome message
    def print_welcome(self):
        """Print the welcome message."""
        # Guard against None values
        if not self.player or not self.player.name:
            return

        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure médiéval !")
        print("Le royaume est en danger et vous avez été élu pour en être le héros !")
        print("Explorez, Discutez, pour découvrir tous les secrets de ce monde et ce pourquoi vous avez attéri ici.")
        print("Bon courage !!!")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    
##############################
# Tkinter GUI Implementation #
##############################

class _StdoutRedirector:
    """Redirect sys.stdout writes into a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, msg):
        """Write message to the Text widget."""
        if msg:
            self.text_widget.configure(state="normal")
            self.text_widget.insert("end", msg)
            self.text_widget.see("end")
            self.text_widget.configure(state="disabled")

    def flush(self):
        """Flush method required by sys.stdout interface (no-op for Text widget)."""

class GameGUI(tk.Tk):
    """Tkinter GUI for the text-based adventure game.

    Layout layers:
    L3 (top): Split into left image area (600x400) and right buttons.
    L2 (middle): Scrolling terminal output.
    L1 (bottom): Command entry field.
    """

    IMAGE_WIDTH = 600
    IMAGE_HEIGHT = 400

    def __init__(self):
        super().__init__()
        self.title("TBA")
        self.geometry("900x700")  # Provide enough space
        self.minsize(900, 650)

        # Underlying game logic instance
        self.game = Game()

        # Ask player name via dialog (fallback to 'Joueur')
        name = simpledialog.askstring("Nom", "Entrez votre nom:", parent=self)
        if not name:
            name = "Joueur"
        self.game.setup(player_name=name)  # Pass name to avoid double prompt

        # Build UI layers
        self._build_layout()

        # Redirect stdout so game prints appear in terminal output area
        self.original_stdout = sys.stdout
        sys.stdout = _StdoutRedirector(self.text_output)

        # Print welcome text in GUI
        self.game.print_welcome()

        # Load initial room image
        self._update_room_image()

        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self._on_close)


    # -------- Layout construction --------
    def _build_layout(self):
        # Configure root grid: 3 rows (L3, L2, L1)
        self.grid_rowconfigure(0, weight=0)  # Image/buttons fixed height
        self.grid_rowconfigure(1, weight=1)  # Terminal output expands
        self.grid_rowconfigure(2, weight=0)  # Entry fixed
        self.grid_columnconfigure(0, weight=1)

        # L3 Top frame
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=6, pady=(6,3))
        top_frame.grid_columnconfigure(0, weight=0)
        top_frame.grid_columnconfigure(1, weight=1)

        # L3L Image area (left)
        image_frame = ttk.Frame(top_frame, width=self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)
        image_frame.grid(row=0, column=0, sticky="nw", padx=(0,6))
        image_frame.grid_propagate(False)  # Keep requested size
        self.canvas = tk.Canvas(image_frame,
                                width=self.IMAGE_WIDTH,
                                height=self.IMAGE_HEIGHT,
                                bg="#222")
        self.canvas.pack(fill="both", expand=True)

        # Initialize image reference (will be loaded by _update_room_image)
        self._image_ref = None  # Keep reference to prevent garbage collection
        # Initial image will be loaded after welcome message

        # L3R Buttons area (right)
        buttons_frame = ttk.Frame(top_frame)
        buttons_frame.grid(row=0, column=1, sticky="ne")
        for i in range(10):
            buttons_frame.grid_rowconfigure(i, weight=0)
        buttons_frame.grid_columnconfigure(0, weight=1)

        # Load button images (keep references to prevent garbage collection)
        assets_dir = Path(__file__).parent / 'assets'
        # Load pre-resized 50x50 PNG images for better quality
        self._btn_help = tk.PhotoImage(file=str(assets_dir / 'help-50.png'))
        self._btn_up = tk.PhotoImage(file=str(assets_dir / 'up-arrow-50.png'))
        self._btn_down = tk.PhotoImage(file=str(assets_dir / 'down-arrow-50.png'))
        self._btn_left = tk.PhotoImage(file=str(assets_dir / 'left-arrow-50.png'))
        self._btn_right = tk.PhotoImage(file=str(assets_dir / 'right-arrow-50.png'))
        self._btn_quit = tk.PhotoImage(file=str(assets_dir / 'quit-50.png'))

        # Command buttons
        tk.Button(buttons_frame,
                  image=self._btn_help,
                  command=lambda: self._send_command("help"),
                  bd=0).grid(row=0, column=0, sticky="ew", pady=2)
        # Movement buttons (N,E,S,O)
        move_frame = ttk.LabelFrame(buttons_frame, text="Déplacements")
        move_frame.grid(row=1, column=0, sticky="ew", pady=4)
        tk.Button(move_frame,
                  image=self._btn_up,
                  command=lambda: self._send_command("go N"),
                  bd=0).grid(row=0, column=0, columnspan=2)
        tk.Button(move_frame,
                  image=self._btn_left,
                  command=lambda: self._send_command("go O"),
                  bd=0).grid(row=1, column=0)
        tk.Button(move_frame,
                  image=self._btn_right,
                  command=lambda: self._send_command("go E"),
                  bd=0).grid(row=1, column=1)
        tk.Button(move_frame,
                  image=self._btn_down,
                  command=lambda: self._send_command("go S"),
                  bd=0).grid(row=2, column=0, columnspan=2)

        # Quit button
        tk.Button(buttons_frame,
                  image=self._btn_quit,
                  command=lambda: self._send_command("quit"),
                  bd=0).grid(row=2, column=0, sticky="ew", pady=(8,2))

        # L2 Terminal output area (Text + Scrollbar)
        output_frame = ttk.Frame(self)
        output_frame.grid(row=1, column=0, sticky="nsew", padx=6, pady=3)
        output_frame.grid_rowconfigure(0, weight=1)
        output_frame.grid_columnconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(output_frame, orient="vertical")
        self.text_output = tk.Text(output_frame,
                                   wrap="word",
                                   yscrollcommand=scrollbar.set,
                                   state="disabled",
                                   bg="#111", fg="#eee")
        scrollbar.config(command=self.text_output.yview)
        self.text_output.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # L1 Entry area
        entry_frame = ttk.Frame(self)
        entry_frame.grid(row=2, column=0, sticky="ew", padx=6, pady=(3,6))
        entry_frame.grid_columnconfigure(0, weight=1)

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(entry_frame, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()


    # -------- Image update --------
    def _update_room_image(self):
        """Update the canvas image based on the current room."""
        if not self.game.player or not self.game.player.current_room:
            return

        room = self.game.player.current_room
        assets_dir = Path(__file__).parent / 'assets'

        # Use room-specific image if available, otherwise fallback
        if room.image:
            image_path = assets_dir / room.image
        else:
            image_path = assets_dir / 'scene.png'

        try:
            # Load new image
            self._image_ref = tk.PhotoImage(file=str(image_path))
            # Clear canvas and redraw image
            self.canvas.delete("all")
            self.canvas.create_image(
                self.IMAGE_WIDTH/2,
                self.IMAGE_HEIGHT/2,
                image=self._image_ref
            )
        except (FileNotFoundError, tk.TclError):
            # Fallback to text if image not found or cannot be loaded
            self.canvas.delete("all")
            self.canvas.create_text(
                self.IMAGE_WIDTH/2,
                self.IMAGE_HEIGHT/2,
                text=f"Image: {room.name}",
                fill="white",
                font=("Helvetica", 18)
            )


    # -------- Event handlers --------
    def _on_enter(self, _event=None):
        """Handle Enter key press in the entry field."""
        value = self.entry_var.get().strip()
        if value:
            self._send_command(value)
        self.entry_var.set("")


    def _send_command(self, command):
        if self.game.finished:
            return
        # Echo the command in output area
        print(f"> {command}\n")
        self.game.process_command(command)
        # Update room image after command (in case player moved)
        self._update_room_image()
        if self.game.finished:
            # Disable further input and schedule close (brief delay to show farewell)
            self.entry.configure(state="disabled")
            self.after(600, self._on_close)


    def _on_close(self):
        # Restore stdout and destroy window
        sys.stdout = self.original_stdout
        self.destroy()


def main():
    """Entry point.

    If '--cli' is passed as an argument, start the classic console version.
    Otherwise launch the Tkinter GUI.
    Fallback to CLI if GUI cannot be initialized (e.g., headless environment).
    """
    args = sys.argv[1:]
    if '--cli' in args:
        Game().play()
        return
    try:
        app = GameGUI()
        app.mainloop()
    except tk.TclError as e:
        # Fallback to CLI if GUI fails (e.g., no DISPLAY, Tkinter not available)
        print(f"GUI indisponible ({e}). Passage en mode console.")
        Game().play()


if __name__ == "__main__":
    main()
