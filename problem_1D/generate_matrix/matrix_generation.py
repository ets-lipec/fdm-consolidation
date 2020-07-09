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



    def Dirichlet(self):
        
        V0 = np.zeros((1,self.nxlay))
        V0[0,0] = 1
        self.M[0,:] = V0

    def Neumann(self):
        
        self.h = float(self.deck.doc["Materials"]["Thermal"]["Heat Transfer Coefficient"] )        
        C2  = 2*self.h*self.dx/self.k
        self.Troom = float(self.deck.doc["Experimental Conditions"]["Room Temperature"] )
        Vnx = np.zeros((1,self.nxlay))
        Vnx[0,self.nxi-2] = 2*self.C1
        Vnx[0,self.nxi-1] = 1-self.C1*(C2+2)
        self.M[self.nxi-1,:] = Vnx
        self.Vamb = np.zeros((self.nxlay,1))
        self.Vamb[self.nxi-1] = self.C1*C2*self.Troom # Ajout du terme constant



    def initialise_vector_temperature(self):
        
        self.Textrusion = float(self.deck.doc["Experimental Conditions"]["Extrusion Temperature"])
        self.T = np.ones((self.nxlay,1))*self.Troom
        self.T[:self.nx+1] = self.Textrusion
        self.Tbed = float(self.deck.doc["Experimental Conditions"]["Bed Temperature"])
        self.T[0] = self.Tbed

    def adjust_vector_temperature(self,vector):
        
        self.T = vector
        self.T[(self.nxi-self.nx):self.nxi] = self.Textrusion
