# classes/voiture.py
from .vehicule import Vehicule

class Voiture(Vehicule):
    def __init__(self, nbPortes, nbRoues, freinAMain=False):
        super().__init__(nbPortes, nbRoues)
        self.freinAMain = freinAMain

    def demarrer(self):
        if self.freinAMain:
            print("Il faut d'abord retirer le frein à main.")
        else:
            print("La voiture démarre.")

    def avancer(self):
        print("La voiture avance.")

    def reculer(self):
        print("La voiture recule.")

    def tirerFreinMain(self):
        self.freinAMain = not self.freinAMain
        state = "activé" if self.freinAMain else "désactivé"
        print(f"Le frein à main est {state}.")
