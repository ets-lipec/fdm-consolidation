import math
import numpy as np
import pdb

class Healing:
    
    def __init__(self, temperature, matrix_generation):
        
        self.temperature = temperature
        self.matrix_generation = matrix_generation
        self.multiple_layers()
        self.time_complete_healing()
        self.time_for_healing()
        
    
    def tw(self,T):
        
        return 2*10**(-5)*math.exp(43000/(8.314*T))
        
    def do_calculation(self,i,j):
        
        Vheal = np.zeros(len(self.temperature.Ttot[0]))
        nxmid = min(i,j)*self.matrix_generation.nx
        ntini = min(i,j)*self.temperature.nt
        
        for k in range (ntini,len(self.temperature.Ttot[0])-1):
            
            tk = (k-ntini)*self.matrix_generation.dt
            tk1 = (k+1-ntini)*self.matrix_generation.dt
            Tav = ((self.temperature.Ttot[nxmid,k+1]+self.temperature.Ttot[nxmid,k])/2)
            Vheal[k+1] = min(1, Vheal[k]+((tk1**(1/4)-tk**(1/4))/self.tw(Tav)**(1/4)))
        
        return Vheal
    
    def do_calculation2(self,i,j):
        
        Vheal = np.zeros(len(self.temperature.Ttot[0]))
        nxmid = min(i,j)*self.matrix_generation.nx
        ntini = min(i,j)*self.temperature.nt
        
        for k in range (ntini,len(self.temperature.Ttot[0])-1):
            
            Tav = ((self.temperature.Ttot[nxmid,k+1]+self.temperature.Ttot[nxmid,k])/2)
            Vheal[k+1] = min(1, (Vheal[k]**4+self.matrix_generation.dt/self.tw(Tav))**(1/4))
        
        
        return Vheal
    
    def do_calculation3(self,i,j):
        
        Vheal = np.zeros(len(self.temperature.Ttot[0]))
        nxmid = min(i,j)*self.matrix_generation.nx
        ntini = min(i,j)*self.temperature.nt
        
        for k in range (ntini,len(self.temperature.Ttot[0])-1):
            
            Vheal[k+1] = min(1, (Vheal[k]**4+(1/(2*self.tw(self.temperature.Ttot[nxmid,k+1]))+1/(2*self.tw(self.temperature.Ttot[nxmid,k])))*self.matrix_generation.dt)**(1/4))
        
        return Vheal

    
    def multiple_layers(self):
        
        self.Mheal = self.do_calculation(1,2)
        for i in range (2,self.matrix_generation.nlay):
            if i==2:
                self.Mheal = np.append([self.Mheal],[self.do_calculation(i,i+1)],axis=0)
            else:
                self.Mheal = np.append(self.Mheal,[self.do_calculation(i,i+1)],axis=0)
        
    def time_complete_healing(self):
        
        self.Thealtot = np.zeros(len(self.Mheal))
        for i in range (len(self.Mheal)):
            k = 0
            for j in self.Mheal[i]:
                if j==1:
                    self.Thealtot[i] = k*self.matrix_generation.dt
                    break
                k = k+1
        
        
    def time_for_healing(self):
        
        self.Tforheal = np.zeros(len(self.Mheal))
        for i in range (len(self.Thealtot)):
            self.Tforheal[i] = self.Thealtot[i]-(i+1)*self.temperature.nt*self.matrix_generation.dt
            