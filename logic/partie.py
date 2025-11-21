## Definir la une partie de jeu

import model.joueur as joueur
import model.pion as pion
import model.damier as damier
import regles
from random import choice


nomJoueur1 = input("Entrer le nom du joueur 1 (Pions Blancs): ")
nomJoueur2 = input("Entrer le nom du joueur 2 (Pions Noirs): ")


class Partie:
    def __init__(self):
        """Initier la classe Partie"""
        self.lancer_partie()
        self.historique = []

    def changer_joueur(self):
        self.joueur1.set_actif(not self.joueur1.is_actif())
        self.joueur2.set_actif(not self.joueur2.is_actif())

    def tour_de_jouer(self):
        """Retourner le joueur actif"""
        if self.joueur1.is_actif():
            return self.joueur1
        return self.joueur2

    
    def deplacer_pion(self, position_a, position_b):
        """Valider le movement du pion et le deplacer et changer de joueur"""
        if regles.is_deplacement_autorise(self.damier, position_a, position_b, self.tour_de_jouer()):
            self.damier.move_pion(position_a, position_b)
            return True
        return False


    def options_mouvements(self, position):
        """Determiner les mouvements possibles pour le pion selectionne"""
        
    def terminer_partie(self):
        """Terminer la partie, determiner le vainqueur, et ajouter le score dans l'historique"""
        self.en_cours = False
        self.historique.append((self.joueur1.get_score(), self.joueur2.get_score()))
        return self.get_vainqueur()
        

    def get_vainqueur(self):
        if self.joueur1.get_score() > self.joueur2.get_score():
            self.vainqueur = self.joueur1
        elif self.joueur1.get_score() < self.joueur2.get_score():
            self.vainqueur = self.joueur2
        else:
            self.vainqueur = None
        
        return self.vainqueur

    def is_en_cours(self):
        """Determiner si la partie est terminee ou pas"""
        return self.en_cours

    def lancer_partie(self):
        """Lancer une nouvelle partie avec les joueurs"""
        self.damier = damier.Damier()
        self.joueur1 = joueur.Joueur(nomJoueur1, "blanc")
        self.joueur2 = joueur.Joueur(nomJoueur2, "noir")
        premier = choice([self.joueur1, self.joueur2])
        premier.set_actif(True)
        self.en_cours = True