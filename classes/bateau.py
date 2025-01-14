# classes/bateau.py
from .vehicule import Vehicule

class Bateau(Vehicule):
    def __init__(self, nbPortes, nbRoues, ancre=False):
        super().__init__(nbPortes, nbRoues)
        self.ancre = ancre

    def demarrer(self):
        if self.ancre:
            print("Il faut d'abord lever l'ancre.")
        else:
            print("Le bateau démarre.")

    def avancer(self):
        print("Le bateau avance.")

    def reculer(self):
        print("Le bateau recule.")

    def descendreAncre(self):
        self.ancre = True
        print("L'ancre est descendue.")

    def monterAncre(self):
        self.ancre = False
        print("L'ancre est montée.")
