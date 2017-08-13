import numpy as np
import math


def average(a):
    return sum(a)/len(a)

def variance(a):
    av = average(a)
    list = []
    for v in a:
        list.append((v - av) ** 2)
    ans = average(list)
    return ans

answer = variance([37,28,22,41,34,30,25,100,45,46])
print(answer)
print(math.sqrt(answer))
