import numpy as np

class Solution:
    
    def _init(self, deck, matrice_generates, initial_conditions, boundary):
        
        self.deck = deck
        self.matrice_generates = matrice_generates
        self.initial_conditions = initial_conditions
        self.boundary = boundary
        self.hot_bed()
        self.bed_cooling()
        self.cold_bed()
    
    def hot_bed(self):
        
        self.nt = int(float(deck.doc["Simulation"]["time"])/matrice_generates.dt)
        self.Ttot = initial_conditions.T
        for t in range (self.nt):
            initial_conditions.T = np.dot(matrice_generates.M,initial_conditions.T)+boundary.Vamb
            self.Ttot = np.append(self.Ttot,initial_conditions.T,axis=1)
    
    def bed_cooling(self):
        
        Vcooling = float(deck.doc["Simulation"]["Vcooling"])
        timecooling = (initial_conditions.Tbed-boundary.Troom)/Vcooling
        self.nt1 = int(timecooling/matrice_generates.dt)
        
        boundary.Vamb[0]=-Vcooling*matrice_generates.dt
        for t in range (self.nt1):
            initial_conditions.T = np.dotmatrice_generates.(M,initial_conditions.T)+boundary.Vamb
            self.Ttot = np.append(self.Ttot,initial_conditions.T,axis=1)
    
    def cold_bed(self):
        self.nt2 = int(float(deck.doc["Simulation"]["time2"])/matrice_generates.dt)
        
        boundary.Vamb[0]=0
        for t in range (self.nt2):
            initial_conditions.T = np.dot(matrice_generates.M,initial_conditions.T)+boundary.Vamb
            self.Ttot = np.append(self.Ttot,initial_conditions.T,axis=1)
        
        