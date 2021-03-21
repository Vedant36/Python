'''
add drawable class
'''
import pygame as pg
import sys
from classes import *

fps = 30
pg.init()
fpsClock = pg.time.Clock()
dim = pg.Rect(0, 0, 640, 360)
sdf = pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Title')
sdf.fill((187,187,177))

wdg = Widget()
wdg.add(Button((200,200,128,72)))
color = ( 45,233, 46)
pos = None
while True:
  #redraw
  wdg.draw(sdf)

  #logic

  #event handling
  for eve in pg.event.get():
    if eve.type==12:
      pg.quit()
      sys.exit()
    if eve.type in {4, 5, 6}:
      wdg.update(eve)
      if pg.mouse.get_pressed()[0]:
        if pos is None:
          pos = eve.pos
        pg.draw.aaline(sdf, color, pos, eve.pos)
        pos = eve.pos
      if eve.type==6:
        pos = None
        continue

  pg.display.update()
  fpsClock.tick(fps)
