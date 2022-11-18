from os import system
import json
from pprint import pprint
import random as rn 
system("cls")

def opcion_1():
    diccionario={443: 'https', 22: 'TFTTP', 80: 'Http', 53: 'DNS',  'lo': '90'}
    llaves = list(diccionario.keys())
    llaves_ordenadas = []
    otros_datos = []
    for i in llaves:
        if type(i) != str:
            llaves_ordenadas.append(i)
        else:
            otros_datos.append(i)
    llaves_ordenadas.sort()
    print(llaves_ordenadas)
    print('los siguientes son datos de tipo no numerico:\n',otros_datos)
    
def opcion_2():
    diccionario={22: 'TFTTP', 80: 'Http', 53: 'DNS', 443: 'https', 'lo': '90'}
    diccionario2={21: 'Telnet', 8080: 'Httplocal', 53: 'DNS', 443: 'https', 'lo': '90'}
    
    for k,v in diccionario.items():
        cont = 0
        for k_2, v_2 in diccionario2.items():
            if k==k_2 and v==v_2:
                print(f'llave: {k} y valor :{v} SI estan en los dos diccionarios')
                cont = 0 
                break

            cont += 1
            if cont == len(diccionario2):
                print(f'llave: {k} y valor :{v} NO estan en los dos diccionarios')

def opcion_3():
    def unir_diccionarios(dicc_1,dicc_2):
        salida = {}
        salida = dicc_2.copy()
        salida.update(dicc_1)
        return salida

    diccionario={22: 'TFTTP', 80: 'Http', 53: 'DNS', 443: 'https', 'lo': '90'}
    diccionario2={21: 'Telnet', 8080: 'Httplocal', 53: 'DNS', 443: 'https', 'lo': '90'}

    nuevo_diccionario = unir_diccionarios(diccionario,diccionario2)
    print(nuevo_diccionario)

def opcion_4():
    personas = [{"nombres":"Pedro Julio", "apellidos":"Tristan Merchan","edad":70},
            {"nombres":"pepito ", "apellidos":"perez","edad":10},
            {"nombres":"juanita", "apellidos":"velasquez","edad":20},
            {"nombres":"jonathan", "apellidos":"chila","edad":30},
            {"nombres":"daniela", "apellidos":"oses","edad":40},
            {"nombres":"giselle", "apellidos":"sanchez","edad":50},
            {"nombres":"tom", "apellidos":"cruz","edad":60}           
            ]

    def personas_rango_edad(lista, inf, sup):
        for i in lista:
            if inf <= i["edad"] <= sup:
                print(i["nombres"],i["apellidos"])

    personas_rango_edad(personas, int(input("ingrese limite inferior: ")),int(input("ingrese limite superior: ")))

def opcion_5():
    with open("files/SalesJan2009.csv", "r") as f:
        lista = f.readlines()
    cont=0
    for i in lista:
        if i.count("United Kingdom") > 0:
            cont += 1
    print(cont)

def opcion_6():
    with open("files\\SalesJan2009.csv", "r") as f:
        lista = f.readlines()
    cont=0
    medio_pago = input('ingrese el medio de pago a consultar: ')
    for i in lista:
        if i.count(medio_pago) > 0:
            cont += 1
    print(cont)

nombres = """
            {
            "jadiazcoronado":{
            "nombres": "Juan Antonio",
            "apellidos": "Diaz Coronado",
            "edad":19,
            "colombiano":true,
            "deportes":["Futbol","Ajedrez","Gimnasia"]
            },
            "dmlunasol":{
            "nombres": "Dorotea Maritza",
            "apellidos": "Luna Sol",
            "edad":25,
            "colombiano":false,
            "deportes":["Baloncesto","Ajedrez","Gimnasia"]
            }
            } 
            """

def opcion_7():
    nombres_2 = json.loads(nombres)
    deporte = input("ingrese deporte a consultar: ").capitalize()
    print('\n')
    [print(v['nombres'],v['apellidos']) for k,v in nombres_2.items() if deporte in v['deportes']] 

def opcion_8():
    nombres_2 = json.loads(nombres)
    inf, sup = int(input("ingrese rango inferior: ")), int(input("ingrese rango superior: "))
    print('\n')
    [print(v['nombres'],v['apellidos']) for k,v in nombres_2.items() if inf <= v['edad'] <= sup] 

