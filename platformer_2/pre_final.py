import json
import math as ma
import pygame as pg
import pygame.locals as lv
import sys

fps=60
dim=pg.Rect(0, 0, 1024, 512)
pg.init()
fpsClock=pg.time.Clock()
sdf=pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Platformer beta 2.0 (stable)')

class Player:
  def __init__(self,pos,img):
    self.r=pg.Rect(*pos,16,32)      # native Rect
    self.i=img                      # player image
    self.p=pg.math.Vector2(0,0)
    #tags-inAir-sLip-Flip
    self.t=[True,False,False]

  @property
  def b(self):
    return pg.transform.flip(self.i,self.t[2],self.t[0])

  def move(self,tiles):
    self.r.x += self.p.x
    collisions = self.r.collidelistall(tiles)
    for tile in collisions:
      if self.p.x > 0:
        self.r.right = tiles[tile].left
      elif self.p.x < 0:
        self.r.left = tiles[tile].right
    if self.r.clamp(dim)!=self.r:
      self.r.clamp_ip(dim)
      self.p.y+=1
    v.p.y+=1
    self.r.y += self.p.y
    collisions = self.r.collidelistall(tiles)
    self.t[0]=True
    for tile in collisions:
      if self.p.y > 0:
        self.t[0]=False
        self.r.bottom = tiles[tile].top
        if self.t[1] and bool(self.p.x):
          self.p.x-=2*int(self.p.x>0)-1
        if self.p.x==0:self.t[1]=False
      elif self.p.y < 0:
        self.r.top = tiles[tile].bottom
        self.p.y+=1
      self.p.y=0

def load_rects(file):
  with open(f'levels/{file}.json','r') as level:asd=json.load(level);con=asd['width']
  return [pg.Rect(32*(a%con),32*(a//con),32,32) for a,b in enumerate(asd['layers'][0]['data']) if b!=0]

lev=pg.image.load('levels/map4.png').convert_alpha()
rec=load_rects('map4')
v=Player([128,128],pg.image.load('data/pixelperson.png').convert_alpha())
vel=4

while True:
  #redraw
  sdf.fill((44,232,245))
  sdf.blit(lev,(0,0))
  sdf.blit(v.b,v.r)

  #logic
  v.move(rec)

  #event handler
  for eve in pg.event.get():
    if eve.type==12 or (eve.type==2 and eve.key==lv.K_ESCAPE):
      pg.quit()
      sys.exit()
    if eve.type==2:
      if eve.key==lv.K_SPACE:
        v.p.y=-12
      if eve.key==lv.K_a:
        v.p.x=-vel
        v.t[1:]=[False,True]
      if eve.key==lv.K_d:
        v.p.x=vel
        v.t[1:]=[False,False]
      if eve.key==lv.K_r:
        lev=pg.image.load('levels/map4.png').convert_alpha()
        rec=load_rects('map4')
        v=Player([128,128],pg.image.load('data/pixelperson.png').convert_alpha())
    if eve.type==3:
      if eve.key==lv.K_a:
        if v.p.x!= vel:v.t[1]=True
      if eve.key==lv.K_d:
        if v.p.x!=-vel:v.t[1]=True
  pg.display.update()
  fpsClock.tick(fps)