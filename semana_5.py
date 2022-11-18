from os import system
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from operator import mod

system("cls")

def opcion_1():
    def producto_vincremental(n,m,iter=0):
        if iter == m:
            return 0
        else:
            return n + producto_vincremental(n,m,iter+1)

    def producto_vdecremental(n,m):
        if n==0:
            return 0
        else: 
            return m + producto_vdecremental(n-1,m)

    valor1, valor2 = int(input('ingrese factor 1: ')), int(input('ingrese factor 2: '))
    print('\n')
    print(producto_vdecremental(valor1, valor2))
    print(producto_vincremental(valor1, valor2))


def opcion_2():
    def sumatoria_n_v1(n=0):
        if n == 0:
            return 0
        else:
            return n + sumatoria_n_v1(n-1)

    def sumatoria_n_v2(n=0,iter=0):
        if n == iter:
            return n
        else:
            return iter + sumatoria_n_v2(n,iter+1)

    valor = int(input('ingrese entero para Hallar la sumatoria hasta 0: '))
    print('\n')
    print(sumatoria_n_v1(valor))
    print(sumatoria_n_v2(valor))


def opcion_3():
    ventasdf = pd.read_csv("files/SalesJan2009.csv")
    #print(ventasdf)
    print('#------------------------------------------------------------------------------------------------')
    cp = Counter(ventasdf["Country"]).most_common(3)
    print(cp)
    cv = Counter(ventasdf["Payment_Type"])
    print(type(cv.most_common(3)))
    print(cv)
    #Reporte por fecha
    if True:
        #ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"])
        #A = (ventasdf['Transaction_date']
        #.dt.floor("d")
        #.value_counts()
        #.rename_axis("date")
        #.reset_index(name="num ventas"))
        #G=A.plot(x="date",y="num ventas",color="green",title="Ventas por fecha")
        #plt.show()
        True


def opcion_4():
    lista= [[1,2,3],[4,5,6],[7,8,9]]

    #[print(elemento) for sublistas in lista for elemento in sublistas] #forma reducida
    for sublistas in lista: #recorre por totalidad de elementos
        for elemento in sublistas:
            print(elemento)

    # [print(lista[i][j]) for i in range(len(lista)) for j in range(len(lista[i]))] #forma reducida
    for i in range(len(lista)): #recorre por indices
        for j in range(len(lista[0])):
            print(lista[i][j])


def opcion_5():
    def variable_argument(*vari):
        for var in vari:
            print(var+1)

    variable_argument(10,20,30,40,50,60)


def opcion_6():
    def suma_1(a,*b,**c):
        print(a)
        for i in b:
            print(i)

        for k,v in c.items():   #recorre items de diccionario **c
            print(k,v)
        
        for k in c.keys():  #recorre items de diccionario **c
            print(k,c[k])
        
    print(suma_1(10,20,30,40,50,clave='hola' ,clave2='como te llamas'))
        

def opcion_7():
    def tipodefigurita(lista):
        return [lista[i] for i in range(len(lista)) if lista[:i].count(lista[i]) == 0]

    def mefaltandeltipodefigurita(listaFaltantes,listaTipo,tipoFigurita):
        return [i for i in listaFaltantes if listaTipo[i] == tipoFigurita]

    def notengo(otrosFiguritas,misFiguritas):
        return [i for i in otrosFiguritas if not i in misFiguritas]

    def puedocambiar(otrosFiguritas,misFiguritas):
        a = [i for i in misFiguritas if not i in otrosFiguritas]
        b = [i for i in otrosFiguritas if not i in misFiguritas]
        return min(len(a),len(b))


def opcion_8():
    def ultimo_numero(numero,i=9):
        if (numero-i)%10 == 0:
            return i
        else:
            return ultimo_numero(numero,i-1)

    print(ultimo_numero(int(input("ingrese un numero entero: "))))


def opcion_9():
    def sumatoria_Ncuadrados(n=0):
        if n == 0:
            return 0
        else:
            return n**2 + sumatoria_Ncuadrados(n-1)
    recursion = True
    valor = 0



    while recursion:
        valor += 1
        try: 
            sumatoria_Ncuadrados(valor)
        except RecursionError:
            print(f'el valor limite de recursion es: {valor}')
            recursion = False


def opcion_10():
    def sumatoria_Ncuadrados(n=0):
        if n == 0:
            return 0
        else:
            return n**2 + sumatoria_Ncuadrados(n-1)

    print(sumatoria_Ncuadrados(int(input('ingrese n para hallar la sumatoria de los primeros n**2: '))))


