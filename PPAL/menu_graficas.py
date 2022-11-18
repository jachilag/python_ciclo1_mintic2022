from os import system
from PPAL import graficas as gf

def opcion_n(opcion): #contiene los algoritmos de cada opcion seleccionada de la calculadora
    if opcion == '1':
        gf.grafica_cuadratica()
    elif opcion == '2':
        gf.grafica_cubica()
    elif opcion == '3':
        gf.grafica_raiz()
    elif opcion == '4':
        gf.grafica_seno()
    elif opcion == '0':
        system("cls")
    else:
        print("\nha seleccionado una opcion no valida\n")


def lista_opciones():   #lista para imprimir en pantalla las opciones disponibles en la calculadora
    salida = []
    salida.append("1. funcion cuadratica")
    salida.append("2. fucion cubica")
    salida.append("3. funcion raiz cuadrada")
    salida.append("4. funcion seno")
    salida.append("0. Fin de funciones basicas")
    return salida


def bloque(opcion,opciones,programa4):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    print(f'{opciones[int(opcion)-1]}\n')
    opcion_n(opcion)
    if opcion != '0':
        input("\n\npresione enter para continuar")
        programa4()

def programa4():
    system('cls')
    print('QUE OPERACION DESEA REALIZAR?:\n')
    opciones = lista_opciones()          # trae la lista de las opciones que se mostraran en pantalla
    [print(x) for x in opciones]            #imprime en pantalla las opciones a elegir
    opcion = input('\n')                    #lee la opcion seleccionada por el usuario
    bloque(opcion,opciones,programa4)     #ejecuta el bloque de instrucciones segun la opcion elegida
