import numpy as np
import matplotlib.pyplot as plt

c=0
def val(co):
  return co*co.conjugate()
def lol(co):
  global c
  k=np.zeros((50),dtype=np.complex64)
  k[0]=co
  for i in range(k.shape[0]-1):
    k[i+1]=k[i]**2+k[i]
    if val(k[i+1])>3:return
  c+=1
  plt.plot(k.real,k.imag)

num=2000
poi=np.random.uniform(-1,1,size=(2,num))
print(*poi)
nap=np.complex_(*poi)
why=np.zeros((50,num),dtype=np.complex64)
# print(nap)
why[0]=nap.copy()
del nap
# for i in why
print(c)
# plt.show()