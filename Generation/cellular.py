import numpy  as np
import pygame as pg
import sys
import time   as tm

fps=30
dim=[1348,734]
pg.init()
fpsClock=pg.time.Clock()
sdf=pg.display.set_mode(dim, 0, 32)
pg.display.set_caption('Cellular')
ima=[pg.image.load('data/water.png'), pg.image.load('data/grass.png')]
siz=[ima[0].get_width(),ima[0].get_height()]
land=np.random.randint(0,2,(dim[0]//siz[0],dim[1]//(siz[0]-1)),bool)
print(land.shape)
sdf.fill((127,255,127))

def blet(land,i,j):
  sdf.blit(ima[int(land[i,j])],(siz[0]*(i)+6,(siz[0]-1)*(j)-5*int(land[i,j])+6))

def smooth_draw(land):
  for i in range(land.shape[0]):
    for j in range(land.shape[1]):
      if np.sum(land[i-1:i+2,j-1:j+2])+np.random.randint(-2,3)>4:io=True
      else:io=False
      land[i,j]=io
      blet(land,i,j)

for i in range(land.shape[0]):
  for j in range(land.shape[1]):
    blet(land,i,j)
  pg.display.update()

while True:
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      pg.quit()
      sys.exit()
    if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
      sdf.fill((127,255,127))
      smooth_draw(land)
      # draw(land)
  pg.display.update()
  fpsClock.tick(fps)