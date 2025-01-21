


####################### Projet NSI Snake ###########################

# impotrtation de la fonction random
import random

# creation du plateau de jeu
jeu_plateau : [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

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

# Initialisation du serpent (une liste de coordonnées)
snake = [[7, 7]]
jeu_plateau[7][7] = 1 

# Définir la direction du serpent
direction = 'droite'  # Possible: 'haut', 'bas', 'gauche', 'droite'

# Fonction pour déplacer le serpent
def deplacer_serpent():
  

    tete_x, tete_y = serpent[0]  # Position de la tête du serpent

    if direction == 'haut':
        tete_x -= 1
    elif direction == 'bas':
        tete_x += 1
    elif direction == 'gauche':
        tete_y -= 1
    elif direction == 'droite':
        tete_y += 1
