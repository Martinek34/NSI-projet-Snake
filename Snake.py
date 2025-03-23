


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
    plateau=[]
    for i in range(haut):
        plateau.append([])
        for j in range(larg):
            plateau[i].append(0)
    return plateau
  
# Données 

# création du serpent
def snake (plateau):
    """ 
    la fonction snake nous met a chaque fois la tete de serpent representée par 5 au milieu du plateau et 
    un morceau de son corps une case a gauche derrier la tete representée par le numéro 1. La fonction mange la liste plateau et elle retourne la liste plateau avec les valeurs 1 et 5 
    qui representent le crops et la tete comme on a deja dit
    """
    plateau[len(plateau)//2][len(plateau[0]//2)] = 5
    plateau[len(plateau)//2][(len(plateau[0]//2)-1] = 4
    return plateau

  
# Fonction pour placer un pomme (2) sur le plateau
def pomme(plateau):
    """
    Paramètres : tableau indexé de type list, la liste passé en argument doit être une liste de liste, qui représente un tableau carré. 
    Retourne : jeu_plateau de type list
    rette fonction est utilisée avec comme liste jeu_plateau
    variable mutable de portée globale.
    """
    pomme_x = random.randrange(0,len(plateau))
    pomme_y = random.randrange(0,len(plateau))
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
    bombe_y = random.randrange(0,len(plateau))
    plateau[bombe_x][bombe_y] = 3 # randrange choisit un numero dans une plage donne
    return plateau

   #Fonction pour verifiier la coision avec la bombe
def collision_bombe(plateau,ligne_bombe,colonne_bombe,ligne_tete,colonne_tete):
    """Cette fonction permet de vérifier si le serpent a mangé la bombe. 
    Elle retourne soit true soit false et si true elle tue le serpent """
    # ligne colonne representent la position de la tête du serpent
    if plateau[ligne_bombe][colonne_bombe] == plateau[ligne_tete][colonne_tete] :
        return True
        print("T'as perdu")
    else :
        return False

def collision_plateau(colonne_tete, ligne_tete, haut, larg):
    """
    Cette fonction permet de vérifier si la tête du serpent est en dehors du plateau et si elle heurte un mur, ce qui met fin au jeu.
    Paramètres : 
    - colonne_tete : entier représentant la colonne de la tête du serpent
    - ligne_tete : entier représentant la ligne de la tête du serpent
    - haut : liste contenant un seul entier représentant la hauteur du plateau
    - larg : liste contenant un seul entier représentant la largeur du plateau
    Retourne : 
    - booléen : True si la tête du serpent est en dehors des limites du plateau, sinon False
    Cette fonction est utilisée pour terminer le jeu si le serpent heurte un mur.
    """
    # Kontrola, zda hlava hada narazila do stěny
    if colonne_tete < 0:
        return True
    if colonne_tete >= larg[0]:
        return True
    if ligne_tete < 0:
        return True
    if ligne_tete >= haut[0]:
        return True
    return False

# Zone de test
colonne_tete = 15  # La colonne de la tete du serpent
ligne_tete = 0  # La ligne de la tete du serpent
haut = [15]  # hauteur du plateau de jeu
larg = [20]  # largeur du plateau de jeu

# Cela nous permet d'afficher que le joueur a perdu
if collision_plateau(colonne_tete, ligne_tete, haut, larg):
    print("Le serpent a frappé le mur ! Le jeu est terminé.")



#Fonction pour verifier la colission avec la pomme
def collision_pomme(plateau,ligne_pomme,colonne_pomme,ligne_tete,colonne_tete):
     """Cette fonction permet de vérifier si le serpent a mangé la pomme dons si le serpent va grandir. 
    Elle retourne soit true soit false et si true le serpent augmente d'un carré """
    # ligne colonne representent la position de la tête du serpent
     if plateau[ligne_pomme][colonne_pomme] == plateau[ligne_tete][colonne_tete] :
        return True
    else :
        return False


#fonction pour faire l'affichage du plateau
def affichage(liste_liste):
   for plateau in liste_liste :
        print(plateau)
    print()


# Programme principal
liste_test = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
affichage(liste_test)
print(bombe(liste_test)) 
liste_test = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
affichage(liste_test)

bombe(liste_test)
affichage(liste_test)

pomme(liste_test)
affichage(liste_test)

snake(liste_test)
affichage(liste_test)

# fonction pour avencé
# 4 représente la queue du serpent 5 la tete

def deplacement(jeu,car):
    """
    Paramètre : jeu de typoe list et car de type int
    fonction qui deplace la tete et la queue du serpent """

    # Chercher la position de la valeur 4 (en ligne et colonne)
    for i in range(len(jeu)) :
        for j in range(5):
            if jeu[i][j] == 4 :
                queue = [i,j]
            elif jeu[i][j] == 5 :
                tete = [i,j]
        print (tete)
    if car == 8 :
        # Deplacement vers le haut
        # Pour la tete
        if jeu[tete[i-1]] < 0 or jeu[tete[i+1]][tete[j]] == 3 or 1 or 4 :
            return False # permet l'arret du programme quand on perd
        #y a-t-il une pomme
        #  appelle sous fonction 
        elif jeu[tete[i-1]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i-1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i-1]][tete[j]] = 5
            liste[queue[i]][queue[j]] = 0
    
    elif car == 6 :
        # Deplacement vers la droite
        # Pour la tete
        if jeu[tete[j+1]] > len(jeu) or jeu[tete[i]][tete[j+1]] == 3 or 1 or 4:
            return False
        #y a-t-il une pomme
        #appelle sous fonction 
        if jeu[tete[i]][tete[j+1]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j+1]] = 5
            
        elif jeu[tete[i]][tete[j+1]] == 0:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j+1]] = 5
            liste[queue[i]][queue[j]] = 0
        print(b)
    elif car == 4 :
        # Deplacement vers le bas
        # Pour la tete
        if jeu[tete[i+1]] > len(jeu) or jeu[tete[i+1]][tete[j]] == 3 or 1 or 4:
            return False 
        #y a-t-il une pomme
        #  appelle sous fonction 
        elif jeu[tete[i+1]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i+1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i+1]][tete[j]] = 5
            liste[queue[i]][queue[j]] = 0
    elif car == 2 :
        # Deplacement vers la gauche
        # Pour la tete
        if jeu[tete[j-1]] < 0 or jeu[tete[i]][tete[j-1]] == 3 or 1 or 4:
            return False
        #y a-t-il une pomme
        #  appelle sous fonction 
        elif jeu[tete[i]][tete[j-1]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j-1]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j-1]] = 5
            liste[queue[i]][queue[j]] = 0
    return jeu



# program principal

def jouer ():
    jeu_plateau(16,16)
    snake(jeu_plateau)
    while True:
        direction = int(input())
        pomme(jeu_plateau)
        bombe(jeu_plateau)
        deplacement(jeu_plateau, direction)
        time.sleep(1) # la fonction time.sleep met le programme en pose pendant 1 seconde
    return jeu_plateau




fen = tkinter.Tk()
fen.title("Snake Game")
fen.resizable(False, False)
height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


fen.mainloop()













