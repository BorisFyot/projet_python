#!/usr/bin/env python
# coding: utf-8

liste=[15,28,21,123,54,144,156,255,844,145,1554,844,955,9444,5630,8444,555]
liste.sort()

def switch(l,c):
	a=len(l)
	b=0
	indice=(a+b)//2
	while(l[indice] != c):
		if (l[indice] > c):
			a = indice
		elif (l[indice] < c):
			b = indice
		indice=(a+b)//2
	return indice

ind=switch(liste,9444)
print liste
print ind
print liste[ind]