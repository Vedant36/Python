#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:00:21 2020

@author: Vedant36
"""

import pygame as pg
import sys
import time   as tm

start_time=tm.time()
fps=30
xl,yl=800,500
pho={0:'floor.png', 1:'why.png', 2:'box.png', 3:'place.png', 4:'grass.png'}
lev=1

i,qwe=0,[]
try:
  while True:
    qwe.append([list(i) for i in open(f'levels/level{i+1:02}.txt').read().split('\n')])
    i+=1
except Exception as e:
  print(e)

ima=[pg.image.load(f'images/{pho[i]}') for i in range(5)]

pg.init()
fpsClock = pg.time.Clock()
sdf=pg.display.set_mode((xl,yl),0,32)
pg.display.set_caption('Box Out')
sdf.fill(( 31,176,224))

def draw(lev):
  print(qwe, lev)
  xa,ya=len(qwe[lev-1][0]),len(qwe[lev-1])
  xp,yp=xl/2-12*xa,yl/2-12*ya
  for i in range(ya):
    for j in range(xa):
      lol=0
      ele=qwe[lev-1][i][j]
      if ele=='2':lol=8
      sdf.blit(ima[int(ele)],(int(xp+24*j),int(yp+24*i-lol)))
      tm.sleep(0.01)
      pg.display.update()
draw(1)  

while True:
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      pg.quit()
      sys.exit()
  pg.draw.rect(sdf,(0,255,0),(5,5,2,2))
  pg.display.update()
  fpsClock.tick(fps)
