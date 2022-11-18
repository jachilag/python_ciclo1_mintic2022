'''Este es un modelo de programa que almacena varios scripts que se vayan a desarrollar
con el fin de no tener tantos scripts separados en diferentes archivos.py ademas de que 
visualmente es mas practico para poder revisar diferentes codigos implementados anteriormente'''

from distutils.util import execute
from os import system
from PPAL.Matematicas import suma1 as sum
from operator import mod 
system("cls")

def opcion_1():
    def invertir_digitos(numero,i=0,numero2=0):
        if numero % 10**(i) == numero:
            return numero2
        else:
            if i == 1:
                numero2 = (int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))) + 1
            numero2 = (numero2*10) + (int((mod((numero-mod(numero,(10**(i-1)))),(10**(i+1))))/(10**(i))))
            return invertir_digitos(numero,i+1,numero2)

    print(invertir_digitos(int(input('ingrese un numero entero : '))))

def opcion_2():
    sum(4,5)
def opcion_3():
    None
def opcion_4():
    None
def opcion_5():
    None
def opcion_6():
    None
def opcion_7():
    None
def opcion_8():
    None
def opcion_9():
    None
def opcion_10():
    None

def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    try:
        if opcion != '0':
            extrae = lambda lista: lista[0]
            print(extrae([i for i in opciones if i.find(opcion+'.') != -1]),'\n')
            eval(f'opcion_{str(opcion)}()') #opcion_3()
            #if opcion!= 1: #agregar or ... a esta instruccion en caso que hayan mas submenus
            input("\n\npresione enter para continuar")
            programa()
        elif opcion == '0':
            system("cls")
    except:
        print("\nerror\n")
        input("\npresione enter para continuar")
        programa()


def programa():
    system('cls')
    print('Ingrese un ejercicio que quiera comprobar:\n')
    opciones=[]
    opciones.append("1. primer_tema_tratado")
    opciones.append("2. segundo_tema_tratado")
    opciones.append("3. tercer_tema")
    opciones.append("4. cuarto_tema")
    opciones.append("5. n_tema")
    opciones.append("6. n_tema")
    opciones.append("7. n_tema")
    opciones.append("8. n_tema")
    opciones.append("9. n_tema")
    opciones.append("10. n_tema")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)
        
#PROGRAMA PRINCIPAL
programa()