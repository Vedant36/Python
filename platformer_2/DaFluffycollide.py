#!/usr/bin/env python3
import pygame as pg, sys
from pygame.locals import *
mainClock = pg.time.Clock()
pg.init()
pg.display.set_caption('Physics Explanation')
screen = pg.display.set_mode((500,500),0,32)
player = pg.Rect(100,100,40,80)
tiles = [pg.Rect(200,350,50,50),pg.Rect(260,320,50,50)]
def move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = rect.collidelistall(tiles)
    for tile in collisions:
        if movement[0] > 0:rect.right = tiles[tile].left
        if movement[0] < 0:rect.left = tiles[tile].right
    rect.y += movement[1]
    collisions = rect.collidelistall(tiles)
    for tile in collisions:
        if movement[1] > 0:rect.bottom = tiles[tile].top
        if movement[1] < 0:rect.top = tiles[tile].bottom
    return rect
right=left=up=down=False
while True:
    screen.fill((0,0,0))
    movement = [0,0]
    if right == True:movement[0] += 5
    if left  == True:movement[0] -= 5
    if up    == True:movement[1] -= 5
    if down  == True:movement[1] += 5
    player = move(player,movement,tiles)
    pg.draw.rect(screen,(255,255,255),player)
    for tile in tiles:
        pg.draw.rect(screen,(255,0,0),tile)
    for eve in pg.event.get((QUIT, KEYDOWN, KEYUP)):
        if eve.type == QUIT:
            pg.quit()
            sys.exit()
        if eve.type in {KEYDOWN,KEYUP}:
            if eve.key == K_RIGHT:right = bool(pg.KEYUP-eve.type)
            if eve.key == K_LEFT :left  = bool(pg.KEYUP-eve.type)
            if eve.key == K_DOWN :down  = bool(pg.KEYUP-eve.type)
            if eve.key == K_UP   :up    = bool(pg.KEYUP-eve.type)
    pg.display.update()
    mainClock.tick(60)
