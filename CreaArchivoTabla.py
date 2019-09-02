# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:51:12 2019

@author: ealaniss
"""
import Lectura as lec
limite = lec.leeEntero("Límite de la tabla: ", 1, 50)
esc = open("tabla.txt", "w") #Abre el archivo físico tablatxt con el archivo lógico esc para ser re escrito 

esc.write(15 * " " + "TABLA DE CUADRADOS Y CUBOS".center(30))
esc.write("\n\n")
esc.write("n".rjust(15) + "n^2".rjust(15) + "n^3".rjust(15))
esc.write("\n\n")
for num in range(1, limite +1):
    esc.write(str(num).rjust(15) + str(num **2).rjust(15) + str(num ** 3).rjust(15) + "\n")
esc.close()



































