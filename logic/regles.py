## Definir les regles du jeu

import model.damier as damier
import model.joueur  as joueur


def is_pion_jouable(damier, position_a, position_b, joueur):
    pion = damier.get_item(position_a)
    pion_potentiel_destination = damier.get_item(position_b)
    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if joueur.get_couleur() == pion.get_couleur() and pion_potentiel_destination == None:
        return True
    
    return False

def is_deplacement_simple(damier, position_a, position_b, joueur):
    """Definir les conditions pour le deplacement d'un de sa position a sa ligne avant immediate"""
    
    pion = damier.get_item(position_a)

    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if is_pion_jouable(damier, position_a, position_b, joueur):
        #Verifier la condition de deplacement d'un pion sur sa ligne superieure immediate, excepté la dame qui peut avancer et reculer
        if abs(position_b[0] - position_a[0]) == 1 and abs(position_b[1] - position_a[1]) == 1:
            
            if pion.get_couleur() == "noir" and position_b[0] > position_a[0]:
                return True
            elif pion.get_couleur() == "blanc" and position_b[0] < position_a[0]:
                return True
            elif pion.is_dame():
                return True
            
    return False


def is_deplacement_eliminant(damier, position_a, position_b, joueur):
    """Verifier les conditions pour deplacer un pion en eliminant un pion de l'adversaire"""
   
    pion = damier.get_item(position_a)

    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if is_pion_jouable(damier, position_a, position_b, joueur):

        #Verifier la condiition de deplacement en cas d'elimination de pion du joueur adverse. 
        #Tout pion peut eliminer le pion adverse en avancant ou reculant
        if abs(position_b[0] - position_a[0]) == 2 and abs(position_b[1] - position_a[1]) == 2:
            ligne_centre = (position_a[0] + position_b[0])/2
            colonne_centre = (position_a[1] + position_b[1])/2
            position_centre = (ligne_centre, colonne_centre)
            pion_potentiel_centre = damier.get_item(position_centre)

            #Verifier qu'il y a un pion du joueur adverse a eliminer
            if pion_potentiel_centre != None and pion_potentiel_centre.get_couleur() != pion.get_couleur():
              return True
            
    return False

def is_deplacement_diagonal(damier, position_a, position_b, joueur):
    """Verifier les conditions pour qu'une dame fasse un long deplacement diagonal"""
    
    pion = damier.get_item(position_a)

    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if is_pion_jouable(damier, position_a, position_b, joueur):
        #Verifier le deplacement diagonal d'une dame      
        if abs(position_a[0] - position_b[0]) == abs(position_a[1] - position_b[1]) and pion.is_dame():
            position_intermediaire = position_a
            pas_ligne = 1 if position_b[0] > position_a[0] else -1
            pas_colonne = 1 if position_b[1] > position_a[1] else -1

            while True:
                #Parcourir les cases intermediaires entre la position de depart (position_a)
                # et la position de destination (position_b)
                ligne_intermediaire = position_intermediaire[0] + pas_ligne
                colonne_intermediaire = position_intermediaire[1] + pas_colonne
                position_intermediaire = (ligne_intermediaire, colonne_intermediaire)
                pion_potentiel_intermediaire = damier.get_item(position_intermediaire)
                
                #Arreter la loupe quand on atteint la position de destination et autoriser le mouvement
                if position_intermediaire == position_b:
                    return True
            
                #Continuer a verifier la case suivante si la case actuelle est vide
                elif pion_potentiel_intermediaire == None:
                    continue
                
                #Arreter la loupe quand on croise un pion du joueur dont c'est le tour et 
                # ne pas autoriser le mouvement. La dame d'une couleur ne peut sauter un pion 
                # de la meme couleur
                elif pion_potentiel_intermediaire.get_couleur() == joueur.get_couleur():
                    return False

                #Autoriser le mouvement si la dame elimine 1 pion de l'adversaire
                elif is_deplacement_diagonal_eliminant(damier, position_a, position_b, joueur):
                    return True
                
    return False


