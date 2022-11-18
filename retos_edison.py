from os import system
import random
import numpy as np
import json as js
import pandas as pd
from pprint import pprint

system("cls")

def opcion_1():
    def suma_lista(lista):  #Funcion que suma todos los valores que tiene una lista 
        suma=0
        for x in lista: 
            suma+=x
        return suma

    #PROGRAMA PRINCIPAL
    p=[]
    N=[]
    opc="s"
    sp=0
    nf=0

    print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
    nombre = input("Por favor ingrese su nombre: ")
    materia = input("Ingrese el nombre de la materia: ")

    while (opc == "s" or opc == "S") and sp < 100:
        
        N.append(float(input("Ingrese la nota obtenida: ")))
        p.append(float(input("Ingrese el porcentaje de la nota: ")))
        sp = suma_lista(p)    #Se llama la funcion para que sume los porcentajes ingresados

        if sp > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            N.pop(len(N)-1)     #Elimina la ultima nota ingresada cuando % excede 100 
            p.pop(len(p)-1)     #Elimina el ultimo porcentaje ingresado cuando % excede 100 
            sp = suma_lista(p)  #Recalcula la suma de porcentajes para que quede en el estado anterior
            continue            #Finaliza el presente ciclo y salta directamente al while
        elif sp == 100:
            break   #Si la suma de porcentajes da 100, rompe el ciclo while en este punto y continua sin preguntar al estudiante
        else:
            opc = input("¿Falta añadir notas? S/N ")

    #----------------REPORTE AL ESTUDIANTE-----------------
    for x in range(len(p)): # FOR que suma los resultados de cada nota por su porcentaje
        nf+=(p[x]/100)*N[x]

    nf = round(nf,2)    #redondea a dos decimales la nota final

    if nf >= 3.00:  
        aprobacion = "aprobado"
    else:
        aprobacion = "reprobado"

    print(f"El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {nf} resultando en {aprobacion}")


def opcion_2():

#from string import ascii_uppercase as alfabeto
    def encriptador(msj):
        clave = {}  #se crea el diccionario
        cont = 0 
        encriptado = ""     #variable de salida que contendra el mensaje encriptado

        for i in range(len(msj)):   #ciclo para crear el diccionario con las letras del "alfabeto"
            if msj[:i].count(msj[i]) == 0: 
                clave[msj[i]] = alfabeto[cont]
                cont += 1

        for j in msj:   #ciclo para encriptar el mensaje de acuerdo a las letras asignadas en el diccionario
            encriptado += clave[j] 

        return encriptado, clave


    def desencriptador(encriptado, clave):
        texto = tuple(clave)   #convierte mensaje encriptado en tupla
        desenclave = {}
        desencriptado = ''

        for k,v in clave.items(): #ciclo para cambiar las claves por los valores
            desenclave[v] = k

        for j in encriptado:   #ciclo para desencriptar el mensaje.
            desencriptado += desenclave[j]  
        
        #ESTE BLOQUE FOR NO SE DEBE PRESENTAR EN EL EJERCICIO
        for k, v in desenclave.items(): #ciclo para inprimir el nuevo diccionario
            print(f'{k} : {v}')

        return desencriptado


    if True:

        """ ------------------------------------------------------------------------------------
        DE AQUI EN ADELANTE NO HACE PARTE DEL RETO, ESTO ES SOLO PARA COMPROBAR LOS EJEMPLOS """

        def ejercicio(opc):
            if opc == 1:
                alfab = 'ABKDEFGHIJL'
                msj = '¡Hola mundo!'
            elif opc ==2:
                alfab = 'JLEPDIAKSCQHFRMNGBO'
                msj = 'The Garden of Earthly Delights'
            else:
                alfab = ''
                msj = ''
                
            return alfab, msj


        def main(msj,ejercicio):
            e, c = encriptador(msj)
            print(f"\nejercicio {ejercicio}: \n")
            for k, v in c.items():
                    print(f'{k} : {v}')
            print(f'\nel mensaje encriptado es: {e}')
            print('el mensaje desencriptado es: ',desencriptador(e,c))
            print("\n")


        def unicos(msj):
            texto = tuple(msj)  #convertimos el mensaje en tupla
            msj = ""
            for i in range(len(texto)): 
                if texto[:i].count(texto[i]) == 0: 
                    msj += texto[i]
            return msj #print(unicos('JLEPDIAKESPCQPHIAFLRMPNERGBLFO'))

        #PROGRAMA PRINCIPAL 

        for i in (1,2):
            alfabeto, mensaje = ejercicio(i)
            main(mensaje,i)


