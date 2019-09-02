# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:11:24 2019

@author: hca
"""

#EJERCICIO 3 FUNCIONES


def nombre(pila,paterno,materno="",reves=True):
    if reves:
        print(pila,paterno,materno)
    else:
        print(materno,paterno,pila)

nombre("Pato","San","God")
nombre("Pato","San",False)
nombre("Pato","San","God")
nombre("Pato","San","God",False)




#EJERCICIO 4 FUNCIONES



def leeEnteros(mensaje="Dato:",inf='',sup=''):
    if inf=='' and sup=='':
        num = int(input(mensaje))
    else:
        if sup == '':
            num = int(input(mensaje))
            while num< inf:
                print("\t ERROR.\tDebe ser mayor o igual a ",inf)
                num = int(input(mensaje))
        else:
            num = int(input(mensaje))
            while num< inf or num>sup:
                print("\t ERROR.\tDebe estar entre ",inf,"y", sup)
                num = int(input(mensaje))
    return num


leeEnteros("Edad:",0)
leeEnteros("Cantidad de articulos: ",1,20)
leeEnteros()




#EJERCICIO 5 FUNCIONES

def leeReales(mensaje="Dato:",inf='',sup=''):
    if inf=='' and sup=='':
        num = float(input(mensaje))
    else:
        if sup == '':
            num = float(input(mensaje))
            while num< inf:
                print("\t ERROR.\tDebe ser mayor o igal a ",inf)
                num = float(input(mensaje))
        else:
            num = float(input(mensaje))
            while num< inf or num>sup:
                print("\t ERROR.\tDebe estar entre ",inf,"y", sup)
                num = float(input(mensaje))
    return num