def is_deplacement_diagonal_eliminant(damier, position_a, position_b, joueur):
    """Verifier les conditions pour qu'une dame fasse un long deplacement diagonal 
    tout en eliminant un pion de l'adversaire"""
    
    pion = damier.get_item(position_a)

    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if is_pion_jouable(damier, position_a, position_b, joueur):
        #Verifier le deplacement diagonal d'une dame      
        if abs(position_a[0] - position_b[0]) == abs(position_a[1] - position_b[1]) and pion.is_dame():
            position_intermediaire = position_a
            pas_ligne = 1 if position_b[0] > position_a[0] else -1
            pas_colonne = 1 if position_b[1] > position_a[1] else -1

            while True:
                #Parcourir les cases intermediaires entre la position de depart (position_a)
                # et la position de destination (position_b)
                ligne_intermediaire = position_intermediaire[0] + pas_ligne
                colonne_intermediaire = position_intermediaire[1] + pas_colonne
                position_intermediaire = (ligne_intermediaire, colonne_intermediaire)
                pion_potentiel_intermediaire = damier.get_item(position_intermediaire)
                
                #Arreter la loupe quand on atteint la position de destination et autoriser le mouvement
                if position_intermediaire == position_b:
                    return False
                
                #Continuer a verifier la case suivante si la case actuelle est vide
                elif pion_potentiel_intermediaire == None:
                    continue

                #Autoriser le mouvement si la dame elimine 1 pion de l'adversaire. 
                # Dans ce cas, la position de destination devrait etre juste apres 
                # le pion adverse suivant sa trajectoire
                elif pion_potentiel_intermediaire.get_couleur() != joueur.get_couleur():
                    ligne_intermediaire = position_intermediaire[0] + pas_ligne
                    colonne_intermediaire = position_intermediaire[1] + pas_colonne
                    position_intermediaire = (ligne_intermediaire, colonne_intermediaire)
                    if position_intermediaire != position_b:
                        return False
                    return True
                
    return False


def is_deplacement_autorise(damier, position_a, position_b, joueur):
    """Obtenir les deplacements autorisés d'un pion"""
    
    #Verifier la condition de deplacement d'un pion sur sa ligne superieure immediate, excepté la dame qui peut avancer et reculer
    if is_deplacement_simple(damier, position_a, position_b, joueur):
        return True
            
    #Verifier la condiition de deplacement en cas d'elimination de pion du joueur adverse. 
    #Tout pion peut eliminer le pion adverse en avancant ou reculant
    elif is_deplacement_eliminant(damier, position_a, position_b, joueur):
        return True

    #Verifier le deplacement diagonal d'une dame      
    elif is_deplacement_diagonal(damier, position_a, position_b, joueur):
        return True


    return False


def get_gain(damier, position_a, position_b, joueur):
    """Definir les conditions pour obtenir un point, apres avoir eliminer un pion de l'adversaire"""
    if is_deplacement_eliminant(damier, position_a, position_b, joueur):
        return 1
    elif is_deplacement_diagonal_eliminant(damier, position_a, position_b, joueur):
        return 1
    
    return 0


def get_gains_possibles(damier, joueur):
    """"""

def get_deplacements_autorises(damier, position_a, joueur):
    """Determiner tous les deplacements autorisés"""
    liste_destinations = []


def devient_dame(damier, position):
    """Definir la condition pour qu'un pion devienne une dame"""
    pion = damier.get_item(position)

    #Si le pion blanc est sur la 1ere ligne du blanc, alors il devient une dame. 
    #De meme pour le pion noir, s'il est sur la 1ere ligne du blanc, alors il devient une dame.
    if (pion.get_couleur() == "blanc" and position[0] == 0) or (pion.get_couleur() == "noir" and position[0] == 9):
        pion.set_dame()
