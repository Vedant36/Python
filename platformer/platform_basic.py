
import math   as ma
import numpy  as np
import pygame as pg
# import random as rd
import sys
import time   as tm
from entity import Entity

start_time=tm.time()
fps=60
dim=[500,500]
moving=False
direc=False
pos=[226,236]

pg.init()
fpsClock = pg.time.Clock()
sdf=pg.display.set_mode(dim,0,32)
pg.display.set_caption('Interesting Title')

man=[pg.image.load('data/soil.png'),pg.image.load('data/top.png')]

def bye():
  import os
  import psutil
  process = psutil.Process(os.getpid())
  print(f'   Memory Used: {process.memory_info().rss/1048576} MB')
  print(        f'Execution Time: {tm.time()-start_time}'        )
  # print(pg.QUIT)
  pg.quit()
  sys.exit()

# def text(text,height,center):
#   font=pg.font.Font('freesansbold.ttf',height).render(f'why',True,(255,255,255),(0,0,0))
#   rec=font.get_rect()
#   rec.center=center
#   sdf.blit(font,rec)

def fill():
  pg.draw.rect  (sdf, (  0,255,  0), (0,300,500,200))
  pg.draw.rect  (sdf, (  0,200,  0), (0,280,500, 20))
  pg.draw.rect  (sdf, (  0,  0,255), (0,  0,500,280))
  pg.draw.circle(sdf, (255,255,  0), (0,  0),    40 )


def draw(key,pos):
  # sdf2.fill((0,0,0,0))
  fill()
  sdf2.blit(man[direc],[pos[0]-16,pos[1]])

sdf2=pg.display.set_mode(dim,pg.SRCALPHA,32)
sdf2.fill((0,0,0,0))
fill()
sdf2.blit(man[1],pos)
pg.draw.rect(sdf,(32,23,46),(100,-5,30,30))

while True:
  if pg.event.get(12) : bye()

  qw=pg.key.get_pressed()[275:277]

  if any(qw):
    if not all(qw) : direc=qw.index(1)
    pos[0]=(pos[0]-(2*(direc)-1))%dim[0]
    # sdf2.scroll(-(2*(direc)-1))
    draw(direc,pos)
    pg.display.update()

  fpsClock.tick(fps)