def opcion_11():
    def eliminar_ultimo_numero(numero,i=9):
        if (numero-i)%10 == 0:
            return int((numero - i)/10)
        else:
            return eliminar_ultimo_numero(numero,i-1)
    print(eliminar_ultimo_numero(int(input('ingrese un numero entero: '))))


def opcion_12():
    def cantidad_digitos(numero,i=0):
        if numero % 10**i == numero:
            return i
        else:
            return cantidad_digitos(numero,i+1)

    print(cantidad_digitos(int(input('ingrese valor: '))))

    
def opcion_13():
    def cantidad_digitos(numero,i=0):
        if numero % 10**i == numero:
            return i
        else:
            return cantidad_digitos(numero,i+1)

    def ultimo_numero(numero,i=9):
        if (numero-i)%10 == 0:
            return i
        else:
            return ultimo_numero(numero,i-1)

    def eliminar_ultimo_numero(numero,i=9):
        if (numero-i)%10 == 0:
            return int((numero - i)/10)
        else:
            return eliminar_ultimo_numero(numero,i-1)

    def suma_digitos(numero,i=0):
        if numero % 10**i == numero:
            return 1
        else:
            return int((mod((numero-mod(numero,(10**(i-1)))),(10**(i+1))))/(10**i)) + suma_digitos(numero,i+1)

    def suma_digitos2(numero):
        if cantidad_digitos(numero) == 0:
            return 0
        else:
            return ultimo_numero(numero) + suma_digitos2(eliminar_ultimo_numero(numero))

    valor = int(input('ingrese un numero entero: '))
    print(suma_digitos(valor))
    print(suma_digitos2(valor))


def opcion_14():
    def primer_numero(numero,i=0):
        if numero % 10**i == numero:
            return int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))
        else:
            return primer_numero(numero,i+1)

    print(primer_numero(int(input('ingrese un numero entero : '))))


def opcion_15():
    def eliminar_primer_numero(numero,i=0):
        if numero % 10**i == numero:
            return numero-(int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))*10**(i-1))
        else:
            return eliminar_primer_numero(numero,i+1)
    print(eliminar_primer_numero(int(input('ingrese un numero entero : '))))


def opcion_16():
    def insertar_primer_numero(numero,insertar=0,i=0):
        if numero % 10**i == numero:
            return numero+(insertar*10**i)
        else:
            return insertar_primer_numero(numero,insertar,i+1)

    print(insertar_primer_numero(int(input('ingrese un numero entero : ')),int(input('ingrese un numero entero a insertar : '))))


def opcion_17():
    def invertir_digitos(numero,i=0,numero2=0):
        if numero % 10**(i) == numero:
            return numero2
        else:
            if i == 1:
                numero2 = (int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))) + 1
            numero2 = (numero2*10) + (int((mod((numero-mod(numero,(10**(i-1)))),(10**(i+1))))/(10**(i))))
            return invertir_digitos(numero,i+1,numero2)

    print(invertir_digitos(int(input('ingrese un numero entero : '))))
    

def opcion_18():
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
    print('Ingrese un ejercicio que quiera comprobar:\n')
    opciones=[]
    opciones.append("1. producto recursividad")
    opciones.append("2. suma de los primeros n numeros, recursivo")
    opciones.append("3. tabular y diagramar datos con pandas matplotlib")
    opciones.append("4. lista de listas: matrices")
    opciones.append("5. sumar 1 a un grupo de datos variables a una funcion")
    opciones.append("6. impresion de diferentes tipos de entradas en funciones")
    opciones.append("7. reto 5: figuritas.py")
    opciones.append("8. recursividad: ultimo digito numero")
    opciones.append("9. recursividad: limite de ciclos")
    opciones.append("10. recursividad: primeros n**2")
    opciones.append("11. recursividad: eliminar el ultimo digito de un entero:")
    opciones.append("12. recursividad: contar cantidad de digitos de un entero")
    opciones.append("13. recursividad: suma de los digitos de un entero")
    opciones.append("14. recursividad: extraer primer numero ")
    opciones.append("15. recursividad: elimina primer digito")
    opciones.append("16. recursividad: insertar numero al principio")
    opciones.append("17. recursividad: numero invertido")
    opciones.append("18. recursividad: ")
    opciones.append("0. Fin del programa")

    [print(x) for x in opciones]
    opcion = input('\n')
    bloque(opcion, opciones, programa)
    
#PROGRAMA PRINCIPAL
programa()