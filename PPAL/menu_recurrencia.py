from os import system
from PPAL import recurrencia as rec

def opcion_n(opcion): #contiene los algoritmos de cada opcion seleccionada de la calculadora
    if opcion == '1':
        print(rec.ultimo_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '2':
        print(rec.eliminar_ultimo_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '3':
        print(rec.suma_digitos(int(input('ingrese un numero entero: '))))
    elif opcion == '4':
        print(rec.sumatoria_Ncuadrados(int(input('ingrese un numero entero: '))))
    elif opcion == '5':
        print(rec.longitud_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '6':
        print(rec.primer_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '7':
        print(rec.eliminar_primer_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '8':
        print(rec.insertar_primer_numero(int(input('ingrese un numero entero: '))))
    elif opcion == '9':
        print(rec.invertir_digitos(int(input('ingrese un numero entero: '))))
    elif opcion == '10':
        print(rec.fibonacci(int(input('ingrese numero de iteraciones en la serie fibonacci: '))))
    elif opcion == '0':
        system("cls")
    else:
        print("\nha seleccionado una opcion no valida\n")


def lista_opciones():   #lista para imprimir en pantalla las opciones disponibles en la calculadora
    salida = []
    salida.append("1. ultimo numero")
    salida.append("2. elminar ultimo numero")
    salida.append("3. suma de digitos")
    salida.append("4. sumatoria de cuadrados")
    salida.append("5. longitud de numero")
    salida.append("6. primer numero")
    salida.append("7. eliminar el primer numero")
    salida.append("8. insertar numero a la izquierda")
    salida.append("9. invertir digitos")
    salida.append("10. serie fibonacci")
    salida.append("0. Fin de funciones basicas")
    return salida


def bloque(opcion,opciones,programa3):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    print(f'{opciones[int(opcion)-1]}\n')
    opcion_n(opcion)
    if opcion != '0':
        input("\n\npresione enter para continuar")
        programa3()

def programa3():
    system('cls')
    print('QUE OPERACION DESEA REALIZAR?:\n')
    opciones = lista_opciones()          # trae la lista de las opciones que se mostraran en pantalla
    [print(x) for x in opciones]            #imprime en pantalla las opciones a elegir
    opcion = input('\n')                    #lee la opcion seleccionada por el usuario
    bloque(opcion,opciones,programa3)     #ejecuta el bloque de instrucciones segun la opcion elegida
