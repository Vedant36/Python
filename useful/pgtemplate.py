#!/usr/bin/env python3
import pygame as pg
import sys
import time as tm

fps = 60
dim = pg.Rect(0, 0, 640, 360)
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Title')

while True:
    for eve in pg.event.get():
        if eve.type==12:
            pg.quit()
            sys.exit()

    pg.display.update()
    fpsClock.tick(fps)