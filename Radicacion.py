# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 22:13:46 2022

@author: Damian
"""
def Radicacion(Radicando, Indice):
    """
La funcion Radicacion posee dos argumentos: Un primer argumento que es el radicando y el segundo argumento es el indice.
EJEMPLO
Radicacion(27,3) Esto dara como resultado la raiz cubica de 27 que es igual a 3.
"""
    Raiz = Radicando**(1/Indice)
    if Indice % 2 == 0 and Radicando < 0:
        print("El radicando debe ser mayor a cero en raices con indice par.")
    else:
         return Raiz


#Puse la condicion que el radicando sea mayor a 0 en indices pares para que no de resultados con numeros imaginarios.