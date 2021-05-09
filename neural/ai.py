#6

import numpy as np
import sys

def act(v):
  return 1/(1+np.exp(-v))
def dact(v):
  return act(v)*(1-act(v))
def acc(y0, y):
  # return 100 * np.corrcoef(y0, y)[0,1]**2 # r squared
  return 100 * (np.equal(y, (y0==y0.max(1,keepdims=True)).astype(int))).all(1).mean()

class Layer:
  def __init__(self, i=0, n=0, data=None):
    if data is None: self.w, self.b = np.random.randn(i, n), np.zeros((1, n))
    else: self.w, self.b = [np.array(i) for i in data]
  def __repr__(self):
    return f'<Layer{self.w.shape}>'
  def _p(self, inputs):
    return np.dot(inputs,self.w)+self.b

class Network:
  def __init__(self, *struc, data = None):
    if data is None:
      self.s = struc
      self.m = [Layer(*self.s[i:i+2]) for i in range(len(struc)-1)]
    else:
      self.s, asd = data
      self.m = [Layer(data=i) for i in asd]
  def __repr__(self):
    return f'<Network{self.s}>'
  def copy(self):
    return Network(data = [self.s,[[i.w.copy(),i.b.copy()] for i in self.m]])
  def tofile(self, name):
    with open(name, 'wb') as data:
      from pickle import dump
      dump([self.s,[[i.w.tolist(),i.b.tolist()] for i in self.m]], data)
  def _f(self, inputs):
    '''Forward propagate through the whole network'''
    A = [act(self.m[0]._p(inputs))]
    for i in self.m[1:]:
      A.append(act(i._p(A[-1])))
    return A
  def train(self, x, y, test, rep=1, e=1.):
    '''Train the network'''
    Q = np.zeros((rep+1))
    div = 100
    ch = {(i*rep)//div for i in range(div+1)}
    for i in range(rep+1):
      A = [x, *self._f(x)]
      V = y-A[-1]
      Q[i] = acc(self._f(test[0])[-1],test[1])
      for j, k in enumerate(self.m[::-1]):
        V*= dact(k._p(A[-2-j]))
        t = k.w.T.copy()
        k.w+= e * A[-2-j].T.dot(V)
        k.b+= e * V.mean(0)
        V = V.dot(t)
      if i in ch:
        print(f'  Accuracy at {100*i//rep:<3}%: {Q[i]:>3.4f}', end='\r')
    print()
    return Q

def load_data(name):
  from os import environ
  asd = np.genfromtxt(f'{environ["HOME"]}/Documents/datasets/{name}', dtype=str, delimiter = ',', skip_header=1)
  np.random.shuffle(asd)
  x, y = np.split(asd, [-1], 1)
  return x, y
def prepro(x, y):
  _x = (x-x.min(0))/(x.max(0)-x.min(0))
  uni = np.unique(y)
  _y = np.array([[int(j[0]==i) for i in uni] for j in y], np.uint8)
  return _x, _y

def main(attr=(), name='iris.csv'):
  np.set_printoptions(linewidth=sys.maxsize,threshold=sys.maxsize)
  from time import time
  x, y = load_data(name)
  _x, _y = prepro(x.astype(float), y)
  k = 5
  e, hid, rep = [eval(i) for i in attr]+[.01, (16,8), 10000][len(attr):]
  U=Network(_x.shape[1], *hid, _y.shape[1])
  print(f'Network = {U}')
  print(f'Accuracy: {acc(U._f(_x)[-1],_y):>2.9}%')
  fold = np.r_[x.shape[0]::k+1] # np.linspace(0, x.shape[0], k+1).astype(int)
  acu, qwe = np.zeros((k)), np.zeros((k,rep+1))
  ini_time = time()
  for i in range(k):
    U.__init__(*U.s)
    t = [np.split(_x, fold[i:i+2], 0), np.split(_y, fold[i:i+2], 0)]
    train = [np.append(i[0], i[2], 0) for i in t]
    test = t[0][1], t[1][1]
    qwe[i] = U.train(*train, test, rep, e)
    acu[i] = acc(U._f(test[0])[-1],test[1]).astype(np.float16)
  print(f'[Finished in {round(time()-ini_time,5)}s]')
  print(f'{acu.tolist()}\nAccuracy: {np.mean(acu):>2.9}%')
  print(f'Variance: {np.var(acu):>2.6}')

  import matplotlib.pyplot as plt
  plt.plot(np.mean(qwe,0)[1:]/100, color='green', lw=1)
  plt.show()
  return U

if __name__ == '__main__':
  main(sys.argv[1:])


# 4
'''
import numpy as np
np.set_printoptions(linewidth=224,threshold=1000)
np.random.seed(36)
aq = lambda v:1/(1+np.exp(-v))
dq = lambda v:aq(v)*(1-aq(v))
nl = np.linalg.norm

class Layer:
  def __init__(self, i, n):
    self.I = i
    self.N = n
    self.W = 3 * np.random.randn(i, n)
    self.B = 3 * np.random.randn(1, n)
  def __repr__(self):
    return f'<Layer({self.I}, {self.N})>'
  def forward(self, inputs):
    return np.dot(inputs,self.W)+self.B

class Network:
  def __init__(self, *struc):
    self.I = struc[0]
    self.O = struc[-1]
    self.S = struc
    self.M = [Layer(*self.S[i:i+2]) for i in range(len(self.S)-1)]
    self.J = lambda a,y_0: (2*a-y_0-1)**2/4
  def __repr__(self):
    return f'<Network{self.S}>'
  def Pass(self, inputs):
    A = [aq(self.M[0].forward(inputs))]
    for i in self.M[1:]:
      A.append(aq(i.forward(A[-1])))
    return A
  def train(self, x, y, rep=1):
    self.X = np.array(x)
    self.Y = np.array(y)
    # self.K = min(self.X.shape[0], self.Y.shape[0])
    self.Q=[]
    for i in range(rep):
      A = [self.X, *self.Pass(self.X)]
      V = y-A[-1]
      for j, k in enumerate(self.M[::-1]):
        V*= dq(k.forward(A[-2-j]))
        t = k.W.T.copy()
        k.W+= A[-2-j].T.dot(V)
        k.B+= V.mean(axis=0)
        V = V.dot(t)
      if not (i+1)%1000:print(f'MRE betwen training {i+1:6}:{nl(y-A[-1]):<20} {nl(V)}')
      self.Q.append(nl(y-A[-1]))
    # print('MRE aafter training: ',nl(y-A[-1]))
    for i in self.M:
      print(np.max(i.W),np.min(i.W))
      print(np.max(i.B),np.min(i.W))

siz=50
ran=(0, np.pi)
x=np.random.uniform(*ran, (siz,1))
y=(np.sin(x)+1)/2
U=Network(1, 4, 4, 1)
print(f'{U} = {U.M}')
print('MRE before training: ',np.linalg.norm(y-U.Pass(x)[-1]))
U.train(x, y, rep=9999)

import matplotlib.pyplot as plt
plt.plot(U.Q)
plt.show()
tx = np.arange(ran[0]-1,ran[1]+1, 0.01)
ty = U.Pass(np.transpose([tx]))[-1].ravel()
plt.plot(tx,(np.sin(tx)+1)/2,color='#0000ff')
plt.plot(tx,ty,color='#ff0000')
plt.scatter(x,y,color= '#00ff00',marker= ".")
plt.show()
'''

# 2
'''
import numpy as np
import random as rd
# seed=None
# np.random.seed(seed)
# rd.seed(seed)
def f(x):return x[:,:1]
def sig(a):
  # return
  return 0.5+np.arctan(a)/np.pi

s=5
t=np.array([list(np.binary_repr(i,s)) for i in np.arange(0,2**s,dtype=int)]).astype(int)
x=np.random.choice([0,1],size=(7,s))
y=f(x)
weights=np.random.uniform(-1,1,size=(x.shape[1],1))#.astype(np.float16)
bias=-0.5

l=np.dot(t,weights)+bias
error=f(t)-sig(l)
print(np.linalg.norm(error))
J=lambda a,b:-(a*np.log(b)+(1-a)*np.log(1-b))/np.log(2)
for i in range(10000):
  error=J(y,sig(np.dot(x,weights)+bias))
  weights+=np.dot((2*x-1).T,error)

print(weights.T)
print(np.round(sig(np.dot(t,weights)+bias).T).astype(float).tolist())
error=f(t)-sig(np.dot(t,weights)+bias)
print(np.linalg.norm(error))
'''

# 1
'''
import numpy as np
import random as rd
#r=3a+5b-4c
x=np.array([[ 1, 0, 1],
            [ 1, 1, 0],
            [ 1, 0, 1],
            [ 0, 1, 1]])
y=np.array([[1,1,1,0]])
def J(a):
  return np.linalg.norm(np.sum(x*a,axis=1)-y,axis=1)
ite=200;sav=.50;mem=int(ite*sav)
a=np.random.uniform(0,6,size=(ite,3))
a[0:,2]*=-1
r=np.zeros((ite,1))
t=np.zeros((ite,4))
for i in range(ite):
  r[i]=J(a[i])
  t[i]=[r[i],*a[i]]
  # print(f'{a[i]} {r[i]}')
print(t)
for i in range(1000):
  t.sort(axis=0,kind='heapsort')
  # print(t)
  # t[mem:]*=0
  for i in range(mem,ite):
    cm=t[i,1:]+np.random.uniform(-1,1,size=(3))#+np.mean(rd.choices(t[:mem,1:],-t[:mem,0],k=1),axis=0)
    t[i]=[J(cm),*cm]
  # if i==49:print(np.sort(t,axis=0))

print(np.sort(t,axis=0))
'''
