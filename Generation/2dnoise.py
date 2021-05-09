import noise
import numpy as np
import pygame as pg
import sys
import math as m
from opensimplex import OpenSimplex

dim = [512,512]
scale = 100
octaves = 5
persistence = 0.5
lacunarity = 2
scale = 40
seed = 36
fps = 30
tmp=OpenSimplex(seed)


pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim)
pg.display.set_caption('Interesting Title')
why=[]

pixObj = pg.PixelArray(sdf)

def terrain(ae):
  if   ae<470:
    return (  0, 69,183) 
  elif ae<485:
    return (239,228,176)
  elif ae<600:
    return ( 34,177, 76)
  # elif ae<670:
  #   return (185,122, 87)
  elif ae<690:
    return (195,195,195)
  else:
    return (242,242,242)

def terrain2(ae):
    return (ae*.255,ae*.255,ae*.255)
    return int(255*ae)
    return (ret//65536,ret//256,ret%256)

def circular(iuy,r=min(dim)//2):
    # return 1
    return (1/(1+m.exp((iuy-r)/36)))

def bye(why=why):
  print(min(why),max(why))
  pg.quit()
  sys.exit()

def noi(i,j):
    # return 1
    # return 500*(tmp.noise2d(i/scale,j/scale)+1)
    return 500*(noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, \
            lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=seed)+1)

def why2(l):
  # return l
  return int(l*(1000-l)/250)

for i in range(dim[0]):
  for j in range(dim[1]):
    ae = int(noi(i,j))#*circular(m.hypot(i-dim[0]//2,j-dim[1]//2)))
    try:pixObj[i][j] = terrain2(ae)
    except:
      print(ae)
    why.append(ae)
  if not (i+1)%16:pg.display.update()
pg.display.update()
# why.append(0)
# bye(why)
# pg.draw.rect(sdf,(255,255,255),(5,5,5,5))
while True:
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      bye(why)
  pg.display.update()
  fpsClock.tick(fps)

# print(noise.pnoise2(0.5,octaves))#,persistence,lacunarity))