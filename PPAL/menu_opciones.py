'''esta libreria contiene tres funciones que son las que se ejecutan en el programa principal del taller paquetes'''

from os import system
from PPAL import strings as st
from PPAL import graficas as grf
from PPAL import cargue_archivos as ca
from PPAL.menu_basicas import programa2 as pg2
from PPAL.menu_recurrencia import programa3 as pg3
from PPAL.menu_graficas import programa4 as pg4


def opcion_n(opcion): #contiene los algoritmos de cada opcion seleccionada de la calculadora
    if opcion == '1':       #menu de operaciones basicas
        pg2() 
    elif opcion == '2':     #conteo de letras en un str
        print(st.conteo_letras(input('ingrese texto: ')))
    elif opcion == '3':     #conteo de palabras en estructura de datos
        print(st.conteo_letras(input('ingrese texto: ')))
    elif opcion == '4':     #conteo de repetidos en string, tupla o lista
        st.conteo_repetidos(input('Ingrese texto: '))
    elif opcion == '5':     #menu graficas (4 graficas)
        pg4()
    elif opcion == '6':     #datos csv para graficar
        ca.ventas()
    elif opcion == '7':     #grafica sinusoidal y creacion de archivo
        grf.grafica_seno()
        with open("C:/Users/User/Desktop/jonathan/Mintic/python/PPAL/archivos/archivocsv.csv", 'w') as acsv:
            None
    elif opcion == '8':     #menu recurrencia
        pg3()
    elif opcion == '0':
        system("cls")
    else:
        print("\nha seleccionado una opcion no valida\n")


def lista_opciones():   #lista para imprimir en pantalla las opciones disponibles en la calculadora
    salida = []
    salida.append("1. operaciones basicas")
    salida.append("2. conteo de letras de un texto")
    salida.append("3. conteo de palabras en string, tupla o lista")
    salida.append("4. conteo de repetidos en string, tupla o lista")
    salida.append("5. graficas")
    salida.append("6. datos a graficar csv")
    salida.append("7. creacion archivo csv despues de graficar funcioni seno")
    salida.append("8. funciones rucurrentes")
    salida.append("0. Fin del programa")
    return salida


def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    print(f'{opciones[int(opcion)-1]}\n')
    opcion_n(opcion)
    if opcion != '0' and opcion != '5' and opcion != '8' and opcion != '1':
        input("\n\npresione enter para continuar")
    if opcion != '0':
        programa()