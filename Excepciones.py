# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:03:12 2019

@author: hca
"""
import math 

x = int(input("Entero: "))

"""
NameError: no encuentra un nobre local o global
ValueError: argumento de funciontiene el tipo correcto pero un valor inapropiado
TypeError: parametro actual es del tipo inapropiado o con un operador 
ZeroDivisionError: segundo argumento de una division o modulo es cero
FileNotFoundError: el archivo o diccionario no existe
"""
n = 5
try:
    fact = math.factorial(n)
    print("Factorial: ", fact)
except:
    print("\tERROR. Argumento incorrecto")

n = -5
try:
    fact = math.factorial(n)
    print("Factorial: ", fact)
except ValueError:
    print("\tERROR. Argumento incorrecto")
    
n = 5
try:
    fact = math.factorial(n)
    print("Factorial: ", f)
except (ValueError, NameError):
    print("\tERROR. Argumento incorrecto")
    
#Mnesajes adecuados

n = 5
try:
    fact = math.factorial(n)
    print("Factorial: ", g)
except ValueError:
    print("\tERROR. Argumento incorrecto")
except NameError:
    print("\tERROR. Argumento incorrecto")
    
    
n = 5
try:
    fact = math.factorial(n)
except ValueError:
    print("\tERROR. Argumento incorrecto")
except NameError:
    print("\tERROR. Argumento incorrecto")
else:
    print("Factorial: ", fact)
finally:
    print("Fin del proceso")
    
"""
try:
    except < >:
    except < >:
        .
        .
        .
    else:
"""

numero = -5 
try:
    fact = math.factorial(numero)
except ValueError as problema:
    print("\tERROR.",problema)
except NameError as problema:
    print("\tERROR.", problema)
else:
    print("\tFactorial: ", fact)
finally:
    print("\tFin del proceso")
    
    
    
    
    
#Raiz de una ecuacion

    
    











            
    