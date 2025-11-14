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

    
    def deplacer_pion(self, positionA, positionB):
        """Valider le movement du pion et le deplacer et changer de joueur"""

    def options_mouvements(self, position):
        """Determiner les mouvements possibles pour le pion selectionne"""
        
    def terminer_partie(self):
        """Terminer la partie, determiner le vainqueur, et ajouter le score dans l'historique"""

    def is_terminer(self):
        """Determiner si la partie est terminee ou pas"""

    def lancer_partie(self):
        """Lancer une nouvelle partie avec les joueurs"""
        self.damier = damier.Damier()
        self.joueur1 = joueur.Joueur(nomJoueur1, "blanc")
        self.joueur2 = joueur.Joueur(nomJoueur2, "noir")
        premier = choice([self.joueur1, self.joueur2])
        premier.set_actif(True)