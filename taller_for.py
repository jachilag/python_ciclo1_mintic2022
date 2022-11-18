from math import factorial
from os import system
system("cls")

def opcion_1():
    for x in range(1,101):
        print(x,"-",x**2)
        
def opcion_2():
    print('\nIMPARES DEL 1-999\n')
    for x in range(1,1000):
        if x%2 != 0:
            print(x)

    print('\nPARES DEL 2-1000\n')
    for x in range(1,1001):
        if x%2 == 0:
            print(x)

def opcion_3():
    n = int(input("ingrese numero natural:\t"))
    for x in range(n,1,-1):
        if x%2 == 0:
            print(x)

def opcion_4():
    def facto(numero):
        resultado = numero
        for n in range(numero-1,0,-1):    
            resultado *= n
        return resultado

    n = int(input("ingrese numero natural:\t"))
    for x in range(1,n+1):
        print(x,"-",facto(x))

def opcion_5():
    n = int(input("ingrese numero natural:\t"))
    potencia = 2
    for x in range(2,n+1):
        potencia *= 2
    print("2 ^",n,"=",potencia)

def opcion_6():
    n = int(input("ingrese numero natural:\t"))
    x = float(input("ingrese numero real:\t"))
    potencia = x
    for y in range(2,n+1):
        potencia *= x
    print(x,"^",n,"=",potencia)

def opcion_7():
    for x in range(1,10):
        print(f"\nTabla del {x}:\n")
        for y in range(1,10):
            print(f"{x} x {y} = {x*y}")

def opcion_8():
    def exp_mclaurin(n,x):
        suma=0
        for i in range(0,n+1):
            suma += (x**i)/factorial(i)  #colocar la funcion que se desea iterar n veces
            #print(f"{i} - {suma}")  #activar para ver los resultados parciales.
        return suma

    #programa principal
    print("\ningrese n,x tal que exp(x,n)")
    n = int(input("ingrese numero natural n: "))
    x = int(input("ingrese numero real x: "))
    print(f"la exponencial de Mclaurin es: {exp_mclaurin(n,x)}")

def opcion_9():
    def seno_mclaurin(n,x):
        suma=0
        for i in range(0,n+1):
            suma += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)  #colocar la funcion que se desea iterar n veces
            #print(f"{i} - {suma}" )  #activar para ver los resultados parciales.
        return suma

    #programa principal
    print("\ningrese n,x tal que seno(x,n)")
    n = int(input("ingrese numero natural n:\t"))
    x = float(input("ingrese numero real x:\t"))
    print(f"el seno de Mclaurin es: {seno_mclaurin(n,x)}")

def opcion_10():
    def coseno_mclaurin(n,x):
        suma=0
        for i in range(0,n+1):
            suma += ((-1)**i)*(x**(2*i))/factorial(2*i)  #colocar la funcion que se desea iterar n veces
            #print(f"{i} - {suma}" )  #activar para ver los resultados parciales.
        return suma

    #programa principal
    print("\ningrese n,x tal que coseno(x,n)")
    n = int(input("ingrese numero natural n:\t"))
    x = float(input("ingrese numero real x:\t"))
    print(f"el coseno de Mclaurin es: {coseno_mclaurin(n,x)}")

def opcion_11():
    def Lnatural_mclaurin(n,x):
        suma=0
        for i in range(0,n+1):
            suma += (1/(2*i+1)) * ((x**2-1)/(x**2+1))**(2*i+1)  #colocar la funcion que se desea iterar n veces
            #print(f"{i} - {suma}" )  #activar para ver los resultados parciales.
        return suma

    #programa principal
    print("\ningrese n,x tal que Ln(x,n)")
    n = int(input("ingrese numero natural n:\t"))
    x = float(input("ingrese numero real x:\t"))
    print(f"el logaritmo natural de Mclaurin es: {Lnatural_mclaurin(n,x)}")
    
def opcion_12():
    def arctangente_mclaurin(n,x):
        suma=0
        for i in range(0,n+1):
            suma += (((-1)**i)*(x**(2*i+1))) / (2*i+1)  #colocar la funcion que se desea iterar n veces
            #print(f"{i} - {suma}" )  #activar para ver los resultados parciales.
        return suma

    def inicio():
        print("\ningrese n,x tal que Ln(x,n)")
        n = int(input("ingrese numero natural n:\t"))
        x = float(input("ingrese numero real entre [-1 y 1] x:\t"))
        if -1.0<= x <= 1.0:
            print(f"el arcotangente de Mclaurin es: {arctangente_mclaurin(n,x)}")
        else:
            input("ha ingresado un valor incorrecto. presione una tecla para continuar")
            system("cls")
            inicio()

    #programa principal
    inicio()


def bloque(opcion,opciones,programa):   #para cada opcion seleccionada se ejecuta el bloque de instrucciones
    system("cls")
    if opcion != '0':
        extrae = lambda x: x[0]
        print(extrae([i for i in opciones if i.find(opcion+'.') !=-1]),'\n')
        eval(f'opcion_{str(opcion)}()')
        #if opcion!= 1: #agregar or ... a esta instruccion en caso que hayan mas submenus
        input("\n\npresione enter para continuar")
        programa()
    elif opcion == '0':
        system("cls")
    else:
        print("\nerror\n")
        input("\npresione enter para continuar")
        programa()


def programa():
    system('cls')
    print('Ingrese un ejercicio que quiera comprobar:\n')
    opciones=[]
    opciones.append("1. numeros del 1 al 100 con su cuadrado")
    opciones.append("2. impares 1-999, pares 2-1000")
    opciones.append("3. pares menores de numero ingresado hasta el 2")
    opciones.append("4. numeros del 1 a ingresado con su factorial")
    opciones.append("5. potencia de 2 elevado a la n")
    opciones.append("6. leer n:natural, x:float y calcular x**n")
    opciones.append("7. tablas de multiplicar del 1 al 9")
    opciones.append("8. funcion exponencial serie Mclaurin")
    opciones.append("9. funcion seno serie Mclaurin")
    opciones.append("10. funcion coseno serie Mclaurin")
    opciones.append("11. funcion logaritmo natural serie Mclaurin")
    opciones.append("12. funcion arctangente serie Mclaurin")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()