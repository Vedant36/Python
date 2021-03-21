# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 05:50:58 2020

@author: Vedant36
"""

import math     as ma
import random   as rd
import time     as tm
import numpy    as np
from   graphics import *

win=GraphWin('Flocking Simulation',200,200)
win.setBackground('Black')
sgt=20
the=ma.pi/6
      
class Boid():
  def __init__(self):
   self.pos=[rd.uniform(0,200),rd.uniform(0,200)]
   self.vel=[rd.uniform(-1,1),rd.uniform(-1,1)]
   self.acc=[rd.uniform(-1,1),rd.uniform(-1,1)]
   self.boi=Point(self.pos[0],self.pos[1])
   self.boi.setFill('White')
   
  def update(self):
    self.pre=list(self.pos)
    self.pos=[self.pos[0]+self.vel[0],self.pos[0]+self.vel[0]]
   
  def draw(self):
   self.boi=Point(self.pre[0]%200,self.pre[1]%200)
   self.boi.setFill('Black')
   self.boi.draw(win)
   self.boi=Point(self.pos[0]%200,self.pos[1]%200)
   self.boi.setFill('White')
   self.boi.draw(win)
   
   
qwe=Boid()
while win.checkKey!='Escape':
  qwe.update()
  qwe.draw()
  

#win.getMouse()        
win.close()