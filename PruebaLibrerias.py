# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:10:49 2019

@author: hca
"""

import Matemáticas as mate 
import Lectura as lec 

numero = lec.leeEntero("Entero: ", 1)
sumaNaturales = mate.sumaEnteros(numero)
sumaDigitos = mate.sumaEnteros(numero, mate.cuentaDigitos)
raiz = mate.raizDigital(numero)
print("Naturales = {:,d}".format(sumaNaturales))
print("Raiz = ", raiz)