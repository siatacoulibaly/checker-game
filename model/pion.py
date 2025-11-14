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
    
    def get_couleur(self):
        return self._couleur
    
    def get_numero(self):
        return self._numero
    
    def is_actif(self):
        return self.actif
    
    def is_dame(self):
        return self.dame
    
    def set_actif(self):
        self.actif = True

    def set_inactif(self):
        self.actif = False
    
    def set_dame(self):
        self.dame = True
    