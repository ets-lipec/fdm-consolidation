import numpy as np
import matplotlib.pyplot as plt

class Stability:
    
    def __init__(self,matrix_generation,temperature):
        
        self.matrix_generation = matrix_generation
        self.temperature = temperature
        self.do_stability_graph()
        
    def choose_dt(self):
        
        l = np.array([self.matrix_generation.dt])
        self.ncurves = 3
        for i in range (self.ncurves):
            l = np.insert(l,0,l[0]/2)
            l = np.append(l,l[-1]*2)
        return l
    
    def temperature_dt(self,dt):
        
        self.matrix_generation.dt = dt
        self.matrix_generation.C1 = dt*self.matrix_generation.D/self.matrix_generation.dx**2
        print(self.matrix_generation.dt)
        self.temperature.multiple_layers()
        self.temperature.hot_bed()
        self.temperature.bed_cooling()
        self.temperature.cold_bed()
        
    def graph_dt(self,axes,k):
        
        color = np.linspace(0,plt.cm.jet.N,2*self.ncurves+1,dtype=int)
        palette = plt.cm.brg(X=color)
        self.t = np.linspace(0,(self.matrix_generation.nlay*self.temperature.nt+self.temperature.nt1+self.temperature.nt2+self.temperature.nt3)*self.matrix_generation.dt,self.matrix_generation.nlay*self.temperature.nt+self.temperature.nt1+self.temperature.nt2+self.temperature.nt3+1)
        axes.plot(self.t,self.temperature.Ttot[2,:]+2*k,color=palette[k],alpha=1-k/(2*self.ncurves+1),label='dt = '+str(self.matrix_generation.dt)[:6]+' s' )
        
    def do_stability_graph(self):
        
        l = self.choose_dt()
        fig = plt.figure(figsize=(12,6))
        axes = fig.add_subplot(1,1,1)
        k = 0
        for i in l:
            self.temperature_dt(i)
            self.graph_dt(axes,k)
            k = k+1
            print(k)
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Temperature (K)",fontsize=16)
        axes.set_title("Evolution of the temperature for different dt")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.matrix_generation.Troom,self.matrix_generation.Textrusion))
        axes.legend(loc='best')
        axes.grid()
        plt.show()