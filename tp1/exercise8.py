#!/usr/bin/env python
# coding: utf-8

liste=[15,28,21,123,54,15,144,156,255,844,145,1554,844]


def switch(l,i1=0,i2=-1):
	temp=l[i2]
	l[i2]=l[i1]
	l[i1]=temp
	return l
print liste
print switch(liste)