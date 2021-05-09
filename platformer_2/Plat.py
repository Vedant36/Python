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

def sign(num):
	if num:return 2*(num>0)-1
	return 0

class Player:
	p=pg.math.Vector2(0,0)				# momentum
	t=[True,False,False]				# tags-inAir-sLip-vFlip
	l=[True,True]						# variables to control the inAir var
	j=2									# jumpCounter
	k=time.time()
	def __init__(self,pos,img):
		self.r = img.get_rect(topleft=pos)  # native Rect
		self.i = img						# player image
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

