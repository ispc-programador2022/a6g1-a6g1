
#Funcion que retorna el producto de dos parametros

def funProducto(x,y):
    try:
        return x*y
    except:
        print("Debe ingresar valores numericos")




#Funcion que retorna el cociente de dos parametros

def funCociente(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("El segundo parametro debe ser distinto a cero")
    except:
        print("Debe ingresar valores numericos")



