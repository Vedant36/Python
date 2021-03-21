import numpy as np

class Network:

  def __init__(self, *lay, seed=None):
    np.random.seed(seed)
    self.l = lay
    self.w = [np.random.randn(*i)/np.log(i[0]*i[1]) for i in zip(lay[:-1],lay[1:])]
    self.b = [np.zeros((1, i)) for i in lay[1:]]

  def act(self, v):return 1/(1+np.exp(-v))
  def dact(self, v):return self.act(v)*(1-self.act(v))
  def acc(self, y, y0):
    pass

  def predict(self, x):
    A = [x]
    [A.append(self.act(A[-1]@w+b)) for w, b in zip(self.w, self.b)]
    return A

  def train(self, x, y, ite=1, e=1.):
    q = np.zeros(ite)
    for i in range(ite):
      A = self.predict(x)
      V = y - A[-1]
      q[i] = np.linalg.norm(V)
      for a, w, b in zip(A[-2::-1], self.w[::-1], self.b[::-1]):
        V*= self.dact(a@w+b)
        w+= e * a.T@V
        b+= e * V.mean(0)
        V = V@w.T
      if not i%100:
        print(f'{i:>7} {100*(y.argmax(1)==A[-1].argmax(1)).mean():<2.5}', end='\r')
    print()
    return q

'''
  def k_fold(_x, _y, k=1, ite=1, e=1.):
    fold = np.r_[x.shape[0]::k+1]
    acu, qwe = np.zeros((k)), np.zeros((k,rep+1))
    ini_time = time()
    for i in range(k):
      U.__init__(*U.s)  
      t = [np.split(_x, fold[i:i+2], 0), np.split(_y, fold[i:i+2], 0)]
      train = [np.append(i[0], i[2], 0) for i in t]
      test = t[0][1], t[1][1]
      qwe[i] = U.train(*train, test, rep, e)
      acu[i] = acc(U._f(test[0])[-1],test[1]).astype(np.float16)
'''