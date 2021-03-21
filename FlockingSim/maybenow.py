# if u come here again use this file only
import pygame as pg
import numpy as np
import sys

fps = 120
dim = pg.Rect(0, 0, 320, 180)
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size)
pg.display.set_caption('Flocking simulation')
pixObj = pg.PixelArray(sdf)

class Boid:
	def __init__(self, num, vel):
		self.n = num
		self.v = vel
		self.pos = np.array([np.random.randint(i, size=num) for i in dim.size]).T
		self.vel = np.random.uniform(-vel**.5, vel**.5, size=(num, 2))

	def apply_behaviour(self):
		"alignment seperation cohesion"
		"for nearby n: n.p.mean -n.v self.p-n.p"
		for i in range(self.n):
			total, behav = 0, np.zeros((3,2))

			for j in range(self.n):
				if i!=j:
					dist = np.linalg.norm(self.pos[i]-self.pos[j])
					if dist>see:
						total+=1
						# behav[0]+= self.vel[j]
						# behav[1]+= ((self.pos[i]-self.pos[j])/dist)*bias
						# behav[2]+= self.pos[j]
			if bool(total):
				self.acc[i]+= (behav.sum(0))/total

	def update(self):
		self.pos = ((self.pos+self.vel)%dim.size).astype(int)
		self.vel+= self.acc
		lin = np.linalg.norm(self.vel, keepdims=1)
		if lin>self.n*self.v:
			self.vel = self.v*self.vel/lin

	def draw(self):
		self.acc = np.zeros((self.n,2))
		# self.apply_behaviour()
		self.update()
		for s in self.pos:
			# pg.draw.aaline(sdf, (255,0,0), s, s+2*p)
			pixObj[s[0]][s[1]] = 0xffffff

see = 10
boid = Boid(20, 1.)
playing = True
while True:
	# display
	if playing:
		sdf.fill(0x1d1d2e)
		boid.draw()

	# events
	for eve in pg.event.get():
		if eve.type==12:
			print()
			pg.quit()
			sys.exit()
		elif eve.type==2 and eve.key==pg.K_SPACE:
			playing = not playing
	pg.display.update()
	fpsClock.tick(fps)

	print(f"{fpsClock.get_fps():2.2f} {np.linalg.norm(boid.vel):2.2f}", end='\r')