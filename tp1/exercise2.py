#!/usr/bin/env python
# coding: utf-8
choix=0
boucle=0
while choix == 0:
	A = raw_input("Etes vous heureux? ")
	bonheur = A
	choix=1
	if (bonheur == "Oui"):
		print "Partage ton bonheur avec les autres"
	elif (bonheur == "Non"):
		while boucle == 0:
			B = raw_input("Cela me convient il ? ")
			convient = B
			boucle=1
			if (convient == "Oui" and bonheur == "Non"):
				print "On y peut rien"
			elif (convient == "Non" and bonheur == "Non"):
				print "Cherche une personne heureuse, c'est contagieux!"
			else: 
				print "Oui ou Non"
				boucle=0
	else:
		print "Oui ou Non"
		choix=0