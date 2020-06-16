class Deformation_Calculation():
    
    def _init_(self, deck, initial_conditions, solution):
        
        self.deck = deck
        self.initial_conditions = initial_conditions
        self.solution = solution
        
    def do_calculation(self):
        
        Tmoy = (solution.Ttot[0,:]+2*solution.Ttot[1,:]+2*solution.Ttot[2,:]+2*solution.Ttot[3,:]+solution.Ttot[4,:])/8 #Température moyenne par la méthode des trapèzes 
        self.Eps = float(deck.doc["Materials"]["Mechanical"]["Coefficient of Thermal Expansion"])*(Tmoy-initial_conditions.Textrusion)