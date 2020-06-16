import numpy as np

class Matrice_Generates:
    
    def __init_(self, deck):
        
        self.deck = deck
        self.do_matrice()
        
    
    def do_matrice(self):
        
        self.lenX = float(deck.doc["Simulation"]["lenX"])
        self.dx =  float(deck.doc["Simulation"]["dx"])             
        self.nx =int(self.lenX/self.dx)
        self.k =  deck.doc["Materials"]["Mechanical"]["Thermal conductivity"]
        self.rho = float(deck.doc["Materials"]["Mechanical"]["Density"])
        self.Cp = float(deck.doc["Materials"]["Thermal"]["Heat Capacity"])
        self.D = self.k/(self.rho*self.Cp)
        self.dt = float(self.rho*self.Cp*self.dx**2/(2*self.k*10))              
        self.C1=self.dt*self.D/self.dx**2
        
        
        self.M = np.zeros((self.nx,self.nx))
        Vsup = Vinf = np.ones((self.nx-1,1))*self.C1
        Vdiag = np.ones((self.nx,1))*(1-2*self.C1)
        np.fill_diagonal(self.M[1:],Vinf)
        np.fill_diagonal(self.M,Vdiag)
        np.fill_diagonal(self.M[:,1:],Vsup)