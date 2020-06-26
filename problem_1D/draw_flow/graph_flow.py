import numpy as np
import matplotlib.pyplot as plt

class Graph_Flow:
    
    def __init__(self, flow_calculation, graph_temperature):
        
        self.flow_calculation = flow_calculation
        self.graph_temperature = graph_temperature
        self.do_graph()
        
    def do_graph(self):
        
        fig = plt.figure(figsize=(12,8))
        axes = fig.add_subplot(1,1,1)
        axes.plot(self.graph_temperature.t,self.flow_calculation.Mflow[0],label='Conduction')
        axes.plot(self.graph_temperature.t,self.flow_calculation.Mflow[1],label='Convection')
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Flow (W/m²)",fontsize=16)
        axes.set_title("Evolution of the flows during the time")
        axes.set_xlim((self.graph_temperature.t.min(),self.graph_temperature.t.max()))
        axes.set_ylim((self.flow_calculation.Mflow.min(),self.flow_calculation.Mflow.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()