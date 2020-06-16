import numpy as np
import matplotlib.pyplot as plt

class Graph_Deformation():
    
    def _init_(self, matrice_generates, solution, deformation_calculation):
        
        self.deck = deck
        self.matrice_generates = matrice_generates
        self.solution = solution
        self.deformation_calculation = deformation_calculation
        
    def do_graph(self):
        
        self.t = np.linspace(0,solution.nt*matrice_generates.dt,solution.nt)
        fig = plt.figure()
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.t,deformation_calculation.Eps)
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Deformation",fontsize=16)
        axes.set_title("Evolution of the deformation during the time")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((deformation_calculation.Eps.min(),deformation_calculation.Eps.max()))
        axes.grid()
        plt.show()