


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
    plateau[len(plateau)//2][len(plateau[0]//2] = 5
    plateau[len(plateau)//2][(len(plateau[0]//2)-1] = 1
    return plateau

  
# Fonction pour placer un pomme (2) sur le plateau
def pomme(plateau):
    """
    Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
    Retourne : jeu_plateau de type list
    rette fonction est utilisée avec comme liste jeu_plateau
    variable mutable de portée globale.
    """
    pomme_x = random.randrange(0,len(liste))
    pomme_y = random.randrange(0,len(liste))
    plateau[pomme_x][pomme_y] = 2 # randrange choisit un numero dans une plage donne
    return plateau



# Fonction pour placer une bombe (3) sur le plateau
def bombe(plateau) : 
    """ Cette fonction permet d'ajouter une bombe sur le plateau qui tue le serpent s'il la mange
  Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
  Retourne : jeu_plateau de type list
  Cette fonction est utilisée avec comme liste jeu_plateau
  variable mutable de portée globale.
  """
    bombe_x = random.randrange(0,len(plateau))
    bombe_y = random.randrange(0,len(plateau)
    plateau[bombe_x][bombe_y] = 3 # randrange choisit un numero dans une plage donne
    return plateau

   #Fonction pour verifiier la coision avec la bombe
def collision_bombe(plateau,ligne_bombe,colonne_bombe,ligne_tete,colonne_tete):
    """Cette fonction permet de vérifier si le serpent a mangé la bombe. 
    Elle retourne soit true soit false et si true elle tue le serpent """
    # ligne colonne representent la position de la tête du serpent
    if plateau[ligne_bombe][colonne_bombe] == plateau[ligne_tete][colonne_tete] :
        return True
    else :
        return False
        
#Fonction pour verifier la colission avec la pomme
def collision_pomme(plateau,ligne_pomme,colonne_pomme,ligne_tete,colonne_tete):
     """Cette fonction permet de vérifier si le serpent a mangé la pomme dons si le serpent va grandir. 
    Elle retourne soit true soit false et si true le serpent augmente d'un carré """
    # ligne colonne representent la position de la tête du serpent
    if plateau[ligne_pomme][colonne_pomme] == plateau[ligne_tete][colonne_tete] :
        return 
    else :
        return False


#fonction pour faire l'affichage du plateau
def affichage(liste_liste):
    for plateau in liste_liste :
        print(plateau)

# Programme principal
liste_test = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
affichage(liste_test)
print(bombe(liste_test)) 



# program principal

jeu_plateau("selection de la hauteur du plateau","selection de la longueur du plateau")
pomme(jeu_plateau)
bombe(jeu_plateau)
direction = "bas"
move(jeu_plateau,direction,snake)
if fen.bind('<d>'):
    direction = "d"
if fen.bind('<z>'):
    direction = "z"
if fen.bind('<q>'):
    direction = "q"
if fen.bind('<s>'):
    direction = "s"



# interface graphique
fen = tkinker.Tk()
fen.title("Snake Game")
fen.resizable(False, False)
height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


fen.mainloop()













