#!/usr/bin/env python3
from json import load
import pygame as pg
import time
import sys

fps=60
dim=pg.Rect(0, 0, 640, 360)
pg.init()
fpsClock=pg.time.Clock()
sdf=pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Platformer 1.0 (stable)')
user = 'Vedant36'
speedrunning = False

def sign(num):
    if num:return 2*(num>0)-1
    return 0

class Player:
    p=pg.math.Vector2(0,0)                  # momentum
    t=[True,False,False]                    # tags-inAir-sLip-vFlip
    l=[True,True]                           # variables to control the inAir var
    j=2                                     # jumpCounter
    k=time.time()
    def __init__(self,pos,img):
        self.r = img.get_rect(topleft=pos)  # native Rect
        self.i = img                        # player image
        self.c = dim.copy()
        self.c2= [self.c.x,self.c.y]

    @property
    def b(self):
        return pg.transform.flip(self.i,self.t[2],False)

    def move(self,tiles,lev):
        self.r.x += int(self.p.x)
        collisions = self.r.collidelistall(tiles)
        for tile in collisions:
            if self.p.x > 0:
                self.r.right = tiles[tile].left
            elif self.p.x < 0:
                self.r.left = tiles[tile].right

        v.p.y+=1
        self.r.y += int(self.p.y)
        collisions = self.r.collidelistall(tiles)
        self.l[1]=True
        for tile in collisions:
            if self.p.y > 0:
                self.l[1]=False
                self.r.bottom = tiles[tile].top
                if self.t[1]:
                    self.p.x-=sign(self.p.x)
                if self.p.x==0:
                    self.t[1]=False
                self.j=2
                self.k=time.time()
            elif self.p.y < 0:
                self.r.top = tiles[tile].bottom
                self.p.y*=-1
                self.p.x+=sign(self.p.x)
            self.p.y=0

        self.t[0]=all(self.l)
        self.l[0]=self.l[1]
        if self.r.clamp(lgr)!=self.r:
            self.r.clamp_ip(lgr)
            self.p.y+=1

def load_rects(file):
    with open(f'levels/{file}.json','r') as level:asd=load(level);w=asd['width']
    return[pg.Rect(32*(a%w),32*(a//w),32,32)for a,b in enumerate(asd['layers'][0]['data'])if b!=0]

lev=pg.image.load('levels/map4.png').convert_alpha()
lgr=lev.get_rect()
rec=load_rects('map4')
v=Player([160,128],pg.image.load('data/pixelperson.png').convert_alpha())
vel=4
pg.event.set_allowed((2, 3, 4, 5, 12))
fit=lambda a,lo,hi:max(lo, min(a,hi))
while True:
    #redraw
    sdf.fill((44,232,245))
    sdf.blit(lev,(0,0),area=v.c)
    sdf.blit(v.b,(v.r.x-v.c.x,v.r.y-v.c.y))

    #logic
    v.move(rec,lev)
    v.c2[0]=fit((v.c2[0]+(v.r.centerx-v.c.centerx)/24),0,lgr.w-dim.w)
    v.c2[1]=fit((v.c2[1]+(v.r.centery-v.c.centery)/24),0,lgr.h-dim.h)
    v.c.topleft=int(v.c2[0]),int(v.c2[1])
    v.c.clamp_ip(lgr)

    #event handler
    for eve in pg.event.get():
        if eve.type==pg.QUIT or (eve.type==pg.KEYDOWN and eve.key==pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        if eve.type==pg.KEYDOWN:
            if eve.key==pg.K_SPACE:
                if bool(v.j) and time.time()-v.k<24/fps:
                    v.p.y=-12
                    v.j=(v.j-1)%3
            elif eve.key==pg.K_a:
                v.p.x=-vel
                v.t[1:3]=[False,True]
            elif eve.key==pg.K_d:
                v.p.x=vel
                v.t[1:3]=[False,False]
        if eve.type==pg.KEYUP:
            if eve.key==pg.K_a:
                if v.p.x!= vel:v.t[1]=True
            if eve.key==pg.K_d:
                if v.p.x!=-vel:v.t[1]=True
        if eve.type==pg.KEYUP and eve.key==pg.K_r:
            lev=pg.image.load('levels/map4.png').convert_alpha()
            rec=load_rects('map4')
            v.i=pg.image.load('data/pixelperson.png').convert_alpha()
            v.r = pg.Rect(160,128,16,32)
            v.t[2] = False

    pg.display.update()
    fpsClock.tick(fps)

'''
            # self.p.y+=1

class stopwatch:
    def __init__(self):
        self.act = self.now = self.set = None
    def check(self):
        if self.set is None: return '0.00000'
        if self.now is not None: 
            self.act = self.now = round(time.time() - self.set,5)
        return self.act
    def start(self):
        self.set = time.time()
        self.now = 0
    def stop(self):
        time.time()-self.set
        self.now = None
    def reset(self):
        self.act = self.now = self.set = None
wa = stopwatch()

# def load_rects(file):
                # if v.p.x!=-vel:v.t[1]=True
        if eve.type in {pg.KEYDOWN, pg.KEYUP} and wa.set is None: wa.start()
        # if eve.type==pg.KEYUP and eve.key==pg.K_r:
            # v.t[2] = False
            wa.reset()

    if speedrunning:
        mo = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        temp = v.r.colliderect((448,32,32,32))
        if temp and not temp2:
            wa.stop()
            print(wa.act)
            with open('speedruns.txt','r') as runs:
                tries = int(runs.readline()[7:])
                asd = runs.read().split('\n')[2:-1]
            a=time.ctime()
            qwe = [[float(i[-10:-1]), f'{mo[a[4:7]]:02}.{int(a[8:10]):02}.{int(a[-2:]):02}', i[4:-22].strip()] for i in asd]
            qwe.append([wa.act, f'{mo[a[4:7]]:02}.{int(a[8:10]):02}.{int(a[-2:]):02}', user.strip()])
            dsa = [f'Tries: {tries+1}\n','#RR    Name                                Date            Times\n','------------------------------------------\n']
            dsa.extend([f'#{i[0]+1:02}    {i[1][-1][:16]:<16}    {i[1][1]}    {i[1][0]:<8}s\n' for i in enumerate(sorted(qwe))])
            with open('speedruns.txt','w') as run:
                run.writelines(dsa)
        temp2=temp
        font=pg.font.Font('freesansbold.ttf',16).render(f'{wa.check()}', True, (0,0,0), (255, 255, 255, 0)).convert()
        font.set_colorkey((255, 255, 255, 0))
        sdf.blit(font,(0,0))
    # pg.display.update()
'''
