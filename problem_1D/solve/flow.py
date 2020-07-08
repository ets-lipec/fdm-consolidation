import numpy as np

class Flow:
    
    def __init__(self, matrix_generation, temperature):
        
        self.matrix_generation = matrix_generation
        self.temperature = temperature
        self.do_calculation()
        
    
    def do_calculation(self):
        
        self.Mflow = [ [self.matrix_generation.k*(self.temperature.Ttot[1,0]-self.temperature.Ttot[0,0])/self.matrix_generation.dx] ,
                       [self.matrix_generation.h*(self.temperature.Ttot[self.matrix_generation.nx,0]-self.matrix_generation.Troom)] ]
        
        
        for i in range (1,self.temperature.nt*self.matrix_generation.nlay):
            
            self.conduction_flow = self.matrix_generation.k*(self.temperature.Ttot[1,i]-self.temperature.Ttot[0,i])/self.matrix_generation.dx
            self.convection_flow = self.matrix_generation.h*(self.temperature.Ttot[int((i-1)/self.temperature.nt+1)*self.matrix_generation.nx,i]-self.matrix_generation.Troom)
            self.Mflow = np.append(self.Mflow,[ [self.conduction_flow] , [self.convection_flow] ],axis=1)
        
        for j in range (self.temperature.nt*self.matrix_generation.nlay,len(self.temperature.Ttot[0])):
            
            self.conduction_flow = self.matrix_generation.k*(self.temperature.Ttot[1,j]-self.temperature.Ttot[0,j])/self.matrix_generation.dx
            self.convection_flow = self.matrix_generation.h*(self.temperature.Ttot[-1,j]-self.matrix_generation.Troom)
            self.Mflow = np.append(self.Mflow,[ [self.conduction_flow] , [self.convection_flow] ],axis=1)
