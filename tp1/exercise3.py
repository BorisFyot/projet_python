#!/usr/bin/env python
# coding: utf-8


liste = [13,2,1,5,6,7,8,9,4,55,42,14,5125,1452,14654,544]

while (len(liste) != 3):
	if (len(liste) > 3):
		liste.pop()
	elif (len(liste) < 3):
		liste.append(3)

if len(liste) == 3:
	liste[2]=2

print liste