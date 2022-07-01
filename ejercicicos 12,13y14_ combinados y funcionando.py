#crear la funcion genrnd que retorna una lista con 50 numeros aleatorios.
from random import randint

def genrnd():
    listado_numeros = [] # crea una lista para almacenar los numeros aleatorios sin repetir.
    contador = 0 # almacena las veces que se agrega un numero a la lista.

    numero_random = randint(1,10000) # genera un numero aleatorio de 1 entre 10000 (en el ejercicio no dice el rango, yo le puse este)

# se repite hasta que el tamaño de la lista no supere a 50
    while contador < 50:
        numero_random = randint(1,10000) # genera un numero aleatorio de 1 entre 10000
        if numero_random in listado_numeros: # verifica si el número aleatorio ya se encuentra en la lista
         pass
        else:
            listado_numeros.append(numero_random) # agrega el número a la lista
            contador+= 1 # suma a cada vuelta
        
    return (listado_numeros)

print(genrnd())

#EJERCICIO 13: FUNCION QUE DEVUELVA LA SUMA DE LAS COMBINACIONES POSIBLES DE LOS NUMEROS GENERADOS POR LA FUNCION GENRND TOMADOS DE A DOS.
from math import factorial
from itertools import combinations, product

#la siguiente funcion con factorial me devuelve la cantidad posible de combinaciones tomados de a par
def suma_comb(n,r):
    el = n - r
    divs = factorial(n) / (factorial(el)* factorial(r))
    return divs

#la siguiente funcion me suma cada par de la lista_combinaciones
def suma_par():
    for i in range(0,len(lista_combinaciones),1):
        print("suma de la combinacion numero:" ,i+1,"->",(lista_combinaciones[i]),"= " , sum(lista_combinaciones[i]))

print("numero de combinaciones posibles tomados de a dos: ",int(suma_comb(50,2)))
#lo siguiente me genera la lista con los valores pares de combinaciones posibles 
lista_combinaciones=(list(combinations(genrnd(), 2)))
#print(lista_combinaciones) (lo comento para que no lo haga ya que solo me pide la suma de los mismos, pero funciona)
suma_par()

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