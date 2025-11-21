## Creer la classe Damier
import pion

class Damier:
    def __init__(self):
        self.init = False
        self._grille = self.init_grille()

    @property
    def grille(self):
        return self._grille
    
    def init_grille(self):
        if self.init == True:
            return
        # Initialiser les pions
        for ligne in range(10):
            for colonne in range(10):
                if (ligne < 4 and (ligne + colonne) % 2 != 0):
                    self._grille[(ligne, colonne)] = pion.Pion("noir", f"{ligne}{colonne}")
                elif(ligne > 5 and (ligne + colonne) % 2 != 0):
                    self._grille[(ligne, colonne)] = pion.Pion("blanc", f"{ligne}{colonne}")
                elif((ligne + colonne) % 2 != 0):
                    self._grille[(ligne, colonne)] = None
                else:
                    self._grille[(ligne, colonne)] = "NA"
        self.init = True
    

    def get_item(self, position):
        try:
            return self.grille[position]
        except: 
            return "NA"


    def move_pion(self, position_a, position_b):
        if self.get_item(position_b) == None and isinstance(self.get_item, pion.Pion):
            self.grille[position_b] = self.get_item(position_a)
            self.grille[position_a] = None
            return True
        return False
    
    def out_pion(self, position):
        if isinstance(self.get_item(position), pion.Pion):
            self.grille[position] = None
            return True
        return False
    