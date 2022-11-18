import math as m
import numpy as np
import matplotlib.pyplot as plt
def grafica_cuadratica():
    x = np.linspace(0, 90, 90)
    fig, ax = plt.subplots()
    ax.plot(x, x**2, label="cuadrado")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("graficas")
    ax.legend()
    plt.show()


def grafica_cubica():
    x = np.linspace(0, 90, 90)
    fig, ax = plt.subplots()
    ax.plot(x, x**3, label="cubica")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("graficas")
    ax.legend()
    plt.show()



def grafica_seno():
    x = np.linspace(0, 2*np.pi, 50)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label="seno")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("graficas")
    ax.legend()
    plt.show()


def grafica_raiz():
    x = np.linspace(0, 90, 90)
    fig, ax = plt.subplots()
    ax.plot(x, x**(1/2), label="raiz")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title("graficas")
    ax.legend()
    plt.show()
