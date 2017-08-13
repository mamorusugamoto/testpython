import numpy as np
import chainer
from chainer import Chain, Variable
import chainer.functions as F
import chainer.links as L

class NeuralNet(chainer.Chain):
    def __init__(self, n_units, n_out):
        super().__init__(
            l1=L.Linear(None, n_units),
            l2=L.Linear(n_units, n_units),
            l3=L.Linear(n_units, n_out),
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)

def check_accuracy(model, xs, ts):
    ys = model(xs)
    loss = F.softmax_cross_entropy(ys, ts)
    ys = np.argmax(ys.data, axis=1)
    
    cors = (ys == ts)
    num_cors = sum(cors)
    accuracy = num_cors / ts.shape[0]
    return accuracy, loss

def main():
    model = NeuralNet(50, 10)

    optimizer = chainer.optimizers.Adam()
    optimizer.setup(model)

    train, test = chainer.datasets.get_mnist()
    xs, ts = train._datasets
    txs, tts = test._datasets

    bm = 100

    for i in range(100):

        for j in range(600):
            model.zerograds()
            x = xs[(j * bm):((j + 1) * bm)]
            t = ts[(j * bm):((j + 1) * bm)]
            t = Variable(np.array(t, "i"))
            y = model(x)
            loss = F.softmax_cross_entropy(y, t)
            loss.backward()
            optimizer.update()

        accuracy_train, loss_train = check_accuracy(model, xs, ts)
        accuracy_test, _           = check_accuracy(model, txs, tts)

        print("Epoch %d loss(train) = %f, accuracy(train) = %f, accuracy(test) = %f" % (i + 1, loss_train.data, accuracy_train, accuracy_test))

if __name__ == '__main__':
    main()
