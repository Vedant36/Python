# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:24:43 2020

@author: Vedant36
"""

import pygame        as pg
import sys
import pygame.locals as lv
import random        as rd
import time          as tm

start_time=tm.time()
fps = 60
box=10
xl,yl=500,300
spd=6#speed
sta=5#no. of blocks at 
poi=5#no. of current length points
pro=pre=275
pos=[[5,15],[6,15],[7,15],[8,15],[9,15]]

def fod():
  return [[rd.randint(0,int(xl/box)-1),rd.randint(0,int(yl/box)-1)]]

def draw(col=(64,255,64),pos=pos):
  for i in pos:
    pg.draw.rect(sdf,col,(i[0]*box,i[1]*box,box,box))
    pg.draw.rect(sdf,(0,0,0),(i[0]*box,i[1]*box,box,box),1)

def che(pre,food):
  sto=pos.pop(0)
  pos.append([0,0])
  if pre<275 and pre+pro != 547:
    pos[-1][0]=pos[-2][0]
    if   pre==273:
      pos[-1][1]=pos[-2][1]-1
    elif pre==274:
      pos[-1][1]=pos[-2][1]+1
  elif pre>274:
    pos[-1][1]=pos[-2][1]
    if   pre==276 :#and pro !=275:
      pos[-1][0]=pos[-2][0]-1
    elif pre==275 and pro !=276:
      pos[-1][0]=pos[-2][0]+1
  if pos[-1]==food[0]:
    pos.insert(0,sto)
    food=fod()
    while food[0] in pos:food=fod()
    draw((255,32,32),food)
    return food
  else:return None
    
def bye():
  import os
  import psutil
  process = psutil.Process(os.getpid())
  print('   Memory Used:',process.memory_info().rss/1048576,'MB')
  print('Execution Time:',tm.time()-start_time)
  pg.quit()
  sys.exit()
  
def text(st):
  io=False
  tm.sleep(2)
  font=pg.font.Font('freesansbold.ttf',int(xl/26)).render('{} {} points'.format(st,poi-5),True,(32,192,255),(0,0,0))
  rect=font.get_rect()
  rect.center=(xl/2,yl/2)
  sdf.fill((0,0,0))
  sdf.blit(font,rect)
  pg.display.update()
  tm.sleep(2)
  bye()

pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode((xl,yl), 0, 32)
pg.display.set_caption('Interesting Title')
c=0
io=True
lis={round(i*fps/spd) for i in range(spd+1)}
pg.mixer.music.load('bensound-slowmotion.mp3')
pg.mixer.music.play(-1, 1)
tm.sleep(1)
draw()
food=fod()
# print(food)
# print(pos)
tm.sleep(1)
draw()
food=fod()
draw((255,32,32),food)
pg.display.update()

while True:
  ert=False
  for event in pg.event.get():
    if event.type == lv.QUIT or (event.type==2 and event.key==27):bye()
    elif event.type==2 and event.key==32:io=not io
    elif event.type==2 and pre!=event.key and event.key in range(273,277):
      if pre+event.key not in {547,551}:
        pre=event.key
    ert=True
    pro=pre
      
  if ((pre==pro and c in lis) or pre!=pro) and io:
    wer=pos[0]
    www=che(pre,food)
    if www!= None:
      food=www
      poi+=1
    if any([pos.count(i)-1 for i in pos]): text('You Just Ate Yourself')
    if not (-1<pos[-1][0]<xl/box and -1<pos[-1][1]<yl/box): text('You Experienced Kinetic Energy')
    pg.draw.rect(sdf,(0,0,0),(wer[0]*box,wer[1]*box,box,box))
    draw()
    ert=True
    if pre!=pro:c=0
  
  c+=1
  if c>fps:c%=fps
  if io:pg.display.update()
  fpsClock.tick(fps)