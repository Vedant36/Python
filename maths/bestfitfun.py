'''This program generates the best fit polynomial function with
degree 'deg' and plots it on a graph'''

import matplotlib.pyplot as plt
import numpy as np

def det(qwe):
  sam=0
  if len(qwe)==2:return qwe[0][0]*qwe[1][1]-qwe[0][1]*qwe[1][0]
  else:
    for i in range(len(qwe)):
      bat=[]
      for j in range(1,len(qwe)):
        ijr=list(qwe[j])
        ijr.pop(i)
        bat.append(ijr)
      sam+=((-1)**(i+1))*det(bat)*qwe[0][i]
    return sam

def Smn(rx,ry,lx,ly=0):
  sum=0
  for i in range(len(rx)):
    sum+=(rx[i]**lx)*(ry[i]**ly)
  return sum

def gen(deg,rx,ry):
  qwe=[]
  for i in range(deg):
    ba=[]
    for j in range(deg):
      ba.append(Smn(rx,ry,i+j))
    qwe.append(ba)
  for i in range(deg):
    qwe[i].append(Smn(rx,ry,i,1))
  
  return(qwe)
  
def detgen(qwe,deg,nr):
  for i in range(deg):
    qwe[i].pop(nr)
  return qwe

rx  = [2,5,6,9]
ry  = [1,2,3,6]
deg = 3
coe = []
rty=gen(deg,rx,ry)
qwe=gen(deg,rx,ry)
crol=list(detgen(qwe,deg,deg))
cro=det(crol)z

plt.scatter(rx,ry,color= "green",marker= ".",s=20)
x=np.arange(min(rx)-1,max(rx)+1,0.1)
# for i in range(deg):
y=np.poly1d()
plt.plot(x,y)#,label=qwe)
plt.show()