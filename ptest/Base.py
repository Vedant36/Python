import pygame as pg
import sys

fps = 60
dim = [640, 360]
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim, 0, 32)
pg.display.set_caption('Title')
sdf.fill((255,255,255))

while True:
  for eve in pg.event.get():
    if eve.type==12:
      pg.quit()
      sys.exit()
  pg.display.update()
  fpsClock.tick(fps)