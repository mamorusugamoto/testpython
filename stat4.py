import numpy as np
import math


def average1(a,b,c,d,e):

    return (a + b + c + d + e)/5

def average2(a,b,c,d,e):

    return (a + b + c + d + e)/5

def var1(a,b,c,d,e):
    av1 = average1(a,b,c,d,e)

    a1 = (a - av1) ** 2
    a2 = (b - av1) ** 2
    a3 = (c - av1) ** 2
    a4 = (d - av1) ** 2
    a5 = (e - av1) ** 2

    return average1(a1 , a2 , a3 ,a4 ,a5)

def var2(a,b,c,d,e):
    av2 = average2(a,b,c,d,e)

    b1 = (a - av2) ** 2
    b2 = (b - av2) ** 2
    b3 = (c - av2) ** 2
    b4 = (d - av2) ** 2
    b5 = (e - av2) ** 2

    return average2(b1 , b2 , b3 ,b4 ,b5)


def double(a,b,c,d,e,f,g,h,i,j):
    av1 = average1(a,b,c,d,e)
    av2 = average1(f,g,h,i,j)

    c1 = (a - av1)*(f - av2)
    c2 = (b - av1)*(g - av2)
    c3 = (c - av1)*(h - av2)
    c4 = (d - av1)*(i - av2)
    c5 = (e - av1)*(j - av2)

    return (c1+c2+c3+c4+c5)/5

print(double(9,5,1,3,7,2,5,9,6,8))


kyou = double(9,5,1,3,7,2,5,9,6,8)

bunsan1 = var1(9,5,1,3,7)
print(bunsan1)
bunsan2 = var2(2,5,9,6,8)
print(bunsan2)

hennsa1 = math.sqrt(bunsan1)
hennsa2 = math.sqrt(bunsan2)

soukannkeisuu = kyou / (hennsa1 * hennsa2)

print(soukannkeisuu)
print(bunsan1)
