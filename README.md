# test
# 4 représente la queue du serpent 5 la tete

jeu = [[4,5,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]



def deplacement(jeu,car):
    """ fonction qui deplace la tete et la queue du serpent """
    # Chercher la position de la valuer 4 (en ligne et colonne)
    for i in range(len(jeu)) :
        for j in range(5):
            if jeu[i][j] == 4 :
                queue = [i,j]
            if jeu[i][j] == 5 :
                tete = [i,j] 
    if car == "8" :
        # Deplacement vers le haut
        # Pour la tete
        print(bgd)
        if jeu[tete[i]][tete[j]] <= 0 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i-1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i-1]][tete[j]] = 5
    if car == "6" :
        # Deplacement vers la droite
        # Pour la tete
        if jeu[tete[i]][tete[j]] != 1 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j+1]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j+1]] = 5
    if car == "4" :
        # Deplacement vers le bas
        # Pour la tete
        if jeu[tete[i]][tete[j]] != 1 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i+1]][tete[j]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i+1]][tete[j]] = 5
    if car == "2" :
        # Deplacement vers la gauche
        # Pour la tete
        if jeu[tete[i]][tete[j]] != 1 :
            return "t'es mort"
        #y a-t-il une pomme
      #  appelle sous fonction 
        if jeu[tete[i]][tete[j]] == 2:
            liste[tete[i]][tete[j]] = 1
            liste[tete[i]][tete[j-1]] = 5
        else:
            liste[tete[i]][tete[j]] = 4
            liste[tete[i]][tete[j-1]] = 5


    
        
        
def affichage(liste) :
    """ fonction temporaire, avant l'interface graphique """
    for ligne in range(len(jeu)) :
        print(ligne)
