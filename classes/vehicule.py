# classes/vehicule.py

class Vehicule:
    def __init__(self, nbPortes, nbRoues):
        self.nbPortes = nbPortes
        self.nbRoues = nbRoues

    def demarrer(self):
        print(f"Le véhicule démarre.")

    def avancer(self):
        print("Le véhicule avance.")

    def reculer(self):
        print("Le véhicule recule.")

    def tournerDroite(self):
        print("Le véhicule tourne à droite.")

    def tournerGauche(self):
        print("Le véhicule tourne à gauche.")
