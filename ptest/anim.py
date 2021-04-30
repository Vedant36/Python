#!/usr/bin/env python3
import numpy  as np
import pygame as pg
import random
import sys

fps=60
dim=[500,500]

pg.init()
fpsClock = pg.time.Clock()
sdf=pg.display.set_mode(dim,16,32)
sdfc=sdf.copy()
pg.display.set_caption('Interesting Title')
sdfc.fill((255,255,255))

acc=3
ran = lambda a: random.randint(0,a)
x,y=ran(dim[0]),ran(dim[1])
pre = np.array([[ran(255),ran(255),ran(255),0],[x,y,ran(dim[0]-x),ran(dim[1]-y)]])

while True:
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      pg.quit()
      sys.exit()
    if event.type==pg.VIDEORESIZE:
      dim=event.size
      sdfc=pg.display.set_mode(dim,16,32)
  x,y=ran(dim[0]),ran(dim[1])
  col=np.array([[ran(255),ran(255),ran(255),0],[x,y,ran(dim[0]-x),ran(dim[1]-y)]])
  why=np.linspace(pre,col,acc).astype(int)
  for i in range(acc):
    pg.draw.ellipse(sdfc,why[i,0,0:3],why[i,1])
    # pg.display.update(why[i][1])
  pre=col
  sdf.blit(sdfc,(0,0))
  pg.display.update()
  fpsClock.tick(fps)
