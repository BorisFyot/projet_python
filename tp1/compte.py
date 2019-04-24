#!/usr/bin/env python
# coding: utf-8

class Compte: # Définition de notre classe Personne
    nombre_compte=0
    numero=1


    def __init__(self, montant): # Notre méthode constructeur
        self.numero = Compte.numero
        self.montant = montant
        Compte.nombre_compte = Compte.nombre_compte + 1
        Compte.numero = Compte.numero + 1

    def get_info(self):
        print "Compte : ", self.numero
        print "montant : ", self.montant
        print "nombre_compte : ", Compte.nombre_compte
        print "numero_compte : ", Compte.numero