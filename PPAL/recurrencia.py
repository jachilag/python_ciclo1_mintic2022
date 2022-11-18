from operator import mod

'''Este archivo contiene funciones para realizar calculos con los digitos de numero enteros,  tales como 
seleccionar el primer o ultimo o el n digito de un entero, realizar sumatorias, eliminar digitos o insertar un digito
en la primera posicion; tambien contiene una funcion para determinar si un numero es palindromo.
Todas las funciones se realizaron con el concepto de RECURSIVIDAD'''

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
    if longitud_numero(numero) == 0:
        return 0
    else:
        return ultimo_numero(numero) + suma_digitos2(eliminar_ultimo_numero(numero))

def sumatoria_Ncuadrados(n=0):
    if n == 0:
        return 0
    else:
        return n**2 + sumatoria_Ncuadrados(n-1)

def longitud_numero(numero,i=0):
    if numero % 10**i == numero:
        return i
    else:
        return longitud_numero(numero,i+1)

def primer_numero(numero,i=0):
    if numero % 10**i == numero:
        return int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))
    else:
        return primer_numero(numero,i+1)

def eliminar_primer_numero(numero,i=0):
    if numero % 10**i == numero:
        return numero-(int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))*10**(i-1))
    else:
        return eliminar_primer_numero(numero,i+1)

def insertar_primer_numero(numero,insertar=0,i=0):
    if numero % 10**i == numero:
        return numero+(insertar*10**i)
    else:
        return insertar_primer_numero(numero,insertar,i+1)

def invertir_digitos(numero,i=0,numero2=0):
    if numero % 10**(i) == numero:
        return numero2
    else:
        if i == 1:
            numero2 = (int((mod((numero-mod(numero,(10**(i-2)))),(10**(i))))/(10**(i-1)))) + 1
        numero2 = (numero2*10) + (int((mod((numero-mod(numero,(10**(i-1)))),(10**(i+1))))/(10**(i))))
        return invertir_digitos(numero,i+1,numero2)

def fibonacci(numero,lista=[0,1],i=0):
    if i == numero-2:
        return lista
    else:
        lista.append(lista[len(lista)-2]+lista[len(lista)-1])
        return fibonacci(numero, lista, i+1)
        return No