# Exercice - Héritage sur des véhicules

## Énoncé :

Dans cet exercice, vous allez créer une hiérarchie de classes représentant différents types de véhicules : une classe générale `Vehicule`, et des classes filles `Voiture`, `Bateau`, et `Avion`.

### 1. Classe `Vehicule` :

La classe `Vehicule` devra avoir les attributs suivants :
- `nbPortes`: le nombre de portes
- `nbRoues`: le nombre de roues

Elle devra aussi implémenter les méthodes suivantes :
- `demarrer()`
- `avancer()`
- `reculer()`
- `tournerDroite()`
- `tournerGauche()`

### 2. Classe `Voiture` :

La classe `Voiture` hérite de `Vehicule` et ajoute l'attribut :
- `freinAMain`: un booléen indiquant si le frein à main est activé ou non.

Elle devra redéfinir les méthodes :
- `demarrer()`
- `avancer()`
- `reculer()`
- `tirerFreinMain()`

### 3. Classe `Bateau` :

La classe `Bateau` hérite de `Vehicule` et ajoute l'attribut :
- `ancre`: un booléen indiquant si l'ancre est levée ou abaissée.

Elle devra redéfinir les méthodes :
- `demarrer()`
- `avancer()`
- `reculer()`
- `descendreAncre()`
- `monterAncre()`

### 4. Classe `Avion` :

La classe `Avion` hérite de `Vehicule` et n'a pas d'attributs spécifiques. Elle devra redéfinir les méthodes :
- `demarrer()`
- `avancer()`
- `reculer()`

### But :

L'objectif est de bien comprendre l'héritage entre classes et la redéfinition de méthodes. Implémentez toutes les classes et les méthodes avec des comportements appropriés.

## Tests :

Des tests unitaires sont fournis dans le fichier `tests/test_vehicule.py`. Assurez-vous que vos classes passent ces tests avant de soumettre votre travail.
