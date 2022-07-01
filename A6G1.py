#Esta aplicación debe llamar a funciones, cada una en su archivo .py a saber:
#función que muestre cartel de presentación.
#función ing2i, debe permitir el ingreso de 2 valores enteros
#función ing2s, debe permitir el ingreso de 2 valores string

def saludo():
    print("""
     _________________________________
    |   __ __  _____  _____   _____   |
    |     |   |      |     | |        |
    |     |   |____  |_____| |        |
    |     |        | |       |        |
    |   __|__ _____| |       |_____   |
    |_________________________________|

    Bienvenidos a nuestro Proyecto n° 1
    
    Aula 6 Grupo 1

    Integrantes:

    Juan Carlos	Güento
    Carlos Andres Gomez
    Juan Pablo Godoy Grosso
    Juan Ezequiel Gomez
    Cinthya yael Gomez
    Monserrat Gutierrrez
    Juan Diego Gonzalez Antoniazzi
    Damian Galello
    Federico Gabriel Gonzalez 
    Camila Micaela Gil Borel
    Maria Nazareth Giménez
    Adrian Alejandro Garcia
    Héctor Daniel gomez
    María Emilia Garmendia
    Laura Gomez
    Carlos Gimenez
    Georgina Gaspar

    
    
    """)

def IngresoDeNumeros(a=0,b=0):
    try:
        a=int(input("Ingrese un valor entero para num1 "))
        b=int(input("Ingrese un valor entero para num2 "))
        return a,b
    except:
        print("Solo puede ingresar valores numericos.")
        IngresoDeNumeros(a=0,b=0)
    

def IngresoDeStrings(a="",b=""):
    try:
        a=input("Ingrese un valor string para 'a' ")
        b=input("Ingrese un valor string para 'b' ")
        return a,b
    except:
        print("Solo puede ingresar strings.")
        IngresoDeStrings(a="",b="")
        

    


saludo()

IngresoDeNumeros()
IngresoDeStrings()


