# Creer la classe Node


class Node:
    def __init__(self, position, profondeur, dame):
        self._position = position
        self.precedent = None
        self._profondeur = profondeur
        self.dame = dame


    def __eq__(self, other_node):
        if isinstance(other_node, Node):
            return self.get_position() == other_node.get_position()
        return NotImplemented

    @property
    def position(self):
        return self._position
    
    @property
    def profondeur(self):
        return self._profondeur
    
    def get_position(self):
        return self._position
    
    def get_precedent(self):
        return self.precedent
    
    def get_profondeur(self):
        return self._profondeur
    
    def is_dame(self):
        return self.dame
    
    def set_precedent(self, node_precedent):
        self.precedent = node_precedent

    def set_dame(self, dame):
        self.dame = dame
    