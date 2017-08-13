import numpy as np
import math
import chainer
from chainer import Chain, Variable
import chainer.functions as F
import chainer.links as L
# for i in range(100):
#   print(i)

# class Testclass():
#      def __init__(self):
#          print("init")
#
#      def __call__(self):
#          print("call")
#
#      def aiueo(self):
#          print("call")
#
#
# model = Testclass()
# model()
#
# model.aiueo()


class Human:
     def __init__(self):
         print("init")

     def __call__(self):
         print("call")

     def showname(self):
         print(self.name)


model = Human()

model.name = "sugamoto"


model.showname()
