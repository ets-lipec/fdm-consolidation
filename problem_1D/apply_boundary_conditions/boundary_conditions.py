import numpy as np



class Boundary_Conditions:

    def __init__(self, deck, matrix_generation):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        
    def Dirichlet(self):
        
        V0 = np.zeros((1,self.matrix_generation.nxlay))
        V0[0,0] = 1
        self.matrix_generation.M[0,:] = V0
        
        
    def Neumann(self):
        
        h = float(self.deck.doc["Materials"]["Thermal"]["Heat Transfer Coefficient"] )        
        C2  = 2*h*self.matrix_generation.dx/self.matrix_generation.k
        self.Troom = float(self.deck.doc["Experimental Conditions"]["Room Temperature"] )
        Vnx = np.zeros((1,self.matrix_generation.nxlay))
        Vnx[0,self.matrix_generation.nxi-2] = 2*self.matrix_generation.C1
        Vnx[0,self.matrix_generation.nxi-1] = 1-self.matrix_generation.C1*(C2+2)
        self.matrix_generation.M[self.matrix_generation.nxi-1,:] = Vnx
        self.Vamb = np.zeros((self.matrix_generation.nxlay,1))
        self.Vamb[self.matrix_generation.nxi-1] = self.matrix_generation.C1*C2*self.Troom # Ajout du terme constant