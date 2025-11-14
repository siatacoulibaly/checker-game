## Creer la classe Joueur

class Joueur: 
    def __init__(self, nom, couleur):
        self._nom = nom
        self._couleur = couleur
        self.score = 0
        self.actif = False

    @property
    def nom(self):
        return self._nom
    
    @property
    def couleur(self):
        return self._couleur
    
    def get_nom(self):
        return self._nom
    
    def get_couleur(self):
        return self._couleur
    
    def add_score(self, points):
        self.score += points

    def set_actif(self, actif):
        self.actif = actif

    def is_actif(self):
        return self.actif