import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


def ventas():   
    ventasdf = pd.read_csv("C:/Users/User/Desktop/jonathan/Mintic/python/PPAL/archivos/SalesJan2009.csv")
    #print(ventasdf)
    print('#------------------------------------------------------------------------------------------------')
    cp = Counter(ventasdf["Country"]).most_common(3)
    print(cp)
    cv = Counter(ventasdf["Payment_Type"])
    print(type(cv.most_common(3)))
    print(cv)
    #Reporte por fecha