def multirnd():
   # Esta funcion toma una lista de numeros random que genera 
   # la funcion del ejercicio 12 y multiplicada cada numero
   # menos el ultimo por el siguiente.
   
   lista= genrnd()                           # pide a genrand (ej 12) que genere una lista y la guarda
   
   # debug : ver la lista que devuelve genrnd()
   # print lista
   
   resultado = []                            # lista vacia para guardar el resultado de esta funcion

   for i in lista[:-1]:                      # por cada item de lista, menos el ultimo
          
           m = i *  lista[lista.index(i)+1]  # multiplicarlo por el siguiente
           resultado.append(m)               # agregarlo a la lista resultado

            # control debug, descomentar en caso de usarlo
            # print (lista)
            # print (i, lista[lista.index(i)+1] )
            # print(i)  
            # print (resultado)  

   return  (resultado)
   
print(multirnd())

# Variacion: 

# si hay que usar combinatoria de elementos, 
# el paso previo seria armar la lista de combinaciones, y luego aplicar la f anterior


# from itertools import combinations

# A = genrnd()
# temp = combinations(A, 2)      # todas las combinaciones de la lista tomadas de a 2 numeros
# result = []
# for i in list(temp):
#	print (i)
#	result.append(i) 

# print (result, len(result))    # sobre esta lista, multiplicar cada par. (1225 items)

