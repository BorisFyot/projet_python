#!/usr/bin/env python
# coding: utf-8
#	Boucle pour la saisie de la premiere valeur
#	Verification si il s'agit bien d'un numerique
choix=0
while choix == 0:
	A = raw_input("Indiquer la valeur de : A ")
	try:
		val1 = float(A)
		choix=1
	except ValueError:
		print "il ne s'agit pas d'un chiffre, merci de saisir un chiffre"
	
#	Boucle pour la saisie de la deuxieme valeur
#	Verification si il s agit bien d'un numérique
choix=0
while choix == 0:
	B = raw_input("Indiquer la valeur de : B ")
	try:
		val2 = float(B)
		choix=1
	except ValueError:
		print "il ne s'agit pas d'un chiffre, merci de saisir un chiffre"
		
#Valeur1² + Valeur2² = Valeur3
val3=val1**2+val2**2;

#Affichage
print val1,"**2 +",val2,"**2 = ",val3