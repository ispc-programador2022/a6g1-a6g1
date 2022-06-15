def imprimirAyuda():
    print('1. Funcion ¨Modulo¨, la cual retorna ¨el modulo de 2 parametros¨')
    print('2. Funcion ¨Potencia¨, la cual retorna ¨la potencia de 2 parametros¨')
    

def ing2i():
    try:
        a = int(input("Ingrese un numero: "))
        b = int(input("Ingrese otro numero: "))
        return a, b
    except ValueError:
        print("Por favor ingrese un numero")
        ing2i()
   

def ing2s():
    a = input("Ingrese el primer string: ")
    b = input("Ingrese el segundo string: ")
    return a, b

def presentacion():
    sel= None
    print("Estimado usuario, ¿como se encuentra? Esta es la Consigna 5 ¨Funcion Modulo¨ y 6 ¨Funcion Potencia¨")
    a , b = ing2i()
    while(sel not in range(1,3) and (sel !='f' or sel !='F')): 
        print("Por favor ingrese la operacion deseada")
        sel = input("Numerica (1 o 2) o ¨f¨ para ayuda:  ")
        if(sel == 'f' or sel == 'F'):
            return sel, a, b
        elif (int(sel) in range(1,3)):
            return int(sel), a, b
        else:
            print("Por favor, ingrese una opcion valida")
           

def modulo(a,b):
    return a%b

def potencia(a,b):
    return a**b


def operacion(op):
    if op == 1:
        print(modulo(a, b))
    elif op == 2:
        print(potencia(a, b))
    else:
        print("Operación no disponible")


sel,a,b = presentacion()
while(sel == 'f'):
    imprimirAyuda()
    sel,a,b = presentacion()
else:
    operacion(sel)
    print("Gracias por usarme")
    print("Fin del programa")
    print("\n")