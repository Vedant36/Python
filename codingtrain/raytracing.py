#!/usr/bin/env python3
import pygame as pg
import sys
import time as tm

fps = 60
pg.init()
dim = pg.Rect(0, 0, 640, 360)
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Title')

# running = True
while True:
    sdf.fill(0xffffff)
    for eve in pg.event.get():
        # print(eve.type, end='\r')
        if eve.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if eve.type

    pg.display.update()
    fpsClock.tick(fps)