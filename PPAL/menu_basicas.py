from os import system
from PPAL import Matematicas as mt

def opcion_n(opcion): #contiene los algoritmos de cada opcion seleccionada de la calculadora
    if opcion == '1':
        print(mt.suma1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))      
    elif opcion == '2':
        print(mt.resta1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '3':
        print(mt.multiplicacion1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '4':
        print(mt.division1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '5':
        print(mt.potencia1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '6':
        print(mt.raiz(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '7':
        print(mt.base_10(int(input('ingrese primer valor: '))))
    elif opcion == '8':
        print(mt.mayor1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '9':
        print(mt.menor1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '10':
        print(mt.and1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '11':
        print(mt.or1(int(input('ingrese primer valor: ')), int(input('ingrese segundo valor: '))))
    elif opcion == '0':
        system("cls")
    else:
        print("\nha seleccionado una opcion no valida\n")


def lista_opciones():   #lista para imprimir en pantalla las opciones disponibles en la calculadora
    salida = []
    salida.append("1. suma")
    salida.append("2. resta")
    salida.append("3. multiplicacion")
    salida.append("4. division")
    salida.append("5. potencia")
    salida.append("6. raiz")
    salida.append("7. base 10")
    salida.append("8. mayor de dos numeros")
    salida.append("9. menor de dos numeros")
    salida.append("10. boleano and")
    salida.append("11. boleano or")
    salida.append("0. Fin de funciones basicas")
    return salida


def bloque(opcion,opciones,programa2):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    print(f'{opciones[int(opcion)-1]}\n')
    opcion_n(opcion)
    if opcion != '0':
        input("\n\npresione enter para continuar")
        programa2()

def programa2():
    system('cls')
    print('QUE OPERACION DESEA REALIZAR?:\n')
    opciones = lista_opciones()          # trae la lista de las opciones que se mostraran en pantalla
    [print(x) for x in opciones]            #imprime en pantalla las opciones a elegir
    opcion = input('\n')                    #lee la opcion seleccionada por el usuario
    bloque(opcion,opciones,programa2)     #ejecuta el bloque de instrucciones segun la opcion elegida
