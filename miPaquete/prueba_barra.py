from time import sleep
from tqdm.auto import tqdm
import sys

def barraTQDM():
    print("copiando archivos")
    for i in tqdm(range(20)):
        #pass
        sleep(0.2)

def barraTQDM_2():
    print("copiando archivos")
    for i in tqdm(range(10001)):
        
        print(" ", end = "\r")


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
        file.write("\r")
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\r")
    file.flush()
    
from progress.bar import Bar, ChargingBar
import os, time, random

def barraProgreso_1():
    bar2 = ChargingBar('Instalando:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.2))
        bar2.next()
    bar2.finish()



# for i in progressbar(range(15), "Computing: ", 40):
#     time.sleep(0.1)

# barraTQDM()
barraProgreso_1()


