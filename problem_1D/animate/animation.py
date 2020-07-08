import numpy as np
import matplotlib.pyplot as plt

class Animation():
    
    def __init__(self,deck,matrix_generation,temperature):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.temperature = temperature
        self.do_color_graph()

    def do_color_graph(self):
        
        #t = np.linspace(0,)
        x = np.linspace(0,1,2)
        y = np.linspace(0,self.matrix_generation.lenX*self.matrix_generation.nlay,self.matrix_generation.nxlay)
        z = np.zeros((len(y),len(x)))
        
        for j in range(len(x)):
            z[:,j] = self.temperature.Ttot[:,0]
        plt.pcolormesh(x, y, z, vmin=z.min(), vmax=z.max(), cmap='plasma')
        # plt.contourf(x, y, z, vmin=z.min(), vmax=z.max())
        plt.colorbar()
        plt.show()