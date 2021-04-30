# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:32:40 2020

@author: Vedant36
"""

import math   as ma
import numpy  as np
import pygame as pg
import random as rd
import sys
import time   as tm

start_time=tm.time()
fps=30
xl,yl=600,600

pg.init()
fpsClock = pg.time.Clock()
sdf=pg.display.set_mode((xl,yl),0,32)
pg.display.set_caption('Noise')
sdf.fill((192,192,192))

def bye():
  import os
  import psutil
  process = psutil.Process(os.getpid())
  print('   Memory Used:',process.memory_info().rss/1048576,'MB')
  print('Execution Time:',tm.time()-start_time)
  pg.quit()
  sys.exit()

def co():
  return rd.randint(0,255)


def draw():
  pixObj = pg.PixelArray(sdf)
  #al=co()
  for i in range(500):
    for j in range(500):
      #print(al)
      #hyp=ma.hypot(i-250,j-250)
      pixObj[i+50][j+50]=(co(),co(),co())
      #al=255*co()#(255-int(255*(ma.sin(hyp/30)**2)*ma.exp(-hyp/30)))*co()
    if i%50==0:pg.display.update()

draw()
#pg.display.update()

while True:
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      bye()
  #pg.draw.rect(sdf,(0,255,0),(5,5,2,2))
  pg.display.update()
  fpsClock.tick(fps)