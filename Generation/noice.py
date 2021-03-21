import pygame as pg
import sys
import numpy as np
import noise as no
from opensimplex import OpenSimplex

scale=30.
seed=np.random.randint(0, 10000)
print(seed)
tmp=OpenSimplex(seed)
dim=[256, 256]
sdf=pg.display.set_mode(dim)

def tri(a): 
  a=(a+1)/2
  # a=1-a*(1-a)
  a=int(256*a)
  return [a, a, a]

def noi(b, k):
  # a= int(128*(pnoise3(i,j,k)+1))
  # return tri(tmp.noise3d(x, y, k))
  return np.array([np.array([tri(tmp.noise2d(i, j)) for j in b],dtype=np.uint8) for i in b],dtype=np.uint8)

def gen(k):
  # arr=np.zeros((*dim,3),dtype=int)
  # for i in range(dim[0]):
  #   for j in range(dim[1]):
  #     arr[i,j]=noi(i/scale,j/scale,k)
  # x, y = np.indices(dim) / scale
  b = (np.arange(dim[0]) / scale).astype(np.float16)
  arr = noi(b, k)
  #   if dim[0]//2==i:print('Array Half Generated...')
  # print('Array Generation Finished...')
  # print(np.min(arr),np.max(arr))
  arr=((255*(np.max(arr)-arr))/(np.max(arr)-np.min(arr))).astype(np.uint8)
  # print(arr)
  sdf.blit(pg.surfarray.make_surface(arr).convert(),(0,0))

k = 0
bruh=False
gen(k)
pg.display.update()
while True:
  for i in pg.event.get():
    if i.type==12:
      pg.quit()
      sys.exit()
    if i.type==2:
      if i.key in{273,274}:
        scale*= 2**(1-2*(i.key-273))
      elif i.key==32:
        bruh=not bruh
  if bruh:
    # k+=0.05
    gen(k)
    print(3)
  pg.display.update()
