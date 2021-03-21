import random as r
import math as m
import time as t
import numpy as np
import matplotlib.pyplot as plt

pop = 20
tim = 50
vsz = 1000
spd = 20
ee=ang=1

qwe = np.random.uniform(0,vsz/2,size=(2,pop))
bas = []
inf = []

def xmv(a,ang):
    ang = r.uniform(0,2*m.pi)
    www = a+spd*m.cos(ang)
    if 0<=www<=vsz:
        return a+www
    elif www<0:return 0
    else:return vsz

def ymv(a,ang):
    ang = r.uniform(0,2*m.pi)
    www = a+spd*m.sin(ang)
    if 0<=www<=vsz:
        return a+www
    elif www<0:return 0
    else:return vsz
#ee=1
for i in range(tim):
    ang = (1/(ang*ee))%1+1
    #print(ang,end=' ')
    bas = [list(map(lambda a:round(xmv(a,ang),2),qwe[0])),list(map(lambda a:round(ymv(a,ang),2),qwe[1]))]
    inf.append(bas)
    t.sleep(0.1)
    ee=ang
#print(inf)
#pop*2*tim
inf=np.array(inf).flatten().reshape(pop,2,tim,order='F')
#inf=inf.flatten()
#print(inf)

for i in range(pop):
    plt.plot(inf[i][0],inf[i][1])
plt.show()
'''Mission Failed: well get 'em next time'''