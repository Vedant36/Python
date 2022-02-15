#!/usr/bin/env python3
"""Simple Platformer Game"""
# pylint: disable=C0103
# Imports {{{1
from json import load
import time
import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
pg = __import__('pygame')

# Initialisation {{{1
FPS = 60
dim = pg.Rect(0, 0, 640, 360)
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Platformer 1.1')

# Helper functions {{{1
def sign(num):
    """Returns the sign of the argument"""
    return -1 if num<0 else int(num>0)

def fit(num, low, high):
    """Brings "num" into the range (low, high)"""
    return max(low, min(num, high))

def load_rects(file):
    """Loads rectangular coordinates for the map"""
    with open(f'levels/{file}.json', encoding="utf-8") as level:
        asd = load(level)
        w = asd['width']
    return[pg.Rect(32*(a%w),32*(a//w),32,32)for a,b in enumerate(asd['layers'][0]['data'])if b != 0]

def die():
    pg.quit()
    sys.exit()

# Player Class {{{1
# TODO: replace class because only one instance of it is ever used
class Player:
    """Player"""
    p = pg.math.Vector2(0,0)  # momentum
    t = [1,0,0]               # tags-inAir-sLip-vFlip
    l = [1,1]                 # variables to control the inAir var
    j = 2                     # jumpCounter
    k = time.time()
    def __init__(self,pos,img):
        self.r = img.get_rect(topleft=pos)  # native Rect
        self.i = img                        # player image
        self.c = dim.copy()
        self.c2= [self.c.x,self.c.y]

    def move(self,tiles):
        """Step through a single frame"""
        self.r.x += int(self.p.x)
        collisions = self.r.collidelistall(tiles)
        for tile in collisions:
            if self.p.x > 0:
                self.r.right = tiles[tile].left
            elif self.p.x < 0:
                self.r.left = tiles[tile].right

        v.p.y += 1
        self.r.y += int(self.p.y)
        collisions = self.r.collidelistall(tiles)
        self.l[1] = True
        for tile in collisions:
            if self.p.y > 0:
                self.l[1] = False
                self.r.bottom = tiles[tile].top
                self.p.x = self.p.x*(1 - 0.1*self.t[1])
                print(self.p.x)
                if self.p.x**2<0.01:
                    self.p.x=0
                self.t[1] = self.p.x != 0
                self.j = 2
                self.k = time.time()
            elif self.p.y < 0:
                self.r.top = tiles[tile].bottom
                self.p.y *= -1
                self.p.x += sign(self.p.x)
            self.p.y = 0

        self.t[0] = all(self.l)
        self.l[0] = self.l[1]
        if self.r.clamp(lgr) != self.r:
            self.r.clamp_ip(lgr)
            self.p.y += 1

# Loading the data {{{1
lev = pg.image.load('levels/map4.png').convert_alpha()
lgr = lev.get_rect()
rec = load_rects('map4')
v = Player([160,128],pg.image.load('data/pixelperson.png').convert_alpha())
vel = 4
pg.event.set_allowed((pg.QUIT, pg.KEYDOWN, pg.KEYUP))

# Game Loop {{{1
while True:
    # redraw {{{2
    sdf.fill((44,232,245))
    sdf.blit(lev,(0,0),area = v.c)
    sdf.blit(pg.transform.flip(v.i,v.t[2],False), (v.r.x-v.c.x,v.r.y-v.c.y))

    # logic {{{2
    v.move(rec)
    v.c2[0] = fit((v.c2[0]+(v.r.centerx-v.c.centerx)/24),0,lgr.w-dim.w)
    v.c2[1] = fit((v.c2[1]+(v.r.centery-v.c.centery)/24),0,lgr.h-dim.h)
    v.c.topleft = int(v.c2[0]),int(v.c2[1])
    v.c.clamp_ip(lgr)

    # event handler {{{2
    for eve in pg.event.get():
        match eve.type:
            case pg.QUIT:
                die()
            case pg.KEYDOWN:
                match eve.key:
                    case pg.K_ESCAPE|pg.K_q:
                        die()
                    case pg.K_SPACE:
                        if bool(v.j) and time.time()-v.k<24/FPS:
                            v.p.y = -12
                            v.j = (v.j-1)%3
                    case pg.K_h:
                        v.p.x = -vel
                        v.t[1:3] = [False,True]
                    case pg.K_l:
                        v.p.x = vel
                        v.t[1:3] = [False,False]
            case pg.KEYUP:
                match eve.key:
                    case pg.K_h:
                        v.t[1] = v.p.x != vel
                    case pg.K_l:
                        v.t[1] = v.p.x != -vel
                    case pg.K_r:
                        lev = pg.image.load('levels/map4.png').convert_alpha()
                        rec = load_rects('map4')
                        v.i = pg.image.load('data/pixelperson.png').convert_alpha()
                        v.r = pg.Rect(160,128,16,32)
                        v.t[2] = False
    # }}}2
    pg.display.update()
    fpsClock.tick(FPS)
