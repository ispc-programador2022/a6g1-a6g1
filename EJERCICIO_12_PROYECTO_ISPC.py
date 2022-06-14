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