def opcion_3():

    def encriptado(texto):
        #determinar la dimension minima nxn para contener el mensaje en la matriz
        longitud = len(texto)
        n, i = 0, 0   #variable que contiene la dimension de la matriz necesaria para contener el mensaje
        while i <= longitud:    
            i = n**2
            n += 1
        n -= 1
        dim = n**2
        #------------------------------------------------------------------------

        indices = [j for j in range(dim)]
        mensaje = texto.ljust(dim,"_")
        codigo_unicode = [ord(mensaje[j]) for j in range(dim)]
        msj = [[indices[j], mensaje[j], codigo_unicode[j]] for j in range(dim)]
        
        random.shuffle(msj)     #aleatoriza la lista con su clave
        clave = [msj[j][0] for j in range(dim)]
        matriz_cuadrada = np.array([[msj[i+j][2] for j in range(n)] for i in range(0,dim,n)])
        return matriz_cuadrada, clave


    def desencriptado(matriz, clave):
        n = matriz.shape[0]
        texto = ''
        for i in range(n):
            for j in range(n):
                texto += chr(matriz[i,j])

        descifrado = ""
        for i in range(len(clave)):
            descifrado += texto[clave.index(i)]

        return descifrado.replace("_","")

    #PROGRAMA PRINCIPAL
    m, c = encriptado("Today is Caturday!")
    print(desencriptado(m,c))


def opcion_4():
    def encriptado(texto):
        #determinar la dimension minima nxn para contener el mensaje en la matriz
        longitud = len(texto)
        n, i = 0, 0   #variable que contiene la dimension de la matriz necesaria para contener el mensaje
        while i <= longitud:    
            i = n**2
            n += 1
        n -= 1
        dim = n**2
        #------------------------------------------------------------------------
        msj = [[j, texto.ljust(dim,"_")[j], ord(texto.ljust(dim,"_")[j])] for j in range(dim)]  #crea lista de listas con cada caracter con su respectivo indice
        random.shuffle(msj)     #aleatoriza la lista con su clave
        clave = [msj[j][0] for j in range(dim)]
        matriz_cuadrada = np.array([[msj[i+j][2] for j in range(n)] for i in range(0,dim,n)])
        return matriz_cuadrada, clave
    
    
    def desencriptado(matriz, clave):
        n = matriz.shape[0]
        texto = "".join([chr(matriz[i,j]) for i in range(n) for j in range(n)])
        descifrado = ''.join([texto[clave.index(i)] for i in range(len(clave))])
        return descifrado.replace("_","")


    #PROGRAMA PRINCIPAL
    m, c = encriptado("Today is Caturday!")
    print(desencriptado(m,c))
    

