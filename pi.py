import math
from this import d
 
def leibnizPi(n):
    pi=0
    for i in range(n):
        pi = pi + (-1)**i * 4/(2*i+1)
    return pi
 
def nilakanthaPi(init):
    suma=3
    d = 2
    for n in range (2, init+1):
        suma=suma+4*(-1)**n/(d*(d+1)*(d+2))
        d = d + 2
        print(suma)
    return suma
 
def newtonPi(x_0):
    x_k = x_0
    x_k_plus_1 = 0
    while (x_k != x_k_plus_1): # nejdriv zkontrolovat rovnost, pak vypocet
        x_k_plus_1 = x_k-math.sin(x_k)/math.cos(x_k) # pak polozeni promennych
        x_k_plus_1, x_k = x_k, x_k_plus_1
        temp_d = x_k
        x_k = x_k_plus_1
        x_k_plus_1 = temp_d
        print(x_k_plus_1, x_k)
        if (x_k == x_k_plus_1): 
            return x_k_plus_1