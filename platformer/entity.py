import math   as ma
import numpy  as np
import pygame as pg
import random as rd
import sys
import time   as tm

vec=pg.math.Vector2

def rect_to_surf(rect):
	surf=pg.Surface(rect.w,rect.h)

class Entity():
	def __init__(self, img, e=0, pos=(0, 0), vel=(0, 0), acc=(0, 0), collides=True, on_ground=False):
		self.i = img
		self.e = e
		self.exis = [vec(pos), vec(vel), vec(acc)]
		self.collides = collides
		self.on_ground = on_ground

	def collided(self,axis=1,collides=True,e=0):
		self.collides = True
		self.e=e

	def on_ground(self,axis=1,on_ground=True):
		self.exis[1][axis]=0

	def update(self,time=1):
		self.exis[0]+=time*self.exis[1]
		self.exis[1]+=time*self.exis[2]

	def draw(self,sdf,pos):
		sdf.blit(self.surf,pos)

lol = Entity(pg.Surface((256,256), 0, 32))
print(lol.__dict__)
print(dir(lol))
