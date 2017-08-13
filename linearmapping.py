import numpy as np
import math

def kainokoushiki(a, b, c):
  ans1 = (-b + math.sqrt( b ** 2 - 4 * a * c)) / (2 * a)
  ans2 = (-b - math.sqrt( b ** 2 - 4 * a * c)) / (2 * a)
  return [ans1,ans2]


answer = kainokoushiki(1, -3, -4)
print(answer)

# e1 = np.array([1,0])
# e2 = np.array([0,1])
# A = np.array([e1,e2]).T
#
# f1 = np.array([2,0])
# f2 = np.array([0,2])
# B = np.array([f1,f2]).T
#
# invA = np.linalg.inv(A)
# invB = np.linalg.inv(B)
#
# tranA = invB.dot(A)
# tranB = invA.dot(B)
#
# print(tranA)
# print(tranB)
