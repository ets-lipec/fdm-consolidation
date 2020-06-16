import numpy as np
import matplotlib.pyplot as plt

class Graph_Temperature:
    
    def _init_(self,matrice_generates,solution):
        
        self.matrice_generates = matrice_generates
        self.solution = solution
        self.do_graph()
    
    def do_graph(self):
        self.t = np.linspace(0,(solution.nt+solutions.nt1+solution.nt2)*matrice_generates.dt,solution.nt+solutions.nt1+solution.nt2+1)
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        for i in range (matrice_generates.nx):
            axes.plot(self.t,solution.Ttot[i,:],label='Layer'+str(i+1))
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Temperature (K)",fontsize=16)
        axes.set_title("Evolution of the temperature of the layers")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((solution.Ttot.min(),solution.Ttot.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        