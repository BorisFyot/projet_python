#!/usr/bin/env python
# coding: utf-8

from compte import Compte 

class Client: # Définition de notre classe Personne
    nombre_client=0


    def __init__(self, nom, prenom,montant=999): # Notre méthode constructeur

        self.nom = nom
        self.prenom = prenom
        self.compte = Compte(montant)
        Client.nombre_client = Client.nombre_client + 1


    def get_info(self):
        print ""
        print "Nom    : ", self.nom
        print "Prenom : ", self.prenom
        print "nombre_client : ", Client.nombre_client
        self.compte.get_info()