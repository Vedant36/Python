import json
import math   as ma
import numpy  as np
import pygame as pg
import pygame.locals as lv
import random as rd
import sys
import time   as tm

fps=60
dim=np.array([1024,512])

pg.init()
fpsClock=pg.time.Clock()
sdf=pg.display.set_mode(dim, 0, 32)
pg.display.set_caption('Platformer beta')
sdf.fill((44,232,245))
tiles=pg.image.load('data/tiles.png')
me=pg.image.load('data/pixelperson.png')

def bye():
  pg.quit()
  sys.exit()
def load_level(file,tiles):
  with open(f'levels/{file}.json','r') as level:
    asd=json.load(level);con=[asd['width'],asd['height']]
    level=asd['layers'][0]['data']
    del asd
  lev=pg.Surface((con[0]*32,con[1]*32),0,32)
  lev.set_colorkey((0,0,0))
  rec=[]
  for a,b in enumerate(level):
    ret=(32*(a%con[0]),32*(a//con[0]))
    are=(32*((b-1)%4),32*((b-1)//4),32,32)
    # print(a,ret,b,are)
    if b!=0:
        rec.append((*ret,32,32))
        lev.blit(tiles,ret,area=are)
  return lev.copy(),rec
def redraw():
  sdf.fill((44,232,245))
  sdf.blit(lev,camera-dim/2)
  sdf.blit(me,me_s)

class timer:
  tim,lim,now=0,5,tm.time()-1
  def set(self,right):
    self.dif=self.lim*(2*right-1)
    self.now=tm.time()
  def cal(self):
    self.gap=tm.time()-self.now
    if self.gap<1:self.tim=self.dif*(1-self.gap)
    else:self.tim=0
    return self.tim
t=timer()
lev,rec=load_level('map4',tiles)
camera=dim.copy()/2
me_s=pg.Rect(96,64,16,32)
me_p=[0,0]
moving=False
falling=False

while True:
  bumper=me_s.move(me_p).collidelist(rec)
  moving=False
  if bumper==-1:moving=True
  if not moving:
    me_p[1]=0
  me_s.move_ip(me_p)
  if not moving:
    cl=me_s.clip(rec[bumper])
    # print(cl.y,me_s.y)
    if cl.y==me_s.y and cl.h==me_s.h:
      if me_s.left<cl.right:
        me_s.left=cl.right
      elif me_s.right>cl.left:
        me_s.right=cl.left
  redraw()
  if True or moving:
    me_p[1]+=1
    me_p[0]=t.cal()
  for eve in pg.event.get():
    if eve.type==12:
      bye()
    if eve.type==2:
      if eve.key==lv.K_SPACE:
        me_p[1]=-10
      # print(moving,bumper,rec[bumper])
    if eve.type==3:
      pass

  if pg.key.get_pressed()[lv.K_a]:t.set(0)
  elif pg.key.get_pressed()[lv.K_d]:t.set(1)
  moving=True
  pg.display.update()
  fpsClock.tick(fps)
