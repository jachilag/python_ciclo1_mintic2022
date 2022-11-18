
def tipodefigurita(lista):
    salida = []
    for i in range(len(lista)):
        if lista[:i].count(lista[i]) == 0:
            salida.append(lista[i])
    return salida


def mefaltandeltipodefigurita(indices,listaTipo,tipoFigurita):
    salida = []

    for i in indices:
        if listaTipo[i] == tipoFigurita:
            salida.append(i)

    return salida



def notengo(otrosFiguritas,misFiguritas):
    salida = []

    for i in otrosFiguritas:
        if not i in misFiguritas:
            salida.append(i)

    return salida
    


def puedocambiar(otrosFiguritas,misFiguritas):
    salida = 0
    for i in misFiguritas:
        if not i in otrosFiguritas:
            salida += 1
    salida2 = 0
    for i in otrosFiguritas:
        if not i in misFiguritas:
            salida2 += 1

    return min(salida,salida2)

