from cmd import PROMPT
from os import system
import json as js
import pandas as pd
from pprint import pprint

system('cls')

def accion(promedio):    #retorna string con el comportamiento de la accion
    if promedio < 239:
        return 'MUY BAJO'
    elif 239 <= promedio < 265:
        return 'BAJO'
    elif 265 <= promedio < 291:
        return 'MEDIO'
    elif 291 <= promedio < 317:
        return 'ALTO'
    else:
        return 'MUY ALTO'

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
    acciones = pd.read_csv('FB.csv')  #leer archivo GLOBANT.csv
    fecha = list(acciones['Date'])  #Se genera una lista con las fechas 
    alta = list(acciones['High'])  #Se genera una lista con el precio mas alto del dia
    baja = list(acciones['Low'])  #Se genera una lista con el precio mas bajo del dia
    longitud = len(fecha)


    #================================================================================================
    #creacion de archivo analisis_archivo.csv

    promedio = [(alta[i]+baja[i])/2 for i in range(longitud)]
    concepto = [accion(promedio[i]) for i in range(longitud)]  #se genera lista con el comportamiento de la accion

    T_analisis = {
    'Fecha': fecha,
    'Mean-Min-Max': promedio,
    'Concepto':  concepto
    }

    with open('analisis_archivo.csv','w',encoding='utf-8') as f:
        [f.write(k+'\t') for k in T_analisis.keys()] #escribe los encabezados de la tabla
        f.write('\n')
        [f.write(T_analisis['Fecha'][i]+'\t'+str(T_analisis['Mean-Min-Max'][i])+'\t'+T_analisis['Concepto'][i]+'\n') for i in range(longitud)]
    

    
    #================================================================================================
    #creacion de archivo detalles.json
    
    detalles = {
        "date_lowest_prom" : fecha[promedio.index(menor_lista(promedio))],
        "lowest_prom" : menor_lista(promedio),
        "date_highest_prom": fecha[promedio.index(mayor_lista(promedio))],
        "highest_prom" : mayor_lista(promedio)
    }
    
    with open('detalles.json','w',encoding='utf-8') as d:
        js.dump(detalles,d,indent=2)
        

solucion()
