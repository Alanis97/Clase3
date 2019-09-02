# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:05:00 2019

@author: EAS
"""

def saluda(nombre,simbolo = '+'):
    print(simbolo*42)
    print('Hola',nombre)                           #Se omiten de derecha a izquierda 
    print(simbolo*42)
saluda('Domitila','#')
saluda('Romulo')

def saluda(nombre,mensaje = 'Hola',simbolo = '+'):
    print(simbolo*42)
    print(mensaje, nombre)
    print(simbolo*42)
saluda('Chinpandolfo','Adios','&')



#Ejercicio 3. Funciones 

def nombre(pila, paterno, materno = " ", reves = True):
    if reves == 1:
        print(pila, paterno, materno)
    else:
        print(paterno, materno, pila)
        
nombre('Alex', 'Plosivo')



#Ejercicio 4. Funciones 

def leeEntero(mensaje = "Dato: ", inf = "", sup = ""):
    if inf == "" and sup == "":
        num = int(input(mensaje))
    else:
        if sup == "":
            num = int(input(mensaje)) 
            while num < inf:
                print("\tERROR. Debe ser mayor o igual a", inf)
                num = inf(input(mensaje))
        else:
            num = int(input(mensaje))
            while num < inf or num > sup:
                print("\tERROR. Debe estar entre", inf, "y", sup)
                num = int(input(mensaje))
    return num

"""leeEntero("Edad: ", -1)
articulos = leeEntero("Articulos: ", 1, 20)
leeEntero()
"""

#Ejercicio 5. Funciones 
def leeReal(mensaje = "Dato: ", inf = "", sup = ""):
    if inf == "" and sup == "":
        num = float(input(mensaje))
    else:
        if sup == "":
           num = float(input(mensaje)) 
           while num < inf:
               print("\tERROR. Debe ser mayor o igual a", inf)
               num = inf(input(mensaje))
        else:
            num = float(input(mensaje))
            while num < inf or num > sup:
                print("\tERROR. Debe estar entre", inf, "y", sup)
                num = float(input(mensaje))
    return num

Calificaciones = leeReal("Calificaciones", -1, 10)




            
            
            
            
            
            
            
    