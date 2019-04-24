#!/usr/bin/env python
# coding: utf-8


liste = [1,1]

choix=0
while choix == 0:
	A = raw_input("Indiquer le nombre de boucle : ")
	try:
		nb = int(A)
		choix=1
	except ValueError:
		print "il ne s'agit pas d'un chiffre, merci de saisir un chiffre"

def ajout(liste2):
	liste2.append(liste2[-1] + liste2[-2])
	return liste2

while nb > 0:
	liste=ajout(liste)
	nb=(nb-1)

print liste