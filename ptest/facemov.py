# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 07:35:15 2020

@author: Vedant36
"""

import pygame as pg
import sys
import pygame.locals as lv
import math

pg.init()

FPS = 500 # frames per second setting
fpsClock = pg.time.Clock()

# set up the window
sdf = pg.display.set_mode((400, 300), 0, 32)
pg.display.set_caption('Animation')

WHITE = (255, 255, 255)
direction = 'right'
the=0
pre=0

font=pg.font.Font('freesansbold.ttf',30).render('Whelcome',True,(0,0,0),(255,255,255))
rect=font.get_rect()
rect.center=(200,20)
pg.mixer.music.load('areyoulonely.mp3')
pg.mixer.music.play(-1, 2.5)

while True: # the main game loop
  #sdf.fill(WHITE)
  '''if direction == 'right':
    catx += 1
    if catx == 321:
      direction = 'down'
  elif direction == 'down':
    caty += 1
    if caty == 221:
      direction = 'left'
  elif direction == 'left':
    catx -= 1
    if catx == 10:
      direction = 'up'
  elif direction == 'up':
    caty -= 1
    if caty == 10:
      direction = 'right'''
  
  sdf.blit(font,rect)
  for event in pg.event.get():
    try:
      print(event.pos,end=' ')
    except:
      pass
    try:
      print(event.key,end=' ')
    except:
      pass
    if pre!=event.type:
      
      print(event.type,end=' ')
    pre=event.type
    if event.type == lv.QUIT:
      pg.quit()
      sys.exit()
  
  pg.display.update()
  fpsClock.tick(FPS)