from Problem import *
import os, sys
import glob
import matplotlib.pyplot as plt
import pdb
from PIL import Image

cwd = os.getcwd()

print(cwd)
deck = Deck(cwd + "/deck.yaml")

matrice_generates = Matrice_Generates(deck)

boundary = Boundary(deck,matrice_generates)

initial_conditions = initial_conditions(deck, matrice_generates)

solution = Solution(deck, matrice_generates, boundary, initial_conditions)

graph_temperature = Graph_Temperature(matrice_generates,solution)

deformation_calculation = Deformation_Calculation(deck, initial_conditions, solution)

# graph_deformation = Graph_Deformation(matrice_generates, solution, deformation_calculation)

bed_cooling = Bed_Cooling()