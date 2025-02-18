


####################### Projet NSI Snake ###########################

# importation de tkinter pour l'interface graphique
import tkinter

# impotrtation des fonctions
import random
import os
import time
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

# création du serpent
def snake (plateau):
    liste[5][5] = 5
    liste[5][4] = 1
# direction
def direction(event):
    direction = ''
    if event == "z" :
        direction = "haut"
    elif event == "s" :
        direction = "bas"
    elif event == "d" :
        direction = "gauche"
    elif event == "q" :
        direction = "droite"
  
# Fonction pour placer un pomme (2) sur le plateau
def pomme (liste):
    """
    Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
    Retourne : jeu_plateau de type list
    rette fonction est utilisée avec comme liste jeu_plateau
    variable mutable de portée globale.
    Cette fonction remplie le tableau ar des nombres entiers compris entre 0 et la longeur du tableau donnée aléatoirement. 
    """
    liste[random.randrange(0,len(liste))][random.randrange(0,len(liste))] = 2 # randrange choisi un numero dans une plage donne
    return liste


# Fonction pour faire bouger le snake
def move_snake(plateau, direction, snake):
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
    if direction == "z":
        tete_y -= 1
    elif direction == "s":
        tete_y += 1
    elif direction == "q":
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
   """
  Cette fonction permet d'ajouter une bombe sur le plateau qui tue le serpent si il la mange
  Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
  Retourne : jeu_plateau de type list
  Cette fonction est utilisée avec comme liste jeu_plateau
  variable mutable de portée globale.
  Cette fonction remplie le tableau ar des nombres entiers compris entre 0 et la longeur du tableau donnée aléatoirement. 
  """
    liste[random.randrange(0,len(liste))][random.randrange(0,len(liste))] = 3 # randrange choisit un numero dans une plage donne
    return liste
#Fonction pour verifiier la coision
def collision(ligne,colonne):
    # ligne colonne representent la position de la tête du serpent
    liste_test[ligne][colonne] == 3 :
        print("T'as perdu na !")

def affichage(liste_liste):
    for liste in liste_liste :
        print(liste)

# Programme principal
liste_test = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
affichage(liste_test)
print(bombe(liste_test)) 



# fonction principal
def init ():
    jeu_plateau("selection de la hauteur du plateau","selection de la longueur du plateau")





# interface graphique
window = tkinker.Tk()
window.title("Snake Game")
window.resizable(False, False)
-
                height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
