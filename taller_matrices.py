from os import system
from numpy import append
from pandas import array
system("cls")

def suma_vector(arreglo):
    suma = 0
    for i in arreglo:
        suma += i
    return suma


def promedio(arreglo):
    return suma_vector(arreglo)/len(arreglo)


def producto_punto(arreglo_1, arreglo_2):
    return suma_vector([arreglo_1[i]*arreglo_2[i] for i in range(len(arreglo_1))])
#print((producto_punto([1,2,3,4],[5,4,3,2,1]))) #35

def producto_punto_directo(arreglo_1, arreglo_2):
    return [arreglo_1[i]*arreglo_2[i] for i in range(len(arreglo_1))]
#print(producto_punto_directo([1,2,3,4,5],[5,4,3,2,1])) #[5, 8, 9, 8, 5]

def mediana(arreglo):
    arreglo.sort()  #ordena los datos ascendente
    if len(arreglo) % 2 != 0:   #si cantidad de datos es impar, se escoge en de la posicion de la mitad
        return arreglo[int((len(arreglo)-1)/2)]
    else:   #si es par, entonces es el promedio de los valores alrededor del centro.
        return (arreglo[int((len(arreglo)-1)/2)]+arreglo[int((len(arreglo)+1)/2)])/2
#print(mediana([1,2,3,4]))

def ceros_al_final(arreglo):
    arreglo_salida = [i for i in arreglo if i != 0]
    ceros = len(arreglo)-len(arreglo_salida)
    arreglo_salida += [0 for i in range(ceros)] 
    return arreglo_salida
#print(ceros_al_final([0, 11, 36, 10, 0, 17, -23, 81, 0, 0, 12, 11, 0])) #resultado: [11, 36, 10, 17, -23, 81, 12, 11, 0, 0, 0, 0, 0]

def matriz_ceros(filas,columnas):
    return [[0 for x in range(columnas)] for y in range(filas)]


def suma_matrices(matriz_1, matriz_2): #falta hacer control de errores para cuando filas o columnas es de 1
    resultado = matriz_ceros(len(matriz_2),len(matriz_2[0])) #creacion de matriz de ceros
    congruencia = (len(matriz_1) == len(matriz_2)) and (len(matriz_1[0]) == len(matriz_2[0]))
    if congruencia:
        for fil in range(len(matriz_1)):
            for col in range(len(matriz_1[0])):
                resultado[fil][col] = matriz_1[fil][col] + matriz_2[fil][col]
    if congruencia == False:
        print("\nno se pueden sumar dos matrices de diferente tamaño\n")
        resultado = []
    return resultado


def suma_matrices2(matriz_1: array, matriz_2: array): #falta hacer control de errores para cuando filas o columnas es de 1
    congruencia = (len(matriz_1) == len(matriz_2)) and (len(matriz_1[0]) == len(matriz_2[0]))
    resultado = [[matriz_1[fil][col] + matriz_2[fil][col] for col in range(len(matriz_1[0]))] for fil in range(len(matriz_1)) if congruencia]
    if congruencia == False:
        print("\nno se pueden sumar dos matrices de diferente tamaño\n")
        resultado = []
    return resultado


def multiplicacion_matrices(matriz_1, matriz_2):
    congruencia = (len(matriz_1[0]) == len(matriz_2))
    resultado = [[producto_punto([matriz_1[fil][i] for i in range(len(matriz_1))],[matriz_2[j][col] for j in range(len(matriz_2))]) for col in range(len(matriz_2[0]))] for fil in range(len(matriz_1)) if congruencia]
    if congruencia == False:
        print("\nno se pueden sumar dos matrices de diferente tamaño\n")
        resultado = []
    return resultado
#matri = multiplicacion_matrices([[1,2],[3,4]],[[3,5,7],[4,6,8]]) #res= [[11, 17, 23], [25, 39, 53]]

def suma_col_matriz(matriz,columna): #columna indexada
    return suma_vector([matriz[i][columna] for i in range(len(matriz))])
#matri = [[3,5,7],[4,6,8]]
#print([suma_col_matriz(matri,i) for i in range(len(matri[0]))])

def suma_fil_matriz(matriz,fila):   #fila indexada
    return suma_vector([matriz[fila][i] for i in range(len(matriz[0]))])
#matri = [[3,5,7],[4,6,8]]
#print([suma_fil_matriz(matri,i) for i in range(len(matri))])

def suma_diag_matriz(matriz): #diagonal 1 es la que empieza en la posicion 0,0; la que no empieza en esa pocision es la diagonal 2
    primer_diagonal = suma_fil_matriz([[matriz[i][i] for i in range(len(matriz))]],0)
    segunda_diagonal = suma_fil_matriz([[matriz[i][len(matriz)-i-1] for i in range(len(matriz))]],0)
    return [primer_diagonal,segunda_diagonal]


def matriz_magica(matriz):  #es la que la suma de todas sus columnas filas y diagonales suman lo mismo.    
    filas = [suma_fil_matriz(matriz,i) for i in range(len(matriz))] # suma de filas
    columnas = [suma_col_matriz(matriz,i) for i in range(len(matriz[0]))]   #suma de columnas
    diagonales = suma_diag_matriz(matriz) + [columnas[0]]   #suma diagonales
    return filas == columnas == diagonales
#print(matriz_magica([[8,1,6],[3,5,7],[4,9,2]]))

def repetidos_lista(lista):
    cont = 0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j]:
                cont += 1
                break

    if cont == 0:
        print("NO existen elementos repetidos")
#repetidos_lista([1,2,3,4,5,4,3,2,1])

def palindromos_en_lista(lista):
    cont = 0
    for i in lista:
        var = i.lower()
        var = var.replace(" ","")
        if var == var[::-1]:
            print(i)
            cont += 1
    if cont == 0:
        print("no existe")
#palindromes_lista(['Luz azul','amor a roma','reconocer','hola daniel','la ruta natural'])

def vocales_lista(lista):
    vocales = "aeiou"
    cont_1 = 0
    cont_2 = 0 
    for i in lista: #recorre cada elemento de lista
        cont_2 = 0
        var = i.lower()
        for j in vocales:   #recorre cada vocal
            if var.find(j) != -1:
                cont_2 += 1
            if cont_2 == 2:
                print(i)
                cont_1 += 1
                break
            
    if cont_1 == 0:
        print("no existe")
#vocales_lista(['Luz azul','amor a roma','reconocer','hola daniel','la ruta natural', 'sol'])
#vocales_lista(['mar', 'sal','sol', 'el'])

def lista_palindromo(lista):
    return "SI es palindromo" if lista == lista[::-1] else "NO es palindromo"
#print(lista_palindromo(['a','m','o','r','a','r','o','m','a']))

def faltantes_listas(lista_1, lista_2):
    salida = []
    for i in lista_1:
        cont = 0
        for j in lista_2:
            cont += 1
            if j == i:
                break
            if cont == len(lista_2):
                salida.append(i)
    return salida
#print(faltantes_listas([1, 'Hola', -12.3, True],[11, -12.3, 'Hola', False]))

def unicos_lista(lista):    #deja los valores unicos en la lista
        return [lista[i] for i in range(len(lista)) if lista[:i].count(lista[i]) == 0]