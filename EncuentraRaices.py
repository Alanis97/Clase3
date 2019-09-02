# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:02:10 2019

@author: ealaniss
"""

import Matemáticas as mat 
import Lectura as lec

def fun1(x):
    return x ** 3 - 2 * x ** 2 +2.25
print("\nf(x) = x ** 3 - 2 * x ** + 2.25")
print("\nIntervalo de evaluación [x0, x1]")
x0 = lec.leeReal("x0: ")
x1 = lec.leeReal("x1: ")
x = mate.raiz(func1, x0, x1)
if (x == "):
    print("No hay cero en ese intervalo") 
else:
    print("\n\tx = {}f(x) = {}".format(x, func1(x)))
enter = input("\n\n\nPresione <enter> para continuar") 
print(10 * "\n")
   
def fun2(x):
    return x ** 2 + 3 * x - 10
print("\nf(x) = x ** 3 - 2 * x ** + 2.25")
print("\nIntervalo de evaluación [x0, x1]")
x0 = lec.leeReal("x0: ")
x1 = lec.leeReal("x1: ")
x = mate.raiz(func1, x0, x1)
if (x == "):
    print("No hay cero en ese intervalo") 
else:
    print("\n\tx = {}f(x) = {}".format(x, func1(x)))
enter = input("\n\n\nPresione <enter> para continuar") 
print(10 * "\n")
   
def func3(x):
    return x ** 3 + x ** 2 - x - 1
print("\nf(x) = x ** 3 - 2 * x ** + 2.25")
print("\nIntervalo de evaluación [x0, x1]")
x0 = lec.leeReal("x0: ")
x1 = lec.leeReal("x1: ")
x = mate.raiz(func1, x0, x1)
if (x == "):
    print("No hay cero en ese intervalo") 
else:
    print("\n\tx = {}f(x) = {}".format(x, func1(x)))
enter = input("\n\n\nPresione <enter> para continuar") 
print(10 * "\n")
   

#Utilizando mis librerias 
""" 
a) lee dos reale (min y max) 
b) en X calcula la raiz de func1
c) Imprime:
    print("x = {}".format(x, func1(x)))
d) Repite a), b) y c) para func2 y func3
    
Datos de prueba:
    func1--(-1,0.5)
    func2---(-8,-2)
    func3---(-2,2)

    
"""
