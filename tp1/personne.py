#!/usr/bin/env python
# coding: utf-8

class Personne: # Définition de notre classe Personne

    """Classe définissant une personne caractérisée par :

    - son nom

    - son prénom

    - son âge

    - son lieu de résidence"""


    def __init__(self, nom, prenom): # Notre méthode constructeur

        """Pour l'instant, on ne va définir qu'un seul attribut"""

        self.nom = nom
        self.prenom = prenom