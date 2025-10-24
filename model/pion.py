## Creer la classe Pion

class Pion:
    def __init__(self, couleur, numero):
        self._couleur = couleur
        self._numero = numero
        self.actif = True
        self.dame = False
    
    @property 
    def couleur(self):
        return self._couleur
    
    @property 
    def numero(self):
        return self._numero
    
    def getCouleur(self):
        return self._couleur
    
    def getNumero(self):
        return self._numero
    
    def isActif(self):
        return self.actif
    
    def isDame(self):
        return self.dame
    
    def setActif(self):
        self.actif = True

    def setInactif(self):
        self.actif = False
    
    def setDame(self):
        self.dame = True
    