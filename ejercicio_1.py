from os import system
system('cls')

def aciertos(cadena,comparacion):
    lista = []

    for letra in range(len(comparacion)):
        if cadena[letra] == comparacion[letra]:
            lista.append(1)
        else:
            lista.append(0)
    return lista

letrasBianca,letrasCamila,letrasVestido = eval(input('ingrese datos: '))
aciertosBianca = aciertos(letrasBianca,letrasVestido)
aciertosCamila = aciertos(letrasCamila,letrasVestido)
print(aciertosBianca,aciertosCamila)

'''
['B','R','V','A','D','N'],['A','V','G','A','M','P'],['A','V','R','A','D','P']
Bianca: brvadn
camila: avgdmp
vestidos: avradp
'''