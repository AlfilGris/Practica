# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:34:59 2019

@author: AlfilGris
"""

import numpy as np

n = int(input("ingrese el tamaño de la matriz (cuadrada):"))

matriz = []
fila_act = [1]*n


matriz.append(fila_act)

for i in range(1,n):
    fila_act = []
    fila_act.append(1)
    for j in range(1,n):
        fila_act.append(matriz[i-1][j]+fila_act[j-1])
    matriz.append(fila_act)



print(np.matrix(matriz))