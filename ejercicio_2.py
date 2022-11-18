import os
os.system('cls')

def run():
    verificacion = False

    while(not verificacion):

        dist_goku = int(input("¿Cual es la distancia a la casa de Goku?: "))
        if dist_goku>0:
            dist_proxesf = (2*dist_goku) + 4
            t = (dist_goku + dist_proxesf)/2

            if t>50:
                name1 = "4"
            if t>31 and t<50:
                name1 = "3"
            if t>21 and t <30:
                name1 = "2"
            if t>0 and t<20:
                name1 = "1"
            
            verificacion = True
        else:
            print("Distancia no valida")
            verificacion = False
    
    listado = [dist_goku , dist_proxesf, t, name1]
    print(listado)
    

if __name__ == "__main__":
    run()

