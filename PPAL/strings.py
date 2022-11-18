def unir_texto(a,b):
  return a+b

def conteo_letras(string):
    return len(string)

def conteo_repetidos(texto):
    def unicos(msj):
        text = tuple(msj)  #convertimos el mensaje en tupla
        msj = ""
        for i in range(len(text)): 
            if text[:i].count(text[i]) == 0: 
                msj += text[i]
        return msj
    
    return len(texto)-len(unicos(texto))
    