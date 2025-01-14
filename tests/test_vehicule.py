# tests/test_vehicule.py
import pytest
from classes.voiture import Voiture
from classes.bateau import Bateau
from classes.avion import Avion

def test_voiture():
    v = Voiture(4, 4)
    v.demarrer()  # Test démarrage sans frein à main
    v.avancer()
    v.reculer()
    v.tirerFreinMain()  # Tester l'activation du frein à main
    v.demarrer()  # Tester démarrage avec frein à main activé
    v.tirerFreinMain()  # Tester la désactivation du frein à main

def test_bateau():
    b = Bateau(0, 0)
    b.demarrer()  # Test démarrage avec ancre descendue
    b.avancer()
    b.reculer()
    b.descendreAncre()  # Tester la descente de l'ancre
    b.monterAncre()  # Tester la montée de l'ancre
    b.demarrer()  # Tester démarrage avec ancre levée

def test_avion():
    a = Avion(2, 3)
    a.demarrer()
    a.avancer()
    a.reculer()
