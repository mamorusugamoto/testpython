import numpy as np
import math
import chainer
from chainer import Chain, Variable
import chainer.functions as F
import chainer.links as L
# for i in range(100):
#   print(i)


train, test = chainer.datasets.get_mnist()
xs, ts = train._datasets
txs, tts = test._datasets
print(xs[0])
print(ts[0])
