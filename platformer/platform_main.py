#!/usr/bin/env python3
import pygame as pg
import    sys
import numpy as np

fps=30
dim=[1000,500]
pg.init()
sdf = pg.display.set_mode(dim,0,32)
pg.display.set_caption('Wieldings Platformer')
ild = lambda a: pg.image.load(f'data/{a}.png')
img = { 0:ild('soil'),
        1:ild( 'top'),
        2:ild('back'),
        3:ild('guyr'),
        4:ild('guyl') }
ali      = img[3]
fpsClock = pg.time.Clock()
ground   = pg.Rect((0,400,dim[0],dim[1]-400))
mov      = [False,False]
h_vel=60
v_vel=60
exi = np.array( [[20.,300.],
                 [ 0.,  0.],
                 [ 0., 30.]] )

while True:
  sdf.fill((255,255,255))
  tim = fpsClock.get_time()
  exi[0] += exi[1] / 10
  if ground.colliderect((*exi[0],32,32)):
    exi[0,1]  = 400-32
    exi[1,1]  = 0
    mov[1]    = False
    exi[1,0] *= 0.99
  exi[1] += exi[2] / 10
  # print(tim, list(exi))
  pg.draw.rect(sdf,(128,244,255),ground)
  sdf.blit(ali,exi[0])

  for event in pg.event.get():
    if event.type == pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      pg.quit()
      sys.exit()
    if event.type == pg.KEYDOWN:
      if   event.key == pg.K_SPACE:
        exi[1, 1] -= h_vel
      elif event.key == pg.K_a:
        exi[1, 0] = -v_vel
      elif event.key == pg.K_d:
        exi[1, 0] =  v_vel
      elif event.key == pg.K_LSHIFT:
        exi[1, 1] += h_vel

  pg.display.update()
  fpsClock.tick(fps)

