# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:08:56 2019

@author: hca
"""

def leeEntero(mensaje = "Dato: ", inf = "", sup = ""):
    num = 0
    if inf == "" and sup == "":
        try:
            num = int(input(mensaje))
        except:
            print("\tERROR. Proporcione un número entero")
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


