import pygame as pg
import sys
from classes import *

fps = 60
dim = pg.Rect(0, 0, 640, 380)
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size, pg.RESIZABLE, 32)
pg.display.set_caption('Tester_for_Nixel')
sdf.fill((187,187,177))
class Popup:
  def __init__(self, rect, color):
    self.r = pg.Rect(rect)
    self.w = None
    self.c = pg.Color(color)
  def draw(self, sdf):
    pg.draw.rect(sdf, self.c, self.r)
  def update(self, eve):
    # if eve.type==pg.MOUSEBUTTONDOWN:
    #   self.w = None
    if not any([i.r.collidepoint(eve.pos) for i in Widget.l[Widget.l.index(self)+1:]]):
      if eve.type==pg.MOUSEMOTION and self.w is not None:
        if pg.mouse.get_pressed()[0]:
          self.r.topleft = eve.pos[0]-self.w[0], eve.pos[1]-self.w[1]
        else: self.w = None
      if eve.type==pg.MOUSEBUTTONDOWN and self.r.collidepoint(eve.pos):
        self.w = eve.pos[0]-self.r.x, eve.pos[1]-self.r.y
        Widget.l.append(Widget.l.pop(Widget.l.index(self)))

Widget.add(Popup(( 15, 15,128, 64), 0x2763D3FF))
Widget.add(Popup((150, 15,128, 64), 0xDF1F1FFF))
Widget.add(Popup((150,150,128, 64), 0x13DA27FF))
Widget.add(Popup(( 15,150,128, 64), 0xEDEF43FF))
pg.event.set_allowed((2, 3, 4, 5, 12))
prev = None
while True:
  sdf.fill((187,187,177))
  Widget.draw(sdf)
  for eve in pg.event.get()[:1]:
    if eve.type in {pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION}:
      Widget.update(eve)
    elif eve.type==pg.QUIT:
      pg.quit()
      sys.exit()
    # if eve.type!=prev:
    #   print((prev:=eve.type), end=' ')
  pg.display.update()
  fpsClock.tick(fps)

