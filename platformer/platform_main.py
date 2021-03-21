import   math as          ma
import  numpy as          np
import pygame as          pg
import random as          rd
import    sys
import   time as          tm
from       os import listdir

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
# lvl = np.array([np.array([list(j) for j in open(f'levels/{i}').read().split('\n')]).astype(int).T for i in listdir('levels')])[:,::-1]
# print(lvl.shape)
# print(lvl)

def bye():
  print(exi)
  pg.quit()
  sys.exit()

# for i in range(lvl.shape[1]):
#   for j in range(lvl.shape[2]):
#     sdf.blit(img[lvl[i][j]],(dim[0],dim[1]))

exi = np.array( [ [20,300],
                  [ 0,  0],
                  [ 0, 30] ] ).astype(np.float16)
ali      = img[3]
fpsClock = pg.time.Clock()
ground   = pg.Rect((0,400,dim[0],dim[1]-400))
mov      = [False,False]

while True:
  tim = fpsClock.get_time()
  exi[0] += exi[1] / 10
  if ground.colliderect((*exi[0],32,32)):
    exi[0,1]  = 400-32
    exi[1,1]  = 0
    mov[1]    = False
    exi[1,0] *= 0.7
  exi[1] += exi[2] / 10
  print(tim, list(exi))
  sdf.fill((255,255,255))
  pg.draw.rect(sdf,(128,244,255),ground)
  sdf.blit(ali,exi[0])

  for event in pg.event.get():
    if event.type == 12 or (event.type==2 and event.key==27):
      bye()
    if event.type == 2:
      if   event.key == pg.K_SPACE:
        exi[1, 1] = -40
      elif event.key == pg.K_a:
        exi[1, 0] = -10
      elif event.key == pg.K_d:
        exi[1, 0]  = 10
      elif event.key == pg.K_LSHIFT:
        exi[1, 1] += 40

  pg.display.update()
  fpsClock.tick(fps)