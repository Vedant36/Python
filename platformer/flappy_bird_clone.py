import   math as ma
import  numpy as np
import pygame as pg
import random as rd
import    sys
import   time as tm
import os
print('heylol')
print(os.getcwd())

fps=30
dim=[1000,500]
# a=int(input())

pg.init()
sdf = pg.display.set_mode(dim,0,32)
pg.display.set_caption('Flappy Bird Clone')

def bye():
  print(exi)
  pg.quit()
  sys.exit()

ild      = lambda a: pg.image.load(f'data/{a}.png')
img      = {0:ild('flappy'),1:ild('head'),2:ild('mid')}
ali      = img[0]
alir     = ali.get_rect()
fpsClock = pg.time.Clock()
camera   = pg.Rect((0,100+alir.h,dim[0],dim[1]-200-2*alir.h))
moving   = False
exi      = np.array( [ [(dim[0]-alir.w)/2, dim[1]/2],
                       [0, 0],
                       [0,30]] ).astype(np.float16)
sdf.fill((255,255,255))
pg.draw.rect(sdf,(128,244,255),(0,0,dim[0],100))
pg.draw.rect(sdf,(128,244,255),(0,dim[1]-100,dim[0],100))
sdf.blit(ali,exi[0])

while True:
  if moving:
    tim = fpsClock.get_time()
    exi[0] += exi[1] / 10
    if not camera.colliderect(alir.move(exi[0])):
      exi[0,1] = camera.y + camera.h
      moving = False
    exi[1] += exi[2] / 10
    print(f'{tim} {exi.tolist()}',flush=False)
    sdf.fill((255,255,255))
    pg.draw.rect(sdf,(128,244,255),(0,0,dim[0],100))
    pg.draw.rect(sdf,(128,244,255),(0,dim[1]-100,dim[0],100))
    sdf.blit(ali,exi[0])

  for event in pg.event.get():
    if event.type == pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      bye()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_SPACE:
        exi[1, 1] = -50
        # exi[2, 1] =  30
        moving    = True

  pg.display.update()
  fpsClock.tick(fps)
