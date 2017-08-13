import numpy as np
import math
A = np.array([[0,1,-2],[-3,7,-3],[3,-5,5]])
l, P = np.linalg.eig( A )
print(np.diag(l))
detA = np.linalg.det(A)
print(P)
print(detA)
