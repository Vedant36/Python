
import random as r
import math as m
import time as t
#import matplotlib.animation as ani
import numpy as np
import matplotlib.pyplot as plt 
#import os
life=10
vecsiz=1000
food=F=30
c=0.3
q=[]
pop=P=10
#fig = plt.figure()
for i in range(P):
  qwe=np.random.uniform(0,vecsiz,size=(2,life))
  b =list([list(map(lambda a:round(a,2),qwe[0])),list(map(lambda a:round(a,2),qwe[1]))])
  q.append(b)
ty=np.arange(0,vecsiz)
for i in range(P):
  plt.plot(q[i][0],q[i][1])
'''fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    ax1.clear()
    for i in range(life):
      plt.plot(q[i][0],q[i][1])
ani = ani.FuncAnimation(fig, animate, interval=1000)'''
plt.show()
