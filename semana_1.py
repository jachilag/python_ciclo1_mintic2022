from os import system
system("cls")

def opcion_1():
    def area_rectangulo(l, a):
        area = l * a
        return area
    largo = float(input("Largo del rectangulo: "))
    ancho = float(input("Ancho del rectangulo: "))
    print("El area del rectangulo es:", end = " ")
    print(area_rectangulo(largo, ancho))

def opcion_2():
    ValorVehiculo = int(input("\ningrese valor del vehiculo: \t"))
    porcentajeGanancia: float = 12/100
    porcentajeImpuesto: float = 6/100
    costoTotal: float = (ValorVehiculo*porcentajeGanancia) + (ValorVehiculo*porcentajeImpuesto) + ValorVehiculo

    #print(costoTotal)
    if costoTotal>50000000:
        costoTotal = costoTotal - costoTotal*0.03
        print("El vehiculo tiene un descuento de 3%: ",costoTotal*0.03)
        print("El valor del vehiculo es: ",costoTotal)
    else:
        print("El vehiculo no tiene descuento y su valor es: ",costoTotal)

def opcion_3():
    def quico(chavo):
        return 2*chavo + 4

    def nono(quico,chavo):
        return int((quico + chavo)/5)

    #PROGRAMA PRINCIPAL
    C = int(input("ingrese el peso del Chavo:\t"))
    Q=quico(C)
    N=nono(Q,C)

    if 0 <= N <= 20:
        etapa = "uno"
    elif 21 <= N <= 40:
        etapa = "dos"
    elif 40 < N < 80:
        etapa = "tres"
    elif N >= 80:
        etapa = "cuatro"
    else:
        etapa = "error"

    print(C,Q,N)
    print(etapa)

def opcion_4():
    chavo = int(input("ingrese el peso del Chavo: \t"))
    quico = 2*chavo + 4
    nono = int((quico + chavo)/5)
    if nono >= 0 and nono <=20:
        etapa = "uno"
    elif nono >= 21 and nono <=40:
        etapa = "dos"
    elif nono >= 41 and nono < 80:
        etapa = "tres"
    elif nono >= 80:
        etapa = "cuatro"
    else:
        etapa = "error"

    print(chavo,quico,nono)
    print(etapa)

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
    print('Ingrese un ejercicio que quiera comprobar de la semana 1:\n')
    opciones=[]
    opciones.append("1. area rectangulo")
    opciones.append("2. costo vehiculo")
    opciones.append("3. la vecindad 1")
    opciones.append("4. la vecindad 2")
    opciones.append("0. Fin del programa")
    
    
    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()