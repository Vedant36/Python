import ai7 as nn
import numpy as np
import sys
from time import time

data = [['train','t10k'],['images.idx3','labels.idx1']]
resh = [[60000,10000],[784,1]]
n = 100
def load(a, b):
  from os import environ
  ret = np.fromfile(f'{environ["HOME"]}/Documents/datasets/mnist/{data[0][a]}-{data[1][b]}-ubyte', np.uint8)
  return ret[16-8*b:].reshape(resh[0][a],resh[1][b])[:n]
def acc(y0, y):
  # return 100 * np.corrcoef(y0, y)[0,1]**2 # r squared
  return 100 * (np.equal(y, y0==y0.max(1,keepdims=True))).all(1).mean()
def tok(y):
  uni = np.unique(y)
  _y = np.array([[int(j[0]==i) for i in uni] for j in y])
  return _y

x = load(0, 0)/256
y = tok(load(0, 1))
test = load(1, 0)/256, tok(load(1, 1))

rep = 1000
U = nn.Network(784,32,16,16,10)
print(f'Network = {U}')
print(f'Accuracy: {acc(U.predict(x)[-1],y):>2.9}%')
ini_time = time()
qwe = U.train(x, y, rep, 0.01)
# qwe = U.train(x, y, test, int(sys.argv[1]), float(sys.argv[2]))
print(f'[Finished in {round(time()-ini_time,5)}s]')
print(f'Accuracy: {acc(U.predict(x)[-1],y):>2.9}%')

import matplotlib.pyplot as plt
rx = np.arange(rep)
plt.scatter(rx,qwe, color='black',s=1)
plt.show()

def corner(qwe):
  ar = qwe.size
  for i in qwe:
    if not np.any(i):
      ar -= qwe.shape[-1]
  lul = ar//28
  for i in qwe.T:
    if not np.any(i):
      ar -= lul
  return ar
