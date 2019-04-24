#!/usr/bin/env python
# coding: utf-8

choix=0
while choix == 0:
	A = raw_input("factoriel de : ")
	try:
		chiffre = int(A)
		choix=1
	except ValueError:
		print "il ne s'agit pas d'un chiffre, merci de saisir un chiffre"

def factoriel(c):
	if (c > 1):
		c = c * factoriel(c-1)
		return c
	elif (c == 1):
		return 1

print factoriel(chiffre)