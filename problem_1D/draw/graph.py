import numpy as np
import matplotlib.pyplot as plt


class Graph:
    
    def __init__(self, matrix_generation, temperature, flow, healing):
        
        self.matrix_generation = matrix_generation
        self.temperature = temperature
        self.flow = flow
        self.healing = healing
        self.do_temperature_graph()
        self.do_flow_graph()
        self.do_healing_graph()
    
    def do_temperature_graph(self):
        
        self.t = np.linspace(0,(self.matrix_generation.nlay*self.temperature.nt+self.temperature.nt1+self.temperature.nt2+self.temperature.nt3)*self.matrix_generation.dt,self.matrix_generation.nlay*self.temperature.nt+self.temperature.nt1+self.temperature.nt2+self.temperature.nt3+1)
        fig = plt.figure(figsize=(12,6))
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.t,self.temperature.Ttot[0,:],label='Bed')
        for i in range (self.matrix_generation.nlay):
            for j in range (1,self.matrix_generation.nx+1):
                axes.plot(self.t[(i*self.temperature.nt):],self.temperature.Ttot[i*self.matrix_generation.nx+j,(i*self.temperature.nt):],label='Layer '+str(i+1)+' Point '+str(j))
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Temperature (K)",fontsize=16)
        axes.set_title("Evolution of the temperature of the layers")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.matrix_generation.Troom,self.temperature.Ttot.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()



    def do_flow_graph(self):
        
        fig = plt.figure(figsize=(12,8))
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.t,self.flow.Mflow[0],label='Conduction')
        axes.plot(self.t,self.flow.Mflow[1],label='Convection')
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Flow (W/m²)",fontsize=16)
        axes.set_title("Evolution of the flows during the time")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.flow.Mflow.min(),self.flow.Mflow.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()



    def do_healing_graph(self):
        
        fig = plt.figure(figsize=(12,8))
        axes = fig.add_subplot(1,1,1)
        for i in range (1,self.matrix_generation.nlay):
            axes.plot(self.t[i*self.temperature.nt:],self.healing.Mheal[i-1,i*self.temperature.nt:],label='Healing between layers '+str(i)+' and '+str(i+1))
            plt.vlines(self.healing.Thealtot[i-1],0,1,linestyle='--')
            plt.text(self.healing.Thealtot[i-1],0,str(self.healing.Tforheal[i-1])[:6])
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Healing",fontsize=16)
        axes.set_title("Evolution of the healing during the time")
        axes.set_xlim((self.t.min(),self.t.max()))
        axes.set_ylim((self.healing.Mheal.min(),self.healing.Mheal.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()


