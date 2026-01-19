# TBA - Jeu d'Aventure Textuel avec Système de Quêtes

Cette branche contient une version du jeu d'aventure TBA (Text-Based Adventure) avec un système de quêtes intégré et une interface graphique.

# Guide utilisateur

## Description

TBA est un jeu d'aventure textuel avec interface graphique (Tkinter) où le joueur explore différents lieux, accomplit des quêtes et interagit avec l'environnement via des commandes textuelles.

**État actuel du projet (branche `tba-quests`) :**
- 14 lieux explorables
- Navigation par directions cardinales (N, E, S, O), U (Up) et D (Down)
- **Système de quêtes complet** avec objectifs et récompenses
- Gestion des quêtes actives et complétées
- Suivi automatique de la progression des objectifs
- Statistiques de déplacement du joueur 
- Interface graphique avec Tkinter
- Système de commandes extensible
- Images et icônes pour améliorer l'expérience visuelle

Cette version introduit un système de quêtes qui enrichit considérablement l'expérience de jeu et sert de base pour des mécaniques plus complexes.

## Lancement du jeu

Pour démarrer le jeu, exécuter simplement :
```bash
python game.py
```

Le jeu s'ouvrira dans une fenêtre graphique avec une interface utilisateur.

On peut toujours exécuter le jeu dans un terminal:
```bash
python game.py --cli
```

## Commandes disponibles

### Commandes de base
- `help` : Afficher l'aide et la liste des commandes
- `quit` : Quitter le jeu
- `go <direction>` : Se déplacer dans une direction (N, E, S, O)
- `history` : Afficher le parcours du joueur
- `look` : Afficher la liste des items et des personnages présents dans la pièce
- `back` : Revenir dans la dernière pièce visitée
- `take <objet>` : Prendre un Item présent dans la pièce où se situe le joueur
- `drop <objet>` : Déposer un Item de l'inventaire dans la pièce actuelle
- `check` : Afficher la liste des Items contenus dans l'inventaire du joueur
- `talk <personnage>` : Parler à un personnage présent dans la pièce
- `charge` : Mémoriser la pièce actuelle si l'Item "beamer" est présent dans l'inventaire
- `use <objet>` : Utiliser un Item présent dans l'inventaire


### Commandes de quêtes
- `quests` : Afficher la liste de toutes les quêtes disponibles
- `quest <titre>` : Afficher les détails d'une quête spécifique
- `activate <titre>` : Activer une quête pour commencer à la suivre

## Système de Quêtes

Le système de quêtes permet de :
- Définir des objectifs à accomplir
- Suivre automatiquement la progression
- Gérer plusieurs quêtes simultanément
- Obtenir des récompenses à la completion

**Types d'objectifs disponibles :**
- Objectifs de visite : visiter un lieu spécifique
- Objectifs de compteur : effectuer une action un certain nombre de fois (ex: se déplacer 10 fois)

## Structuration

Le projet est organisé en 8 modules contenant chacun une ou plusieurs classes :

### Modules principaux

- **`game.py` / `Game`** : Gestion de l'état du jeu, de l'environnement et de l'interface avec le joueur
- **`game.py` / `GameGUI`** : Classe qui gère l'interface graphique Tkinter
- **`room.py` / `Room`** : Propriétés génériques d'un lieu (nom, description, sorties, Items & personnages présents)
- **`item.py` / `Item`** : Propriétés génériques d'un objet (nom, description, poids)
- **`player.py` / `Player`** : Représentation du joueur avec gestion des déplacements et intégration du QuestManager
- **`character.py` / `Character`** : Représentation d'un PNJ avec gestion des déplacements aléatoires et des interactions
- **`command.py` / `Command`** : Structure des commandes avec leurs paramètres et actions associées
- **`actions.py` / `Actions`** : Méthodes statiques définissant toutes les actions exécutables (déplacements, gestion des quêtes, etc.)
- **`quest.py`** : 
  - `Quest` : Représentation d'une quête avec ses objectifs
  - `Objective` : Classe de base pour les objectifs
  - `RoomObjective` : Objectif de visite d'un lieu
  - `CounterObjective` : Objectif basé sur un compteur
  - `QuestManager` : Gestionnaire des quêtes du joueur

### Dossier assets

Le dossier `assets/` contient les ressources graphiques :
- Icônes de navigation (flèches directionnelles)
- Icônes d'aide et de sortie
- Images des différents lieux du jeu
- Diagramme des classes sous forme de fichier png

## Architecture

Le jeu utilise une architecture orientée objet avec gestion d'événements :

1. **Game** initialise le jeu et les quêtes disponibles
2. **Player** contient un `QuestManager` qui suit les quêtes actives
3. **QuestManager** vérifie automatiquement la progression lors des actions du joueur
4. **Objectives** définissent différents types de conditions à remplir
5. **Room** représente chaque lieu avec ses connexions
6. **Command** encapsule les commandes utilisateur
7. **Actions** implémente les interactions avec le joueur


## Description

Le jeu se joue dans un univers médiéval avec un village central divisé en deux parties entouré de lieux dans le même thème tels qu'un château, une forêt, des ruines, une grotte, etc. Vous plongez directement dans une avanture dans laquelle le royaume à besoin de vous pour être sauvé d'une menace. Explorez, discuter, accomplissez des quêtes pour atteindre l'objectif final. Différents items et personnages sont disponibles pour intéragir avec le monde et vous guider tout au long de votre aventure. 

## Conditions de Victoire/Défaite 

Victoire : Vous devez réaliser les quêtes dans l'ordre puis finir par aller dans la grotte avec l'ensemble de l'équipement nécessaire (sword & shield) pour abattre le dragon.

Défaite : Si vous vous aventurer dans la grotte sans équipement vous êtes directement éliminé.

# Guide développeur : diagramme des classes
![alt text](diagramme_classes.png)


# Perspective de développement

Certains items implémentés dans le jeu ne sont pas utiles (pièces, potion, clés). 
Nous pourrions rajouter : 
- une action d'achat dans la boutique avec les pièces
- un système de point de vie et de guérison 
- le dévérouillage de portes grâce aux clés
- un système de réapparition lorsque que l'on est éliminé au lieu de mettre fin à la partie
