import numpy as np

class Temperature:
    
    def __init__(self, deck, matrix_generation):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.multiple_layers()
        self.hot_bed()
        self.bed_cooling()
        self.cold_bed()


    def multiple_layers(self):
        
        self.nt = int(float(self.deck.doc["Simulation"]["Time per layer"])/self.matrix_generation.dt)
        for i in range (1,self.matrix_generation.nlay):
            if i == 1:
                self.matrix_generation.do_matrix(i)
                self.matrix_generation.Dirichlet()
                self.matrix_generation.Neumann()
                self.matrix_generation.initialise_vector_temperature()
                self.Ttot = self.matrix_generation.T
            for t in range (self.nt-1):
                self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
                self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)
            
            self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
            self.matrix_generation.do_matrix(i+1)
            self.matrix_generation.Dirichlet()
            self.matrix_generation.Neumann()
            self.matrix_generation.adjust_vector_temperature(self.matrix_generation.T)
            self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)
        
        for t in range (self.nt):
                self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
                self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)


    def hot_bed(self):
        
        self.nt2 = int(float(self.deck.doc["Simulation"]["Time before cooling"])/self.matrix_generation.dt)
        
        self.matrix_generation.Vamb[0]=0
        for t in range (self.nt2):
            self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
            self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)

        
    def bed_cooling(self):
        
        Vcooling = float(self.deck.doc["Simulation"]["Vcooling"])
        timecooling = (self.matrix_generation.Tbed-self.matrix_generation.Troom)/Vcooling
        self.nt1 = int(timecooling/self.matrix_generation.dt)
        
        self.matrix_generation.Vamb[0]=-Vcooling*self.matrix_generation.dt
        for t in range (self.nt1):
            self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
            self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)

    def cold_bed(self):
        
        self.nt3 = int(float(self.deck.doc["Simulation"]["Time after cooling"])/self.matrix_generation.dt)
        
        self.matrix_generation.Vamb[0]=0
        for t in range (self.nt3):
            self.matrix_generation.T = np.dot(self.matrix_generation.M,self.matrix_generation.T)+self.matrix_generation.Vamb
            self.Ttot = np.append(self.Ttot,self.matrix_generation.T,axis=1)
        
        