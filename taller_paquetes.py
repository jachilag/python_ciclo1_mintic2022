from os import system
import PPAL.menu_opciones as op

def programa():
    system('cls')
    print('CALCULADORA\n\n')
    opciones = op.lista_opciones()                              # trae la lista de las opciones que se mostraran en pantalla
    [print(x) for x in opciones]                                #imprime en pantalla las opciones a elegir
    opcion = input('\n\nIngrese una operacion a realizar: \n')  #lee la opcion seleccionada por el usuario
    op.bloque(opcion,opciones,programa)                         #ejecuta el bloque de instrucciones segun la opcion elegida

#PROGRAMA PRINCIPAL
programa() 