def opcion_9():
    def unicos_lista(lista):
        return [lista[i] for i in range(len(lista)) if lista[:i].count(lista[i]) == 0]

    nombres_2 = json.loads(nombres) #deserializa objeto json como entrada de texto en consola o variable
    dep = [v_2 for k,v in nombres_2.items() for v_2 in v['deportes']]   #crea lista con los deportes que se practican
    dep = unicos_lista(dep)     #elimina los deportes repetidos de la variable dep   
    practicantes = {i:[] for i in dep}  #asigna las llaves con los deportes y los valores con listas vacias.
    {practicantes[v_2].append(k) for  k,v in nombres_2.items() for v_2 in v['deportes'] if v_2 in dep} #asigna en los valores las llaves del diccionario 'nombres_2'
    salida = json.dumps(practicantes,indent=4)  #convierte a formato JSON
    print(salida)
    
def opcion_10():
    #================================================================================================
    #algoritmo que permite seleccionar aleaoriamente datos de un archivo base y guardarlo en dos archivos 
    #para poder realizar el ejercicio planteado.
    with open('files/usuarios-23871-export.json','r',encoding="utf-8") as data:
        usuarios = json.load(data)  #carga datos.json a variable usuarios

    cedula = list(usuarios.keys())  #se crea lista con las cedulas que son las llaves del diccionario
    usuarios_1 = {cedula[i]:usuarios[cedula[i]] for i in rn.sample(list(range(13)), k=5)}   #se escogen items aleatoriamente para el primer archivo
    usuarios_2 = {cedula[i]:usuarios[cedula[i]] for i in rn.sample(list(range(13)), k=5)}   #se escogen items aleatoriamente para el segundo archivo

    #------------------------------------------------------------------------------------------------
    #genera los archivos con datos seleccionados aleatoriamente
    with open('files/usuarios_1.json','w',encoding="utf-8") as file:
        json.dump(usuarios_1, file, indent=2,ensure_ascii= False)

    with open('files/usuarios_2.json','w',encoding="utf-8") as file:
        json.dump(usuarios_2, file, indent=2,ensure_ascii= False)


    #================================================================================================
    #algoritmo que encuentra los datos coincidentes de dos archivos y los guarda en un archivo JSON
    with open('files/usuarios_1.json','r',encoding='utf-8') as data_1:
        usu_1 = json.load(data_1)   #deserializo diccionario 1

    with open('files/usuarios_2.json','r',encoding='utf-8') as data_2:
        usu_2 = json.load(data_2)   #deserializo diccionario 2

    #------------------------------------------------------------------------------------------------
    #Se crea diccionario con las coincidencias de ambos diccionarios
    usu_t = {k:v for k,v in usu_1.items() if k in usu_2.keys() and v == usu_2[k]} 
    print(json.dumps(usu_t,indent=2,ensure_ascii=False))    #imprime en pantalla lo que guardara en el archivo json

    #------------------------------------------------------------------------------------------------
    with open('files/usuarios_en_comun.json','w',encoding='utf-8') as data_t:
        json.dump(usu_t, data_t,indent=2,ensure_ascii=False)    #crea archivo json

def opcion_11():
    #================================================================================================
    #algoritmo que permite seleccionar aleaoriamente datos de un archivo base y guardarlo en dos archivos 
    #para poder realizar el ejercicio planteado.
    with open('files/usuarios-23871-export.json','r',encoding="utf-8") as data:
        usuarios = json.load(data)  #carga datos.json a variable usuarios

    notas = {v['Nombre'].replace("\"",""):[] for k,v in usuarios.items()}  #obtiene los nombres del consorcio ACO
    {notas[i].append(round(rn.uniform(2.5,5),2)) for i in notas.keys() for j in range(rn.randint(1,6))}
    pprint(notas)
    print("---------------------------------------------------------------------------------")

    #------------------------------------------------------------------------------------------------
    #genera los archivos con datos seleccionados aleatoriamente
    with open('files/notas.json','w',encoding="utf-8") as file:
        json.dump(notas, file, indent=2,ensure_ascii= False)

    #================================================================================================
    #algoritmo que lee el archivo con la lista de notas por estudiante y genera otro archivo JSON que 
    #contiene el promedio de las notas en el valor y en las llaves el nombre del estudiante 
    with open('files/notas.json','r',encoding='utf-8') as data_1:
        dnotas = json.load(data_1)   #deserializo diccionario 1

    [dnotas.update({k:round(sum(v)/len(v),2)}) for k,v in dnotas.items()] #bucle que obtiene el promedio y lo guarda en el valor de la llave

    with open('files/notas_promedio.json','w', encoding="utf-8") as data_2:
        json.dump(dnotas,data_2,indent=2,ensure_ascii=False)

    pprint(dnotas)
    
