from os import system
system("cls")

def opcion_1():
    numero = int(input("factorial de:\t"))
    n = numero
    while n>1:    
        n -= 1
        numero *= n
    print(numero)

def opcion_2():

    def facto(numero):
        n = numero
        while n>1:    
            n -= 1
            numero = numero*n
        return numero

    def perm(n,r):
        return facto(n)/facto(n-r)

    #PROGRAMA PRINCIPAL
    n = int(input("ingrese N:\t"))
    r = int(input("ingrese r:\t"))
    print("la permutacion es:\t",perm(n,r))

def opcion_3():
    def calculo(operacion,numero_1,numero_2):
        if operacion == 1:
            resultado = numero_1 + numero_2
        elif operacion == 2:
            resultado = numero_1 - numero_2
        elif operacion == 3:
            resultado = numero_1 * numero_2
        elif operacion == 4:
            resultado = numero_1 / numero_2
        else:
            print("ha ingresado un valor incorrecto")
            resultado = None
        return resultado

    def inicio():
        print("calculadora:")
        print("1.Suma\n2.resta\n3.multiplica\n4.divide\n")
        operacion = float(input("que operacion va a realizar?\t"))
        return operacion

    #PROGRAMA PRINCIPAL
    operacion = inicio()
    numero_1 = float(input("ingrese el primer valor:\t"))
    numero_2 = float(input("ingrese el segundo valor:\t"))

    if operacion >=1 and operacion <=4:
        print("el resultado es:\t",calculo(operacion,numero_1,numero_2))
    else:
        print("ha ingresado una operacion incorrecta")

def opcion_4():
    i = 2   # inicializa a i en 2
    j = 25  # inicializa a j en 25
    while i < j:    # mientras i sea menor a j
        print(i, j, sep = ", ") # imprime los valores de i y j
        i *= 2  # i = i * 2; i se mult´ıplica por 2 en cada paso
        j += 10 # j = j + 10; se incrementa de 10 en 10

    print("the end.")   # se ejecuta al terminar el ciclo
    print(i, j, sep = ", ") # valores finales de i y j

def opcion_5():
    def calculo(operacion,numero_1,numero_2):
        if operacion == 1:
            resultado = numero_1 + numero_2
        elif operacion == 2:
            resultado = numero_1 - numero_2
        elif operacion == 3:
            resultado = numero_1 * numero_2
        elif operacion == 4:
            resultado = numero_1 / numero_2
        else:
            print("ha ingresado un valor incorrecto")
            resultado = None
        return resultado
    def inicio():
        print("\nCALCULADORA:")
        print("1.Suma\n2.resta\n3.multiplica\n4.divide\n5.salir\n")
        operacion = float(input("que operacion va a realizar?\t"))
        return operacion

    def calculadora():
        operacion = inicio()
        if operacion == 5:
            opcion = 2
        elif operacion !=5:
            numero_1 = float(input("ingrese el primer valor:\t"))
            numero_2 = float(input("ingrese el segundo valor:\t"))
            if operacion >=1 and operacion <=4:
                print("el resultado es:\t",calculo(operacion,numero_1,numero_2))
            else:
                print("ha ingresado una operacion incorrecta")
            opcion = 1
        return opcion

    #PROGRAMA PRINCIPAL
    opcion = 1
    while opcion == 1:
    #-----------------------------------------------------------
        opcion=calculadora()
    #-----------------------------------------------------------
    system('cls')

def opcion_6():
    animales = ["raton","gato","perro","leon",1,"jirafa","dinosaurio","oso"]
    for x in range(7,-1,-1):
        print(animales[x])

def opcion_7():
    def epsilon():
        epsilon = 0
        potencia = 0

        while(epsilon == 0):
            if((1 + 2 ** potencia) == 1):
                print("================")
                epsilon = potencia
                print(epsilon)
                print(1 + 2 ** potencia)
                return epsilon
            else:
                print("================")
                print(potencia)
                print(1 + 2 ** potencia)
                potencia -= 1

    epsilon = epsilon()
    print("El epsilón de la máquina es: " + str(epsilon))

def opcion_8():
    text_1=input("ingrese 1 texto\t")
    texto_2=input("ingrese 2 texto\t")

    count=0
    for i in text_1:
        if text_1.count(i)<=texto_2.count(i):
            count+=1

    if count==len(text_1):
        print("esta incluida")
    else:
        print("no esta incluida")
    
def opcion_9():
    def ronda(arma_R):
        arma_F = armas_F.find(arma_R)
        arma_V = armas_V.find(arma_R)

        if arma_F == -1 and arma_V != -1:
            ganador = "V"
        elif arma_V == -1 and arma_F != -1:
            ganador = "F"
        else:
            ganador = "E"
        return ganador
            
    #PROGRAMA PRINCIPAL 
    partida = []
    puntos_V = 0
    puntos_F = 0

    armas_V = input("Equipo Vampiric, elijan sus armas:\t")
    armas_F = input("Equipo Frenzy, elijan sus armas:\t")
    armas_reloj = input("las armas elegidas por el reloj del sistema son:\t")

    for c in armas_reloj:
        ganador_ronda = ronda(c)
        
        if ganador_ronda == "V":
            puntos_V += 1
        elif ganador_ronda == "F":
            puntos_F += 1
        else:
            None
        
        if puntos_F == puntos_V:
            partida.append('≈')
        elif puntos_F > puntos_V:
            partida.append('F')
        elif puntos_F < puntos_V:
            partida.append('V')
        else:
            None

    print("".join(partida))
    
def opcion_10():
    partida : str = ""
    puntos_V = 0
    puntos_F = 0
    armas_V = input("Equipo Vampiric, elijan sus armas:\t")
    armas_F = input("Equipo Frenzy, elijan sus armas:\t")
    armas_reloj = input("las armas elegidas por el reloj del sistema son:\t")
    for c in armas_reloj:   # Ciclo for que recorre cada letra de las armas del reloj
        if armas_F.find(c) >= 0: puntos_F += 1
        if armas_V.find(c) >= 0: puntos_V += 1
        if puntos_F == puntos_V: partida += '≈'     #Si global empatan, agraga el simbolo '≈' a la lista "partida"
        elif puntos_F > puntos_V: partida += 'F'     #Si global gana F, agraga el simbolo 'F' a la lista "partida"
        elif puntos_F < puntos_V: partida += 'V'    #Si global gana V, agraga el simbolo 'V' a la lista "partida"
        else: None 
    print(partida)   

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
    opciones.append("1. factorial")
    opciones.append("2. permutacion")
    opciones.append("3. calculadora")
    opciones.append("4. ejemplo while")
    opciones.append("5. calculadora ciclo infinito con while")
    opciones.append("6. ejemplo del ciclo FOR")
    opciones.append("7. euler de la maquina ")
    opciones.append("8. una cadena incluida en la otra?")
    opciones.append("9. reto 2 version 1")
    opciones.append("10. reto 2 version 2 reducida ")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()