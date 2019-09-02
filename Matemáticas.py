# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:43:42 2019

@author: hca
"""
import Matemáticas as mat 
import Lectura as lec 

def cuentaDigitos(num):
    c = 0 
    while num > 0:
        c += 1
        num //= 10
    return c


def sumaEnteros(num, func = ""):
    suma = 0
    if func == "":
        for i in range(num + 1):
            suma += 1                          #Suma los primeros num naturales
    else: 
        limite = func(num)
        for n in range(limite):
            suma += num % 10 
            num //= 10
    return suma

#sumaEnteros(2834, cuentaDigitos)

#Raíz digital 

def raizDigital(num):
    raiz = sumaEnteros(num, cuentaDigitos)
    while raiz > 9:
        raiz = sumaEnteros(raiz, cuentaDigitos)
    return raiz
#raizDigital(341997)



"""
Raíz de una función
metodo:
    1. Calculamos: X2 = X0 + X1 / 2
    2. Si abs(f(x)) <= e => f(x) es raiz 
    3 Si no cumple 2:
        3.1 Si f(X0) * F(X) < 0 => X1 = X
            Si no X0 = X
        3.2 Repetir punto 1
"""


def raiz(f, x0, x1, epsilon = 0):
    if (f(x0) * f(x1) > 0):
        x = ""
    else:
        x = (x0 + x1) / 2
        while abs (f(x)) > epsilon:
            if f(x0) * f(x) < 0:
                x1 = x
            else:
                x0 = x
            x = (x0 + x1) / 2 
    return x 

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
   
    
    
    




