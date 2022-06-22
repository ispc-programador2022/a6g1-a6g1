#14: FUNCION QUE DEVUELVA EL PRODUCTO DE LAS COMBINACIONES POSIBLES DE LOS NUMEROS GENERADOS POR LA FUNCION GENRND TOMADOS DE A DOS
from math import factorial
from itertools import combinations

#la siguiente funcion con factorial me devuelve la cantidad posible de combinaciones tomados de a par
def producto_comb(n,r):
    el = n - r
    divs = factorial(n) / (factorial(el)* factorial(r))
    return divs
 
#la siguiente funcion realiza el producto de cada par de la lista_combinaciones(la cual en cada pasada la transformo en  una tupla para poder multiplicar sus componentes)
def producto_par():
     for i in range(0,len(lista_combinaciones),1):
         tupla_numeros = (lista_combinaciones[i])     
         producto = (tupla_numeros[0] * tupla_numeros[1])
         print("producto de la combinacion numero:" ,i+1,"->",(lista_combinaciones[i]),"= " , producto )
        
print("numero de combinaciones posibles tomados de a dos: ",int(producto_comb(50,2)))
#lo siguiente me genera la lista con los valores pares de combinaciones posibles 
lista_combinaciones=(list(combinations(genrnd(), 2)))
#print(lista_combinaciones) (lo comento para que no lo haga ya que solo me pide la suma de los mismos, pero funciona)
producto_par()