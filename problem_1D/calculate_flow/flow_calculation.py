import numpy as np

class Flow_Calculation:
    
    def __init__(self, matrix_generation, boundary_conditions, solution):
        
        self.matrix_generation = matrix_generation
        self.boundary_conditions = boundary_conditions
        self.solution = solution
        self.do_calculation()
        
    
    def do_calculation(self):
        
        self.Mflow = [ [self.matrix_generation.k*(self.solution.Ttot[1,0]-self.solution.Ttot[0,0])/self.matrix_generation.dx] ,
                       [self.boundary_conditions.h*(self.solution.Ttot[self.matrix_generation.nx,0]-self.boundary_conditions.Troom)] ]
        
        
        for i in range (1,self.solution.nt*self.matrix_generation.nlay):
            
            self.conduction_flow = self.matrix_generation.k*(self.solution.Ttot[1,i]-self.solution.Ttot[0,i])/self.matrix_generation.dx
            self.convection_flow = self.boundary_conditions.h*(self.solution.Ttot[int((i-1)/self.solution.nt+1)*self.matrix_generation.nx,i]-self.boundary_conditions.Troom)
            self.Mflow = np.append(self.Mflow,[ [self.conduction_flow] , [self.convection_flow] ],axis=1)
        
        for j in range (self.solution.nt*self.matrix_generation.nlay,len(self.solution.Ttot[0])):
            
            self.conduction_flow = self.matrix_generation.k*(self.solution.Ttot[1,j]-self.solution.Ttot[0,j])/self.matrix_generation.dx
            self.convection_flow = self.boundary_conditions.h*(self.solution.Ttot[-1,j]-self.boundary_conditions.Troom)
            self.Mflow = np.append(self.Mflow,[ [self.conduction_flow] , [self.convection_flow] ],axis=1)
