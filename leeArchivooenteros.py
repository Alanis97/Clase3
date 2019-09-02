# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:16:02 2019

@author: ealaniss
"""
#Abrir el archivo 
"""
lee = open("datos.txt")     #Se abre para lectura 
lee = open ("datos.txt", "tipo de operación")
tipo de operación:
        r Lectura
        r+ Lectura/Escritura (al final)
        w Sobre escritura. Si no existe el archivo se crea
        a Añadir. Escribe al final del archivo 
"""
#Cerrar
"lee.close()"

#Leer el archivo 
"""readline(): en cada lectura lee una linea creando un string 
readlines(): Lee todo el archivo y crea una lista de strings 
read() : Lee todo el archivo creando un string de todo, separando las lineas por \n 

Fin de archivo 
    linea = lee.readline()
    while linea:
        .
        .
        .
        linea = lee.readline()
        
    Se puede utilizar un for-each:
        for linea in lee:
            print(linea)
"""



#Ejercicio 1. ARCHIVOS

n = 0 #cantidad de enteros leidos
impares = 0 #cantidad y porcentaje de impares 
lee = open("enteros.txt", "r") #abre el archivo de nombre físico enteros.txt y lógico lee

numero = lee.readline()
while numero:
    n += 1
    if int(numero) % 2 == 1:
        impares += 1
    numero = lee.readline()
lee.close()
if n > 0:
    impares = impares * 100 / n 
    print("Hay {:.3f}% de impares en {:,d} enteros".format(impares, n))
else: 
    print("El archivo está vacio") 


#Crear un archivo
    
"""
w => esc = open("resultados.txt", "w")
a) write()
    El argumento debe de ser un string 
    Para cambiar de linea se debe de especificar con \n
b) writelines()
    Escribe una lista completa 
    Todo en una sola linea y juntando los elementos 
"""

#Ejercicio 2. Archivos 



