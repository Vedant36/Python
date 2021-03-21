import numpy as np
import sys
import ai7 as nn

asd = np.genfromtxt('../datasets/iris.csv', dtype=str, delimiter = ',', skip_header=1)
np.random.shuffle(asd)
x, y = np.split(asd, [-1], 1)
x = x.astype(float)
_x = (x-x.min(0))/(x.max(0)-x.min(0))
uni = np.unique(y)
_y = np.array([[int(j[0]==i) for i in uni] for j in y], np.uint8)

# _x = np.random.random((100,1))
# _y = (np.sin(2*_x*np.pi-np.pi)+1)/2

U = nn.Network(_x.shape[1], 16, _y.shape[1])
det = sys.argv[1:]+[10000,0.03][len(sys.argv)-1:]
U.train(_x, _y, ite=int(det[0]), e = float(det[1]))
print(U.predict(_x)[-1][:10].T)
print(_y[:10].T)

# import matplotlib.pyplot as plt

