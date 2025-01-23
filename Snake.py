


####################### Projet NSI Snake ###########################

# importation de tkinter pour l'interface graphique
import tkinter as tk

# impotrtation de la fonction random
import random

# creation du plateau de jeu
def jeu_plateau ()
for i in range (16):
  

# Fonction pour placer un pomme (2) sur le plateau
def pomme (liste):
  """
  Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
  Retourne : jeu_plateau de type list
  Cette fonction est utilisée avec comme liste jeu_plateau
  variable mutable de portée globale.
  Cette fonction remplie le tableau ar des nombres entiers compris entre 0 et la longeur du tableau donnée aléatoirement. 
  """
  # Pré-condition :
  assert (len(liste)=len(ligne[0],"vous ne respectez pas la condition de passer un tableau carré en argument")
  liste[random(0,len(liste))][random(0,len(liste[0])] = 2
  return liste
# Zone de test
pomme(jeu_plateau)

# Initialisation du serpent
def init(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

  for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)

# Définir la direction du serpent


# interface graphique
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOUR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
