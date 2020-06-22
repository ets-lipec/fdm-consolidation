import numpy as np
import matplotlib.pyplot as plt

class Graph_Temperature:
    
    def __init__(self,matrix_generation, boundary_conditions, solution):
        
        self.matrix_generation = matrix_generation
        self.boundary_conditions = boundary_conditions
        self.solution = solution
        self.do_graph()
    
    def do_graph(self):
        
        self.t = np.linspace(0,(self.matrix_generation.nlay*self.solution.nt+self.solution.nt1+self.solution.nt2)*self.matrix_generation.dt,self.matrix_generation.nlay*self.solution.nt+self.solution.nt1+self.solution.nt2+1)
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.t,self.solution.Ttot[0,:],label='Bed')
        for i in range (self.matrix_generation.nlay):
            for j in range (1,self.matrix_generation.nx+1):
                axes.plot(self.t[(i*self.solution.nt+1):],self.solution.Ttot[i*self.matrix_generation.nx+j,(i*self.solution.nt+1):],label='Layer '+str(i+1)+' Point '+str(j))
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Temperature (K)",fontsize=16)
        axes.set_title("Evolution of the temperature of the layers")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.boundary_conditions.Troom,self.solution.Ttot.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        