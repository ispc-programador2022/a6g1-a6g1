def mediarnd():  #La funcion toma los numeros random que genera 
                #la funcion del ejercicio 12 y calcula el promeio o media de los mismos.
          
 numeros= genrnd()       #tomo la función del ejercicio 12 con los números que genere aleatoriamente
  #El promedio se calcula con la suma de los elementos 
  #dividida por la cantidad de los elementos 
  
 promedio = sum(numeros) / len (numeros)   #sum me permite sumar los elementos contenidos en mis lista y
                                          # len me permite obtener la cantidad de elementos de mi lista. 
 return promedio

print(mediarnd())
 