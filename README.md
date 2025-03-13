# test
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
            if jeu[i][j] == 5 :
                tete = [i,j]
    
    if car == "8" :
        # Deplacement vers le haut
        # Pour la tete
        if jeu[tete[i]] < 0 or jeu[tete[i+1]][tete[j]] == 3 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i-1]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i-1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i-1]][tete[j]] = 5
            liste[queue[i]][queue[j]] = 0
    
    elif car == "6" :
        # Deplacement vers la droite
        # Pour la tete
        if jeu[tete[j]] > len(jeu) or jeu[tete[i]][tete[j+1]] == 3 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j+1]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j+1]] = 5
            
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j+1]] = 5
            liste[queue[i]][queue[j]] = 0

    elif car == "4" :
        # Deplacement vers le bas
        # Pour la tete
        if jeu[tete[i]] > len(jeu) or jeu[tete[i+1]][tete[j]] == 3 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i+1]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i+1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i+1]][tete[j]] = 5
            liste[queue[i]][queue[j]] = 0
        return jeu
    elif car == "2" :
        # Deplacement vers la gauche
        # Pour la tete
        if jeu[tete[j]] < 0 or jeu[tete[i]][tete[j-1]] == 3 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j-1]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j-1]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j-1]] = 5
            liste[queue[i]][queue[j]] = 0
     return jeu


# zone de test
jeu = [[4,5,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]

print(deplacement(jeu,6))


        
def affichage(liste) :
    """ fonction temporaire, avant l'interface graphique """
    for ligne in range(len(liste)) :
        print(ligne)
