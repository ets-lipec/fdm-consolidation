import numpy as np

class Initial_Conditions:
    
    def _init_(self, deck, matrice_generates):
        
        self.deck = deck
        self.matice_generates = matrice_generates
        self.do_vector_temperature()
        
    
    def do_vector_temperature(self):
        
        self.Textrusion = float(deck.doc["Experimental Conditions"]["Extrusion Temperature"])
        self.T = np.ones((matrice_generates.nx,1))*self.Textrusion
        self.Tbed = float(deck.doc["Experimental Conditions"]["Bed Temperature"])
        T[0] = self.Tbed