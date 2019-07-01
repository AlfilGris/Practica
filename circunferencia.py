# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:07:32 2019

@author: AlfilGris
"""

print("ingrese los valores de la ecuacion (valores enteros).")
h = int(input("h: "))
k = int(input("k: "))
r = int(input("r: "))

c = 0

for x in range(h-r,h+r):
    for y in range(k-r,k+r):
        if (x-h)**2+(y-k)**2<r**2 :
            c += 1

print("hay {} puntos DENTRO de la circunferencia indicada.".format(c))