def opcion_5():
    #funcion que elimina los simbolos no deseados, y convierte todos los textos en minusculas
    def Normalizacion_datos(lista_texto):
        simbolos = ['-','¿','?','.',',','¡','!',':','"']    #simbolos a eliminar del texto
        datos = []                                          #lista que contiene los datos de salida
        for palabra in lista_texto:                         #recorrer cada palabra de lista_texto
            cadena = palabra.lower()                        #colocar todo en minuscula
            for simbolo in simbolos:                        #recorre la lista de simbolos
                if simbolo in palabra:                      #compara si hay simbolos en cada palabra
                    cadena = cadena.replace(simbolo,'')     #si hay simbolos los elimina
            datos.append(cadena)                            #agrega la palabra normalizada a la lista 'datos'
        return datos                                        #devuelve la lista con datos normalizados


    #funcion que devuelve los valores unicos de una lista, cadena, tupla, entero o float
    def unicos(entrada):                    
        tipo = type(entrada)                #determina el tipo de dato del parametro de entrada
        if tipo == str:                     #si el tipo de dato es string, salida es de tipo string
            salida = ''
        elif tipo == list or tipo == tuple: #si el tipo de dato es lista o tupla, salida es de tipo lista
            salida = []
        elif tipo == int or tipo == float:  #si el tipo de dato es entero o flotante, salida es de tipo string
            entrada = str(entrada)          #convierte tipo numerico a string
            salida = ''
        else:
            print('esta funcion no aplica para ese tipo de datos')
            return None

        for i in range(len(entrada)):                           #recorre cada elemento de la entrada    
            if entrada[:i].count(entrada[i]) == 0:              #si no encuentra otro valor anteriormente...
                if tipo == str or tipo == int or tipo == float: #si es de tipo string entero o float...
                    salida += entrada[i]                        #...agrega dicho valor a string salida
                elif tipo == list or tipo == tuple:             #si es de tipo lista o tupla....
                    salida.append(entrada[i])                   #...agrega dato a lista salida
                else:
                    None

        numero = lambda x: float(x) if tipo == float else int(x)    #funcion anonima que convierte string a entero o flotante
        return numero(salida) if tipo == int or tipo == float else salida   #Devuelve lista 'salida' con los valores unicos


    # recibe lista y devuelve diccionario: Las llaves son los datos
    # y los valores son las veces que encuentra esos datos en la lista
    def conteo_palabras(lista):             
        listaUnicos = unicos(lista)     #llama funcion unicos 
        diccionario = {}                #diccionarip vacio de salida
        for palabra in listaUnicos:     #recoore lista de unicos
            diccionario.update({palabra: lista.count(palabra)}) #agrega item a diccionario 
        return diccionario              #retorna diccionario


    # Funcion que recibe un diccionario y devuelve una lista de sublistas de par de elementos: clave,valor.
    # De la lista resultante la organiza de mayor a menor y solo se sacan los primeros n datos que se le 
    # indiquen en el parametro 'top'
    def seleccionar_top(diccionario, top = 0):          
        lista = [[k,v] for k,v in diccionario.items()]      #crea la lista apartir del diccionario
        ordenados = sorted(lista, key=lambda frecuencia: frecuencia[1], reverse=True)   #ordena descendente la lista apartir del segundo elemento de la sublista (clave) 
        return [ordenados[i] for i in range(20)]            #devuelve los primeros 20 datos de la lista

    # FUNCION PROGRAMA PRINCIPAL
    def main(lista_texto):      
        lista1 = Normalizacion_datos(lista_texto)           
        return seleccionar_top(conteo_palabras(lista1),20) 
    
    texto = '''también, entiendo que como es temporada de elecciones las expectativas para lo que 
    lograremos este año son bajas aún así señor presidente de la cámara de representantes aprecio el 
    enfoque constructivo que usted y los otros líderes adoptaron a finales del año pasado para aprobar 
    un presupuesto y hacer permanentes los recortes de impuestos para las familias trabajadoras así que 
    espero que este año podamos trabajar juntos en prioridades bipartidistas como la reforma de la 
    justicia penal y ayudar. a la gente que está luchando contra la adicción a fármacos de prescripción 
    Tal: Vez¡ !Podamos Sorprender De ¿Nuevo A Los Cínicos?'''


    cuento = texto.replace("\n","").split(" ")
    pprint(main(cuento))


