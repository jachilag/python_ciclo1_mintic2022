from os import system
system("cls")

def opcion_1():
    materias = ['matematicas','fisica', 'historia', 'ed. fisica', 'etica','quimica','lenguaje','ingles','sistemas','habilidades']
    nota = [float(input(f'que nota saco en la materia {x}: ')) for x in materias] #ciclo para preguntar al usuario las notas
    print('\nTus notas son: \n')
    [print(f'en {materias[y]} has sacado {nota[y]}') for y in range(len(materias))] #ciclo para imprimir las notas 


def opcion_2():
    ganadores = []
    opc = 1
    print('Para salir ingrese 0\n')
    while opc != 0:
        ganadores.append(int(input(f"ingrese numero {len(ganadores)+1} ganador: ")))
        opc = ganadores[len(ganadores)-1]
    
    ganadores.pop()
    print(f"\nlos numeros ordenados de menor a mayor son: \n{sorted(ganadores)}")
    print(f"\nlos numeros ordenados de mayor a menor son: \n{sorted(ganadores,reverse=True)}")

    
def opcion_3():
    numeros = [x for x in range(1,11)]
    numeros.sort(reverse=True)
    print(numeros ,end=", ")
 

def opcion_4():
    materias = ['matematicas','fisica', 'historia', 'ed. fisica', 'etica','quimica','lenguaje','ingles','sistemas','habilidades']
    nota = []
    nota_limite = 3.0

    for x in materias: #ciclo para preguntar al usuario las notas
        nota.append(float(input(f'que nota saco en la materia {x}: '))) 

    #eliminar aprobadas
    for y in range(len(materias)-1,-1,-1):#range(len(materias)-1,0,-1)=(8,7,6,5,4,3,2,1,0)
        if nota[y] >= nota_limite:
            nota.pop(y)
            materias.pop(y)

    print("usted tiene que repetir :", materias)


def opcion_5():
    materias = ['matematicas','fisica', 'historia', 'ed. fisica', 'etica','quimica','lenguaje','ingles','sistemas','habilidades']
    nota_limite = 3.0
    nota = [float(input(f'que nota saco en la materia {x}: ')) for x in materias]   
    print(f"usted tiene que repetir: {[materias[y] for y in range(len(materias)) if nota[y] < nota_limite]}")


def opcion_6():
    entrada = tuple(map(lambda letra: letra.upper() ,input("ingrese serie de repeticiones: ").split(",")))
    #entrada = input("ingrese serie de repeticiones: ").replace(",","").upper() #esta opcion es viable para trabajar con strings
    'E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E'
    cuerdas =  [entrada[0]] #variable de salida de las letras en mayuscula
    cantidad = [1]   #variable de salida de las repeticiones de las cuerdas
    for x in range(1,len(entrada)):   
        if entrada[x] == entrada[x-1]:
            cantidad[len(cantidad)-1] += 1
        else:
            cuerdas.append(entrada[x])
            cantidad.append(1)
    [print(i, end=" ") for i in cuerdas]
    [print(j, end=" ") for j in cantidad]


def opcion_7():
    secuencia = list(input("ingrese serie de repeticiones: ").split(",")) #recibe los datos
    'E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E'

    for n in range(len(secuencia)):   #pasa los letras a mayusculas
        secuencia[n] = secuencia[n].upper()

    salida_1 =  [secuencia[0]] #variable de salida de las letras en mayuscula
    salida_2 = [1]   #variable de salida de las repeticiones de las salida_1

    for n in range(1,len(secuencia)):   
        if secuencia[n] == secuencia[n-1]:
            salida_2[len(salida_2)-1] += 1
        else:
            salida_1.append(secuencia[n])
            salida_2.append(1)

    for i in salida_1:
        print(i, end=" ")

    for j in salida_2:
        print(j, end=" ")


def opcion_8():
    secuencia = list(input("ingrese serie de repeticiones: ").split(",")) #recibe los datos
    'E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E'

    for n in range(len(secuencia)):   #pasa los letras a mayusculas
        secuencia[n] = secuencia[n].upper()

    secuencia.append("*")

    letra = []
    veces = []
    contador = 1

    for x in range(len(secuencia)-1):# range(20)=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
        if secuencia[x] != secuencia[x+1]:
            letra.append(secuencia[x])
            veces.append(contador)
            contador = 1 
        else:
            contador += 1

    if secuencia[-1] == secuencia[-2]:
        veces[-1] = veces[-1] + 1
    else:
        letra.append(secuencia[len(secuencia)-1])
        veces.append(1)

    letra.pop()
    veces.pop()

    for i in letra:
        print(i, end=" ")

    print("\n")
    for j in veces:
        print(j, end=" ")


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
    opciones.append("1. imprime notas de materias ingresadas")
    opciones.append("2. numeros ganadores ordenados")
    opciones.append("3. numeros 1-10 manera inversa por comas")
    opciones.append("4. materias reprobadas version 1")
    opciones.append("5. materias reprobadas version 2")
    opciones.append("6. reto 3 version reducida")
    opciones.append("7. reto 3 version normal")
    opciones.append("8. reto 3 version grupal")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()