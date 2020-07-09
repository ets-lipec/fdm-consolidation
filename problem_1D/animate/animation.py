import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

class Animation():
    
    def __init__(self,deck,matrix_generation,temperature):
        
        self.deck = deck
        self.matrix_generation = matrix_generation
        self.temperature = temperature
        self.do_color_graph()
        self.do_animation()

    def do_color_graph(self):
        
        x = np.linspace(0,1,2)
        y = np.linspace(-self.matrix_generation.dx,self.matrix_generation.lenX*self.matrix_generation.nlay,self.matrix_generation.nxlay)
        z = np.zeros((len(y),len(x)))
        t = float(self.deck.doc["Animation"]["Time Interval"])
        k = 0
        cmapdeck = self.deck.doc["Animation"]["Color Map"]
        self.index = []
        
        for i in range (len(self.temperature.Ttot[0])-1):
            if abs((i+1)*self.matrix_generation.dt-k*t)>abs(i*self.matrix_generation.dt-k*t):
                plt.clf()                
                z[:,:] = self.temperature.Ttot[:,[i]]
                plt.pcolormesh(x, y, z, vmin=self.matrix_generation.Troom, vmax=self.matrix_generation.Textrusion, cmap=cmapdeck)
                plt.colorbar()
                plt.suptitle('time: {:.2f}'.format(k*t), fontsize=16)
                plt.savefig('./output/temperature' + str("%03d" %k) + '.jpg')
                k = k+1
        plt.clf()                
        z[:,:] = self.temperature.Ttot[:,[len(self.temperature.Ttot[0])-1]]
        plt.pcolormesh(x, y, z, vmin=self.matrix_generation.Troom, vmax=self.matrix_generation.Textrusion, cmap=cmapdeck)
        plt.colorbar()
        plt.suptitle('time: {:.2f}'.format(k*t), fontsize=16)
        plt.savefig('./output/temperature' + str("%03d" %k) + '.jpg')

    def do_animation(self):   
        frames = []
        imgs = glob.glob("./output/*.jpg")
        for i in imgs:
            new_frame = Image.open(i)
            frames.append(new_frame)
            print(i)
           
        # Save into a GIF file that loops forever
        frames[0].save('./output/temperature.gif', format='GIF',
                        append_images=frames[1:],
                        save_all=True,
                        duration=200, loop=0)