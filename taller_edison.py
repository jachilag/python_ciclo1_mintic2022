from os import system
system("cls")

def opcion_1():
    a = int(input("ingrese primer valor:\t"))
    b = int(input("ingrese segundo valor:\t"))
    c = int(input("ingrese tercer valor:\t"))
    print("El promedio de los tres numeros es: ",(a+b+c)/3)

def opcion_2():
    edad = int(input("Ingrese su edad:\t"))
    if edad>=18:
        print("Usted puede Votar")
    elif 0 <= edad < 18:
        print("Usted NO puede votar")
    else:
        print("dato incorrecto")

def opcion_3():
    nombre = input("ingrese su nombre:\t")
    system('cls')
    materia = input("ingrese materia:\t")
    system('cls')
    nota_1 = int(input("ingrese su nota corte 1:\t"))
    nota_2 = int(input("ingrese su nota corte 2:\t"))
    nota_3 = int(input("ingrese su nota corte 3:\t"))
    nota_final = nota_1*0.3 + nota_2*0.3 + nota_3*0.4
    system('cls')
    print("nombre:     ",nombre)
    print("materia:    ",materia)
    print("nota 1:     ",nota_1)
    print("nota 2:     ",nota_2)
    print("nota 3:     ",nota_3)
    print("NOTA FINAL: ",nota_final)

def opcion_4():
    a = int(input("ingrese primer valor:\t"))
    b = int(input("ingrese segundo valor:\t"))
    if b > a:
        print("\nEl segundo numero es el mayor:",b)
    elif b < a:
        print("\nEl primer numero es el mayor:",a)
    elif b == a:
        print("\nLos dos numeros son iguales:",b)
    else:
        print("error")
        system("pause")
        system("cls")
        opcion_4()

def opcion_5():
    a = float(input("ingrese numero real:\t"))
    if a>=0:
        print("El numero",a,"es positivo." )
    elif a<=0:
        print("El numero",a,"es negativo." )
    else:
        print("error")

def opcion_6():
    moneda = input('''
    Elija una opcion:
        1. Dolares a Pesos
        2. Pesos a Dolares
        ''')
    tasa = float(input("ingrese el valor de un dolar en pesos:\t"))
    if moneda == '1':
        cantidad = float(input("ingrese cantidad de DOLARES a convertir en PESOS:\t"))
        print("\nUsted tiene",cantidad*tasa,"pesos.")
    elif moneda == '2':
        cantidad = float(input("ingrese cantidad de PESOS a convertir en DOLARES:\t"))
        print("\nUsted tiene",cantidad/tasa,"dolares.")  

def opcion_7():
    opcion = input('''
    ELIJA UNA OPCION:
    1. consultar
    2. retirar
    3. depositar
    4. salir

    ''')
    if opcion == '1':
        system("cls")
        print("usted esta CONSULTANDO.....\n")
        system("pause")
        system('cls')
        opcion_7()
    elif opcion == '2':
        system("cls")
        print("usted esta RETIRANDO.....\n")
        system("pause")
        system('cls')
        opcion_7()
    elif opcion == '3':
        system("cls")
        print("usted esta DEPOSITANDO.....\n")
        system("pause")
        system('cls')
        opcion_7()
    elif opcion == '4':
        system("cls")
        print("usted va a SALIR.....\n")
        system("pause")
        system('cls')
    else:
        print("\n")
        print("error")
        input("\npresione una tecla para continuar")
        opcion_7()

def opcion_8():
    contador = 0
    numero = 0
    acumulado = 0
    while contador <= 5:
        numero += 1
        if numero%5 == 0:
            acumulado += numero
            contador += 1
            print(numero,"\t",acumulado)
        
def opcion_9():
    H_trabajadas = int(input("ingrese total de horas trabajadas en el día: "))
    C_ordinaria = int(input("ingrese el valor de la hora ordinaria: "))
    if 0 <= H_trabajadas <= 8:
        salario = H_trabajadas*C_ordinaria
        print("\nsu salario por sus",H_trabajadas,"ordinarias son: ", salario, "pesos")
    elif 8 < H_trabajadas <= 16:
        salario = (8*C_ordinaria) + (2*(H_trabajadas-8)*C_ordinaria)
        print("\nsus primeras 8 horas ordinarias son:\t", (8*C_ordinaria), "pesos")
        print("sus extras por sus",H_trabajadas-8," horas extas son: ", (2*(H_trabajadas-8)*C_ordinaria), "pesos")
        print("su salario es:\t", salario, "pesos")
    elif 16 < H_trabajadas:
        salario = (8*C_ordinaria) + (16*C_ordinaria) + (3*(H_trabajadas-16)*C_ordinaria)
        print("\nsus primeras 8 horas ordinarias son:\t", (8*C_ordinaria), "pesos")
        print("sus extras por sus 8 primeras horas extas son: ", (16*C_ordinaria), "pesos")
        print("sus extras por sus 8 segundas horas extas son: ", (3*(H_trabajadas-16)*C_ordinaria), "pesos")
        print("su salario TOTAL es:\t", salario, "pesos")
    else:
        print("error")
    
def opcion_10():
    def datos():
        system('cls')
        print("los temas almacenados son:\n")
        print(temas)
        print("\nTEMAS CURSO DE PYTHON\n")
        print('''que desea hacer?:
            1. ingresar un nuevo tema
            2. terminar de ingresar temas y finalizar programa
            ''')
        opcion = input()

        if opcion == "1":
            temas.append(input("ingrese un tema nuevo:\t"))
            datos()
        elif opcion == '2':
            system('cls')
            print("los temas en el curso de python son:\n\n",temas,"\n")
            print("\nel primer tema de la lista es:\t",temas[0])
            print("el ultimo tema de la lista es:\t",temas[len(temas)-1],"\n\n")
        else:
            input("\nha digitado una opcion incorrecta.... presiones enter para continuar\n")
            datos()


    #PROGRAMA PRINCIPAL
    temas = []
    datos()

def opcion_11():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = [9, 10, 11, 12]

    my_lista = [a, b, c]
    for x in range(3):
        print(my_lista[x])

    print("\nEl primer elemento de la nueva lista es: ",my_lista[0][0])
    print("El ultimo elemento de la nueva lista es: ",my_lista[len(my_lista)-1][len(my_lista[x])-1])
    print("El primer elemento de la fila 1 es: ",my_lista[0][0])
    print("El primer elemento de la fila 2 es: ",my_lista[1][0])
    print("El primer elemento de la fila 3 es: ",my_lista[2][0])


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
    print('Ingrese un punto del taller que quiera ver:\n')
    opciones=[]
    opciones.append("1. Promedio de tres numeros")
    opciones.append("2. Derecho al voto")
    opciones.append("3. Nota final")
    opciones.append("4. Ordena dos numeros descendete")
    opciones.append("5. Positivo o Negativo")
    opciones.append("6. Conversion Dolares-pesos y visceversa")
    opciones.append("7. Cajero")
    opciones.append("8. Sumatoria 10 primeros multiplos de 5")
    opciones.append("9. Dinero trabajador")
    opciones.append("10. Lista de temas Python")
    opciones.append("11. Lista cuadro")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()
