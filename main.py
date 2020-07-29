from problem_1D import *


cwd = os.getcwd()

deck = Deck(cwd + "/deck.yaml")

matrix_generation = Matrix_Generation(deck)

temperature = Temperature(deck, matrix_generation)

flow = Flow(matrix_generation, temperature)

healing = Healing(temperature, matrix_generation)

graph = Graph(matrix_generation, temperature, flow, healing)

animation = Animation(deck, matrix_generation, temperature)

stability = Stability(matrix_generation, temperature)

#deformation_calculation = Deformation_Calculation(deck, matrix_generation, initial_conditions, solution)

#graph_deformation = Graph_Deformation(matrix_generation, solution, deformation_calculation)