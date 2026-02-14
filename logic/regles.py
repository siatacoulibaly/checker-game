## Definir les regles du jeu

import model.damier as damier
import model.joueur  as joueur
import model.node as node


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
                elif get_pion_elimine_in_deplacement_diagonal(damier, position_a, position_intermediaire, joueur):
                    return True
                
    return False


def get_pion_elimine_in_deplacement_diagonal(damier, position_a, position_b, joueur):
    """Verifier les conditions pour qu'une dame fasse un long deplacement diagonal 
    tout en eliminant un pion de l'adversaire | Retourner le pion elimine"""
    
    pion = damier.get_item(position_a)
    pion_elimine = None

    #Seulement autoriser les pions du joueur de tour d'etre deplacés dans une case vide
    if is_pion_jouable(damier, position_a, position_b, joueur):
        #Verifier le deplacement diagonal d'une dame      
        if abs(position_a[0] - position_b[0]) == abs(position_a[1] - position_b[1]) and pion.is_dame():
            position_intermediaire = position_a
            pas_ligne = 1 if position_b[0] > position_a[0] else -1
            pas_colonne = 1 if position_b[1] > position_a[1] else -1
            elimine = 0

            while True:
                #Parcourir les cases intermediaires entre la position de depart (position_a)
                # et la position de destination (position_b)
                ligne_intermediaire = position_intermediaire[0] + pas_ligne
                colonne_intermediaire = position_intermediaire[1] + pas_colonne
                position_intermediaire = (ligne_intermediaire, colonne_intermediaire)
                pion_potentiel_intermediaire = damier.get_item(position_intermediaire)
                
                #Arreter la loupe quand on atteint la position de destination et autoriser le mouvement
                if position_intermediaire == position_b and elimine != 1:
                    return None
                
                #Autoriser le mouvement si la dame elimine exactement 1 pion de l'adversaire avant 
                # d'arriver a la position de destination
                if position_intermediaire == position_b and elimine == 1:
                    return pion_elimine
                
                #Continuer a verifier la case suivante si la case actuelle est vide
                elif pion_potentiel_intermediaire == None:
                    continue

                #Compter le nombre de pions adverse entre la position de depart et 
                # la position de destination 
                elif pion_potentiel_intermediaire.get_couleur() != joueur.get_couleur():
                    elimine += 1
                    pion_elimine = pion_potentiel_intermediaire
                    continue
                
    return pion_elimine


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
    elif get_pion_elimine_in_deplacement_diagonal(damier, position_a, position_b, joueur):
        return 1
    
    return 0


def add_node(damier, node_final, position, couleur):
    """Ajouter une section a un parcours"""
    profondeur_new = node_final.get_profondeur() + 1
    is_dame = False
    if node_final.is_dame() or devient_dame(damier, position, couleur):
        is_dame = True
    node_final_new = node.Node(position, profondeur_new, is_dame)
    node_final_new.set_precedent(node)
    return node_final_new


def get_pion_elimine(damier, node_a, node_b, joueur):
    """Obtenir la position du pion elimine"""
    if not node_a.is_dame() and not node_b.is_dame():
        ligne_elimine = (node_a.get_position()[0] + node_b.get_position()[0]) / 2
        colonne_elimine = (node_a.get_position()[1] + node_b.get_position()[1]) / 2
        position_elimine = (ligne_elimine, colonne_elimine)
    else:
        position_elimine = get_pion_elimine_in_deplacement_diagonal(damier, node_a.get_position(), node_b.get_position(), joueur)
    return position_elimine

def is_parcours_possible(damier, node_final, joueur):
    """Verifier qu'une section du parcours ne se repete pas"""
    node_a = node_final
    node_b = node_final.get_precedent()
    pion_intermediaire = get_pion_elimine(damier, node_a.get_position(), node_b.get_position(), joueur)

    node_intermediaire = node_b
    while node_intermediaire.get_precedent():
        pion_intermediaire_a_verifier = get_pion_elimine(damier, node_intermediaire, node_intermediaire.get_precedent(), joueur)
        if pion_intermediaire_a_verifier == pion_intermediaire:
            return False
        node_intermediaire = node_intermediaire.get_precedent()
    return True


