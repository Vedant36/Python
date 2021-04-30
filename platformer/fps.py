#!/usr/bin/env python3
import numpy as np
from os.path import join
import pygame as pg
import pygame.locals as lv
import sys

fps=30
dim=pg.Rect(0,0,640,360)

pg.init()
fpsClock = pg.time.Clock()
sdf=pg.display.set_mode(dim.size)
pg.display.set_caption ('Pew Pew')
sdf.fill((161,239,140))

def exp(al):
  return 1/(1+np.exp(-al))

class Entity():
  def __init__(self,sdf,ima,rotate=0):
    self.entity  = pg.image.load(join('data',f'{ima}.png'))
    self.physics = np.zeros((3,2),np.float16)
    self.sdf     = sdf
    self.rotate  = 0

  def draw(self,rotate=None):
    if rotate is not None:self.rotate=rotate
    self.rotate%=360
    new=pg.transform.rotate(self.entity,self.rotate)
    # new.get_rect().center=self.physics[0]+100
    cen=new.get_rect().center
    sdf.blit(new,self.physics[0].astype(np.uint16),area=(cen[0]-16,cen[1]-16,32,32))

  def update(self):
    self.physics[:2]+=self.physics[1:]
    if self.physics[1,0]>3:
      self.physics[1,0]=3
    if self.physics[1,1]>3:
      self.physics[1,1]=3
    if self.physics[1,0]<-3:
      self.physics[1,0]=-3
    if self.physics[1,1]<-3:
      self.physics[1,1]=-3
    # self.physics[1]=5*exp(self.physics[1])*bool(all(self.physics[1]))
    self.physics[0]%=dim.size

vel=1
pg.key.set_repeat(100,30)
player=Entity(sdf,'player')
player.draw()

it=0
while True:
  phy=player.physics
  rot=player.rotate
  for event in pg.event.get():
    if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_q):
      pg.quit()
      sys.exit()
    elif event.type==pg.KEYDOWN:
      if event.key == lv.K_w:
        it=1
      elif event.key == lv.K_s:
        it=-1
      elif event.key == lv.K_a:
        player.rotate+=10
      elif event.key == lv.K_d:
        player.rotate-=10
      elif event.key == lv.K_SPACE:
        player.physics[1:]=np.zeros((2,2))
        it=0
  phy[2]=it*vel*np.array([np.cos(np.radians(rot)),-np.sin(np.radians(rot))])
  player.update()
  sdf.fill((161,239,140))
  player.draw()
  pg.display.update()
  fpsClock.tick(fps)