def opcion_12():
    claves = {'a':'$',
            'e':'#',
            'i':'*',
            'o':'¬',
            'u':'+',
            'á':'$',
            'é':'#',
            'í':'*',
            'ó':'¬',
            'ú':'+',
            '\"':''    
            }

    #================================================================================================
    #algoritmo que toma los nombres y los cargos de ACO y convierte los valores(cargos) encriptados segun
    #el diccionario de claves.
    with open('files/usuarios-23871-export.json','r',encoding="utf-8") as data:
        usuarios = json.load(data)  #carga datos.json a variable usuarios

    nombres = {v['Nombre'].replace("\"","").lower(): v['Cargo'].lower() for k,v in usuarios.items()}  #obtiene los nombres del consorcio ACO
    [[nombres.update({k:v.replace(k_2,v_2)}) for k,v in nombres.items()] for k_2,v_2 in claves.items()]


    with open('files/encriptado.json','w',encoding='utf-8') as file:
        json.dump(nombres,file,indent=2,ensure_ascii=False)
    pprint(nombres)
    print('------------------------------------------------------------------------------------------------')

    with open('files/encriptado.json','r',encoding='utf-8') as data:
        encriptado = json.load(data)
    [[encriptado.update({k:v.replace(v_2,k_2)}) for k,v in encriptado.items()] for k_2,v_2 in encriptado.items()]

    pprint(encriptado)
    print('------------------------------------------------------------------------------------------------')
    with open('files/desencriptado.json','w',encoding='utf-8') as data:
        json.dump(encriptado, data, indent=2, ensure_ascii= False)

def opcion_13():
    lista = [i for i in range(5)]
    def valor():
        try:
            ind = int(input('ingrese indice de la lista: '))
            return lista[ind]
        except IndexError:
            print('Intenta acceder a una posicion que no esta en el arreglo\n')
            valor()
        except ValueError:
            print('Ha ingresado un dato incorrecto. Ingrese un numero entero..\n')
            valor()
        else:
            return lista[ind]
    print(valor())

def opcion_14():
    def operar(a,b):
        try:
            return int(a)+b
        except TypeError:
            print("Los tipos de datos no cuadran para hacer la operación\n")
            main()
        except ValueError:
            print("el valor ingresado no es un numero entero ..\n")
            main()

    def main():
        a = input('ingrese dato: ')
        b = 'hola'
        operar(a, b)
    main()

def opcion_15():
    def main():
        try:
            entrada = input('ingrese una llave: ')
            dict = {'James': 'Java', 'Dennis' : 'C', 'Das':'Python'}
            print(dict[entrada])
        except KeyError:
            print('intenta acceder a una llave que no esta en el diccionario... \n')
            main()
        
    main()

def opcion_16():
    #{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62,"f": 35}
    #d p h u i e t q

    json_string = input('ingrese objeto diccionario: ')
    diccionario = json.loads(json_string)
    faltantes = input("ingrese las laminas que les faltan: ")
    suma = 0
    salida = ""

    for i in faltantes:
        for k,v in diccionario.items():
            if i == k: 
                suma += v
                salida += k + " "

    print(suma)
    print(salida)

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
    opciones.append("EJERCICIOS DICCIONARIOS:")
    opciones.append("1. ascendente las llaves; si no es numerico = warning")
    opciones.append("2. verifica clave:valor si se encuentran en ambos diccionarios")
    opciones.append("3. unir dos diccionarios")
    opciones.append("4. personas en rango de edad")
    opciones.append("\nEJERCICIOS ARCHIVOS:")
    opciones.append("5. United Kingdom")
    opciones.append("6. Medio de pago")
    opciones.append("\nEJERCICIOS JSON:")
    opciones.append("7. nombres y apellidos de practicantes de un deporte ingresado por usuario")
    opciones.append("8. nombres y apellidos que esten en un rango de edad ingresado por usuario")
    opciones.append("9. deportes:[practicantes]")
    opciones.append("10. imprime keys comunes de dos archivos en un archivo JSON(genera archivos aleatoriamente)")
    opciones.append("11. promedio notas(genera notas de forma aleatoria)")
    opciones.append("12. encriptar y desencriptar datos JSON")
    opciones.append("\nEJERCICIOS CONTROL DE ERRORES:")
    opciones.append("13. error Fuera de indice de lista")
    opciones.append("14. suma error tipo de dato")
    opciones.append("15. comprueba llave de diccionario.")
    opciones.append("16. reto 4")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)

#PROGRAMA PRINCIPAL
programa()



