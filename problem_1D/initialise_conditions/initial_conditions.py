import numpy as np

class Initial_Conditions:
    
    def __init__(self, deck, matrix_generation):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
    
    def initialise_vector_temperature(self):
        
        self.Textrusion = float(self.deck.doc["Experimental Conditions"]["Extrusion Temperature"])
        self.T = np.zeros((self.matrix_generation.nxlay,1))
        self.T[:self.matrix_generation.nx+1] = self.Textrusion
        self.Tbed = float(self.deck.doc["Experimental Conditions"]["Bed Temperature"])
        self.T[0] = self.Tbed
        
    def adjust_vector_temperature(self,vector):
        
        self.T = vector
        self.T[(self.matrix_generation.nxi-self.matrix_generation.nx):self.matrix_generation.nxi] = self.Textrusion
        