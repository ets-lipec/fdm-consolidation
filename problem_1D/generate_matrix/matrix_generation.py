import numpy as np

class Matrix_Generation:
    
    def __init__(self, deck):
        
        self.deck = deck     
        self.initialise_variables()
    
    def initialise_variables(self):
        
        self.lenX = float(self.deck.doc["Experimental Conditions"]["Layer Thickness"])
        self.nx =  int(self.deck.doc["Simulation"]["Number of intervals per layer"])             
        self.dx = self.lenX/self.nx
        self.k =  float(self.deck.doc["Materials"]["Thermal"]["Thermal Conductivity"])
        self.rho = float(self.deck.doc["Materials"]["Mechanical"]["Density"])
        self.Cp = float(self.deck.doc["Materials"]["Thermal"]["Heat Capacity"])
        self.D = self.k/(self.rho*self.Cp)
        self.dt = float(self.rho*self.Cp*self.dx**2/(2*self.k*10))              
        self.C1=self.dt*self.D/self.dx**2
        self.nlay = int(self.deck.doc["Experimental Conditions"]["Number of Layers"])
    
    def do_matrix(self,i):
        
        self.nxlay = self.nlay*self.nx+1
        self.nxi = i*self.nx+1
        self.M = np.zeros((self.nxlay,self.nxlay))
        Vsup = Vinf = np.zeros((self.nxlay-1,1))
        Vsup[:self.nxi-1] = Vinf[:self.nxi-1] = self.C1
        Vdiag = np.zeros((self.nxlay,1))
        Vdiag[:self.nxi] = (1-2*self.C1)
        np.fill_diagonal(self.M[1:],Vinf)
        np.fill_diagonal(self.M,Vdiag)
        np.fill_diagonal(self.M[:,1:],Vsup)