def get_plus_longs_parcours(liste_parcours):
    """Obtenir les parcours avec les plus grandes profondeurs, les gains maximums"""
    liste_plus_long_parcours = []
    if len(liste_parcours) != 0:
        liste_parcours.sort(key = lambda node_item: node_item.get_profondeur(), reverse = True)
        profondeur_max = liste_parcours[0].get_profondeur()
        
        for parcours in liste_parcours:
            if parcours.get_profondeur() == profondeur_max:
                liste_plus_long_parcours.append(parcours)
            else:
                break
    return liste_plus_long_parcours


def get_gains_possibles(damier, joueur):
    """"""


def get_deplacements_autorises(damier, position_a, joueur):
    """Determiner tous les deplacements autorisés"""
    
    root_node = node.Node(position_a, 0, damier.get_item(position_a).isdame())
    liste_destinations = []
    liste_destinations_potentielles_simples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    liste_destinations_potentielles_eliminant = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
    liste_parcours_a_tester = [root_node]
    liste_parcours_testes = []

    #Verifier les possibilites de deplacements simples (une case a la fois / deplacement en 1)
    for position in liste_destinations_potentielles_simples:
        ligne_candidat = position_a[0] + position[0]
        colonne_candidat = position_a[1] + position[1]
        position_candidat = (ligne_candidat, colonne_candidat)
        if is_deplacement_autorise(damier, position_a, position_candidat, joueur):
            final_node = add_node(damier, root_node, position_candidat, joueur.get_couleur())
            liste_parcours_testes.append(final_node)

    #Verifier les possibilites de deplacements eliminants (deplacement en 2). Apres chaque deplacement, 
    # on verifie les possibilites de deplacement eliminant additionnel
    if not damier.get_item(position_a).is_dame():
        while len(liste_parcours_a_tester) != 0:
            node_teste = liste_parcours_a_tester[-1]
            liste_parcours_a_tester = liste_parcours_a_tester[:-1]
            ajout = False
            for position in liste_destinations_potentielles_eliminant:
                ligne_candidat = node_teste.get_position()[0] + position[0]
                colonne_candidat = node_teste.get_position()[1] + position[1]
                position_candidat = (ligne_candidat, colonne_candidat)
                node_candidat = add_node(damier, node_teste, position_candidat, joueur.get_couleur())

                if is_deplacement_autorise(damier, node_teste.get_position(), position_candidat, joueur) and is_parcours_possible(damier, node_candidat, joueur):
                    liste_parcours_a_tester.append(node_candidat)
                    ajout = True
                
            if ajout: 
                liste_parcours_testes.append(node_teste)

    #Verifier les possibilites de deplacements eliminants pour dame. Apres chaque deplacement, 
    # on verifie les possibilites de deplacement eliminant additionnel
    else:
        while len(liste_parcours_a_tester) != 0:
            node_teste = liste_parcours_a_tester[-1]
            liste_parcours_a_tester = liste_parcours_a_tester[:-1]
            ajout = False

    #Recuperer les parcours les plus longs
    liste_destinations = get_plus_longs_parcours(liste_parcours_testes)
    return liste_destinations
            


def devient_dame(damier, position, couleur = None):
    """Definir la condition pour qu'un pion devienne une dame"""
    pion = damier.get_item(position)

    #Si le pion blanc est sur la 1ere ligne du blanc, alors il devient une dame. 
    #De meme pour le pion noir, s'il est sur la 1ere ligne du blanc, alors il devient une dame.
    if not pion and couleur:
        if (couleur == "blanc" and position[0] == 0) or (couleur == "noir" and position[0] == 9):
            pion.set_dame()
    elif pion:
        if (pion.get_couleur() == "blanc" and position[0] == 0) or (pion.get_couleur() == "noir" and position[0] == 9):
            pion.set_dame()
    else: 
        NotImplemented
