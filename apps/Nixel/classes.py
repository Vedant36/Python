import pygame as pg
class Screen:
  pass
class Widget:
  l, add = list(), classmethod(lambda cls, o:cls.l.append(o))
  draw = classmethod(lambda cls, sdf:[i.draw(sdf)for i in cls.l])
  update = classmethod(lambda cls, sdf:[i.update(sdf)for i in cls.l])

class Popup:
  def __init__(self, rect, color):
    self.r, self.c = pg.Rect(rect), pg.Color(color)
    self.w = None
  def draw(self, sdf):
    pg.draw.rect(sdf, self.c, self.r)
  def update(self, eve):
    if eve.type==6:
      self.w = None
    elif not any([i.r.collidepoint(eve.pos) for i in Widget.l[Widget.l.index(self)+1:]]):
      if eve.type==4 and self.w is not None and pg.mouse.get_pressed()[0]:
        self.r.topleft = eve.pos[0]-self.w[0], eve.pos[1]-self.w[1]
      if eve.type==5 and self.r.collidepoint(eve.pos):
        self.w = eve.pos[0]-self.r.x, eve.pos[1]-self.r.y
        Widget.l.append(Widget.l.pop(Widget.l.index(self)))

class Button:
  def __init__(self, rect):
    self.c = [( 32, 41,255), (123, 35,102), (255, 41, 34)]
    self.s = 0
    self.r = pg.Rect(rect)
    self.i = False
  def draw(self, sdf):
    pg.draw.rect(sdf, self.c[self.s], self.r)
  def update(self, eve):
    t=self.s
    if self.r.collidepoint(eve.pos):
      if eve.type in {5, 6} and eve.button==1:self.s = 7 - eve.type
      else:self.s = (self.s+self.i>1)+1
    else:
      self.s = 0
      if eve.type==6 and eve.button==1:self.i=False
    if 3*t+self.s==6:self.i = True
    return 3*t+self.s == 7
