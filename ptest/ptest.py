#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:03:45 2020

@author: Vedant36
"""

import math   as ma
import numpy  as np
import pygame as pg
import random as rd
import sys
import time   as tm

start_time=tm.time()
'''
fill(color)
pygame.draw.polygon(surface, color, pointlist, width)
pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.aaline(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, closed, pointlist, width)
pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.ellipse(surface, color, bounding_rectangle, width)
pygame.draw.rect(surface, color, rectangle_tuple, width)

pixObj = pg.PixelArray(sdf)
pixObj[480][380] = BLACK
del pixObj
pygame.display.toggle_fullscreen()
w,h = screen.get_width(),screen.get_height()
pygame.image.save(surface,filename)
catImg = pg.image.load('face.png')
catx = 10
caty = 10
font=pg.font.Font('freesansbold.ttf',30).render('Whelcome',True,(0,0,0),(255,255,255))
rect=font.get_rect()
rect.center=(200,20)
pg.mixer.music.load('areyoulonely.mp3')
pg.mixer.music.play(-1, 2.5)
pg.time.Clock().get_fps()
'''

fps = 500
pre=0
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode((400, 300), 16)
pg.display.set_caption('Title')
the=0
sdf.fill((36,57,31))
def text(text,height=12,pos=(0,0)):
  font=pg.font.Font('freesansbold.ttf',height).render(f'{text}',True,(255,255,255),(0,0,0))
  sdf.blit(font,pos)

text('lolyes', 12)
def bye():
  import os
  import psutil
  process = psutil.Process(os.getpid())
  print('   Memory Used:',process.memory_info().rss/1048576,'MB')
  print('Execution Time:',tm.time()-start_time)
  pg.quit()
  sys.exit()

while True:
  for eve in pg.event.get():
    if eve.type!=pre:
      print(str(eve)[7:-3], flush=1)
    pre=eve.type
    if eve.type == pg.QUIT:
      bye()
  pg.display.update()
  fpsClock.tick(fps)
