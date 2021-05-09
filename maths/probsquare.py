# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 02:22:23 2020

@author: Vedant36
"""

import matplotlib.pyplot as plt
import numpy as np

qwx=[]
qwy=[]
qwe=list(np.arange(1,100+1,1,int))
asd=[]
for i in qwe:
  for j in qwe:
    k=i*j**2
    if k not in qwx:
      qwx.append(k)
      qwy.append(1)
    else:
      qwy[qwx.index(k)]+=1
print('Generation Complete...')

plt.scatter(qwx,qwy,s=1)
plt.show()