def cantidad(archivo,texto):    # funcion que retorna la cantidad de veces que encuentra un texto en un archivo
        N_sube = 0
        with open(archivo,'r',encoding='utf-8') as f:
            for linea in f:
                if linea.find(texto) != -1:
                    N_sube += 1
        return N_sube