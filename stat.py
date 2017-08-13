import numpy as np
import math


def average(a,b,c,d,e):

    return (a + b + c + d + e)/5

def var(a,b,c,d,e):
    av = average(a,b,c,d,e)

    a1 = (a - av) ** 2
    a2 = (b - av) ** 2
    a3 = (c - av) ** 2
    a4 = (d - av) ** 2
    a5 = (a - av) ** 2

    return average(a1 , a2 , a3 ,a4 ,a5)
print(var(12,3,9,13,7))
