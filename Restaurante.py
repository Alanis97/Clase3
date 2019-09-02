# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:06:53 2019

@author: hca
"""



def leeN():
    n = int(input("Consumiciones: "))
    while n < 1:
        print("\tERROR. Debe ser mayor a 0")
        n = int(input("Consumiciones: "))
    return n 

def leeMonto(num):
    monto = float(input("Monto {:,d}: $".format(num)))
    while monto <= 0:
         print("\tERROR. Debe ser mayor a 0")
         monto = float(input("Monto {:,d}: $".format(num)))
    return monto

def calculaDescuento(monto):
    if monto <= 100:
        desc = 10
    else:
        if monto <= 200:
            desc = 15.50
        else:
            desc = 22.35
    return monto * desc / 100


def calcularIva(iva,monto):
    return monto * iva / 100
print(calcularIva(10,500))

def Imprime(monto):
    desc = calculaDescuento(monto)
    iva = calcularIva(16, monto - desc)
    print("${:,.2f}\t${:,.2f}\t${:,.2f}\t${:,.2f}\t${:,.2f}".format(monto, desc, monto - desc, iva, monto-desc+iva))
Imprime(-9000)

#Programa principal 
n = leeN()
for i in range(n):
    Imprime(leeMonto( i + 1))


a=6
b=7.5
c=True

x=int(b)
y=float(a)
z=str(c)


print(x)
print(y)
print(z)

w=bool(a)
wl=bool(0)
print(w)
print(wl)


t=int(w)
print(t)

del a


#%reset
#borra todo(solo se puede desde la consola)


#clear()  
#Borra la consola





#
#
# IMPRESION CON FORMATO
#
#

sueldo=245678935.47892
articulos=97871


#Sueldos
#f para reales
# , para separar en tres con 
#el 20 separa respecto a la derecha
#si quisiera a la izquierda usaría -

print("sueldo= {:20.1f}".format(sueldo))
print("sueldo= ${:,.2f}".format(sueldo))

#Enteros
#d para enteros
print("Cantidad= {:,d}".format(articulos))

#cambio de linea
#\n


#tabulador
#\t

print("aguazota\t azul")

#varias variables

print("Sueldo =${:,.2f}\tImpuesto = ${:.2f}\n".format(sueldo,234.56))

#caracteres especiales

print("\t\t\"RESULTADOS\"")

#mismo renglon, diferente print
print("Sueldo =${:,.2f}".format(sueldo),end="")
print("\tImpuesto =${:.2f}\n".format(234.56))






#EJERCICIO 22 REPASO


def leerN():
    n = int(input("¿Cuántos montos son?"))
    while n<=0:
        print("ERROR. \nSolo montos positivos mayores a cero por favor")
        n = int(input("¿Cuántos montos son?"))
    return(n)

"""

#parametros por omision

#Se ommiten de derecha a izquuierda

def saluda(nombre, simbolo='+'):
    print(simbolo*42)
    print("Hola",nombre)
    print(simbolo*42)
    
def saludaPro(nombre,mensaje='Hola',simbolo='+'):
    print(simbolo*42)
    print(mensaje,nombre)
    print(simbolo*42)
    
    
saluda("Pato","#")
       
       
saluda("Pato")

saludaPro("Pepe","Adios","&")
saludaPro("Pepe","Adios")  
saludaPro("Pepe")        