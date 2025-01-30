


####################### Projet NSI Snake ###########################

# importation de tkinter pour l'interface graphique
import tkinter as tk

# impotrtation des fonctions
#import random
#import os
#import time
# creation du plateau de jeu
def jeu_plateau(haut, larg):
    ''' 
    parametres : hauteur et largeur du plateau
    retourne : le plateau de jeu (liste) '''
    liste=[]
    for i in range(haut):
        liste.append([])
        for j in range(larg):
            liste[i].append(0)
    return liste
  
# Données 


  
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
  assert (len(liste) == len(ligne[0],"vous ne respectez pas la condition de passer un tableau carré en argument")
  liste[random(0,len(liste))][random(0,len(liste[0])] = 2
  return liste
# Zone de test
pomme(jeu_plateau)


# Fonction pour faire bouger le snake
def move_snake(plateau, snake, direction):
"""
Déplace le serpent dans la direction spécifiée et vérifie les collisions.
Paramètres : direction (str) : La direction dans laquelle le serpent doit se déplacer. Peut être l'une des valeurs suivantes :
        - "w" : haut
        - "s" : bas
        - "a" : gauche
        - "d" : droite
    - snake (list) : Liste représentant les coordonnées des segments du serpent. La dernière position dans la liste (`snake[-1]`) est la tête du serpent.
    - plateau (list de list) : Le plateau de jeu, représenté par une liste de listes. Chaque sous-liste est une ligne du plateau, et chaque élément représente une case du plateau.
Retour : Retourne `True` si le serpent a été déplacé avec succès (pas de collision), ou `False` en cas de collision (avec lui-même ou les bords du plateau).
"""
    tete_x, tete_y = snake[-1]
    if direction == "w":
        tete_y -= 1
    elif direction == "s":
        tete_y += 1
    elif direction == "a":
        tete_x -= 1
    elif direction == "d":
        tete_x += 1

    nouvelle_tete = [tete_x, tete_y]
    if nouvelle_tete in snake or tete_x < 0 or tete_y < 0 or tete_x >= len(plateau[0]) or tete_y >= len(plateau):
        return False
    #Pré-condition
    snake.append(new_head)
    if board[head_y][head_x] == "F":
        place_food(board, snake)
    else:
        tail = snake.pop(0)
        board[tail[1]][tail[0]] = "."

    board[head_y][head_x] = "S"
    return True
# Fonction pour placer une bombe (3) sur le plateau
def bombe(liste) : 

# interface graphique
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOUR,
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
