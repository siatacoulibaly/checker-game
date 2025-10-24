## Creer la classe Joueur

class Joueur: 
    def __init__(self, nom, couleur):
        self._nom = nom
        self._couleur = couleur
        self.score = 0

    @property
    def nom(self):
        return self._nom
    
    @property
    def couleur(self):
        return self._couleur
    
    def getNom(self):
        return self._nom
    
    def getCouleur(self):
        return self._couleur
    
    def addScore(self, points):
        self.score += points