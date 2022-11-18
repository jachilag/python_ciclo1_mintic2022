from os import system
import math as m
import numpy as np
import matplotlib.pyplot as plt
system("cls")

def Misterio(a,b):
    if a<=0 and b<=0:
        return 1
    if a%2==0:
        return a+Misterio(b,b-1);
    else:
        return b+ Misterio(a+1,b)

def fibonacci(cantidad):
    lista = [0,1]
    for i in range(1,cantidad-1):
        lista.append(lista[i]+lista[i-1])
        print(lista)
    return lista

def metodoRaro():
    letras = ['C','O','L','O','M','B','I','A']
    n= len(letras)
    #print(n)
    izq = 0
    der = 0
    aux = 0
    salida = ""
    for i in range(0,n):
        print(i)
        if aux>n:
            break
        der = aux +1

        while (der>=izq):
            if der==izq:
                salida += letras[aux]
                #print(salida)
                aux += der
            der -= 1
            print(str(izq) + "-" + str(der) + "-" + str(aux))
        izq += 1
    
    return salida


def main():
    #print(metodoRaro())
    print(fibonacci(int(input('ingrese n: '))))
    

main()
