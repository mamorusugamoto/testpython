import numpy as np
import math


def average1(a):
    return sum(a)/len(a)

def average2(b):
    return sum(b)/len(b)

print(a)
print(b)



def variance(a):
    av = average1(a)
    list = []
    for v in a:
        list.append((v - av) ** 2)
    ans = average1(list)
    return ans

def variance(b):
    av = average2(b)
    list = []
    for v in a:
        list.append((v - av) ** 2)
    ans = average2(list)
    return ans


average()



answer = variance([37,28,22,41,34,30,25,100,45,46])
print(answer)
print(math.sqrt(answer))
