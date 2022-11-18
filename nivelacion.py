def salidas(texto1,texto2):
    lista = [0 for i in range(len(texto2))]

    for letra in range(len(texto2)):
        if texto1[letra] == texto2[letra]:
            lista[letra] = 1
    return lista

Bianca,Camila,Vestido = eval(input('datos de entrada: '))
salidaBianca = salidas(Bianca,Vestido)
salidaCamila = salidas(Camila,Vestido)
print(salidaBianca,salidaCamila)

'''
entrada: ['B','R','V','A','D','N'],['A','V','G','A','M','P'],['A','V','R','A','D','P']
salida: [0, 0, 0, 1, 1, 0] [1, 1, 0, 1, 0, 1]
'''