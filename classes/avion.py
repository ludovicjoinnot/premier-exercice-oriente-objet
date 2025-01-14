# classes/avion.py
from .vehicule import Vehicule

class Avion(Vehicule):
    def __init__(self, nbPortes, nbRoues):
        super().__init__(nbPortes, nbRoues)

    def demarrer(self):
        print("L'avion démarre.")

    def avancer(self):
        print("L'avion avance.")

    def reculer(self):
        print("L'avion recule.")
