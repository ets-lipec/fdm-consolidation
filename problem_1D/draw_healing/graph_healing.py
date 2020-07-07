import matplotlib.pyplot as plt

class Graph_Healing:
    
    def __init__(self,healing_calculation,graph_temperature,matrix_generation,solution):
        
        self.healing_calculation = healing_calculation
        self.graph_temperature = graph_temperature
        self.matrix_generation = matrix_generation
        self.solution = solution
        self.do_graph()
        
    def do_graph(self):
        
        fig = plt.figure(figsize=(12,8))
        axes = fig.add_subplot(1,1,1)
        for i in range (1,self.matrix_generation.nlay):
            axes.plot(self.graph_temperature.t[i*self.solution.nt:],self.healing_calculation.Mheal[i-1,i*self.solution.nt:],label='Healing between layers '+str(i)+' and '+str(i+1))
            plt.vlines(self.healing_calculation.Thealtot[i-1],0,1,linestyle='--')
            plt.text(self.healing_calculation.Thealtot[i-1],0,str(self.healing_calculation.Tforheal[i-1])[:6])
        axes.set_xlabel("Time (s)",fontsize=16)
        axes.set_ylabel("Healing",fontsize=16)
        axes.set_title("Evolution of the healing during the time")
        axes.set_xlim((self.graph_temperature.t.min(),self.graph_temperature.t.max()))
        axes.set_ylim((self.healing_calculation.Mheal.min(),self.healing_calculation.Mheal.max()))
        axes.legend(loc='best')
        axes.grid()
        plt.show()