def opcion_6():

    def accion(close_i, open_i):    #retorna string con el comportamiento de la accion
        if close_i - open_i > 0:
            return 'SUBE'
        elif close_i - open_i < 0:
            return 'BAJA'
        else:
            return 'ESTABLE'

    def menor_lista(lista): #devuelve el menor valor numerico de una lista

        def menor_2(x,y):
            menor = x if x < y else y
            return  menor

        menor = lista[0]
        for x in range(1,len(lista)):
            if lista[lista.index(menor)] != menor_2(lista[lista.index(menor)],lista[x]):
                menor = lista[x]
        return menor

    def mayor_lista(lista): #devuelve el mayor valor numerico de una lista
        
        def mayor_2(x,y):
            mayor = x if x > y else y
            return  mayor

        mayor = lista[0]
        for x in range(1,len(lista)):
            if lista[lista.index(mayor)] != mayor_2(lista[lista.index(mayor)],lista[x]):
                mayor = lista[x]
        return mayor

    def cantidad(archivo,texto):    #cantidad de veces que encuentra un texto en un archivo
            N_sube = 0
            with open(archivo,'r',encoding='utf-8') as f:
                for linea in f:
                    if linea.find(texto) != -1:
                        N_sube += 1
            return N_sube

    def solucion():
        acciones = pd.read_csv('GLOBANT.csv')  #leer archivo GLOBANT.csv
        fecha = list(acciones['Date'])  #Se genera una lista con las fechas 
        apertura = list(acciones['Open'])  #Se genera una lista con el precio de apertura 
        cierre = list(acciones['Close'])  #Se genera una lista con el precio de cierre 
        alta = list(acciones['High'])  #Se genera una lista con el precio mas alto del dia
        baja = list(acciones['Low'])  #Se genera una lista con el precio mas bajo del dia
        longitud = len(apertura)


        #================================================================================================
        #creacion de archivo analisis_archivo.csv

        comportamiento = [accion(cierre[i],apertura[i]) for i in range(longitud)]  #se genera lista con el comportamiento de la accion
        punto_medio = [(alta[i]-baja[i])/2 for i in range(longitud)]

        T_analisis = {
        'Fecha': fecha,
        'Comportamiento de la accion': comportamiento,
        'Punto medio HIGH-LOW': punto_medio
        }

        with open('analisis_archivo.csv','w',encoding='utf-8') as f:
            [f.write(k+'\t') for k in T_analisis.keys()] #escribe los encabezados de la tabla
            f.write('\n')
            [f.write(T_analisis['Fecha'][i]+'\t'+T_analisis['Comportamiento de la accion'][i]+'\t'+str(T_analisis['Punto medio HIGH-LOW'][i])+'\n') for i in range(longitud)]
        

        
        #================================================================================================
        #creacion de archivo detalles.json
        
        detalles = {
            "date_lowest_price" : fecha[baja.index(menor_lista(baja))],
            "lowest_price" : menor_lista(baja),
            "date_highest_price": fecha[alta.index(mayor_lista(alta))],
            "highest_price" : mayor_lista(alta),
            "cantidad_veces_sube" : cantidad('analisis_archivo.csv','SUBE'), 
            "cantidad_veces_baja" : cantidad('analisis_archivo.csv','BAJA'),
            "cantidad_veces_estable" : cantidad('analisis_archivo.csv','ESTABLE'),
        }
        
        with open('detalles.json','w',encoding='utf-8') as d:
            js.dump(detalles,d,indent=2)
            

    solucion() 
    print('archivos analisis_archivo.csv y detalles.json, han sido generados')

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
    print('Ingrese el reto que quiera comprobar:\n')
    opciones=[]
    opciones.append("1. RETO 1: TOMA DE NOTAS DE MATERIAS")
    opciones.append("2. RETO 2: ENCRIPTAR Y DESENCRIPTAR MENSAJE")
    opciones.append("3. RETO 3: ENCRIPTAR MATRIZ V1")
    opciones.append("4. RETO 3: ENCRIPTAR MATRIZ V2")
    opciones.append("5. RETO 4: TOP 20 PALABRAS CUENTO")
    opciones.append("6. RETO 5: ANALISIS ACCIONES GLOBANT")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion,opciones,programa)

#PROGRAMA PRINCIPAL
programa()