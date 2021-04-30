
import pygame as pg
import pygame.locals as lv
import sys
import numpy as np
np.set_printoptions(linewidth=sys.maxsize,threshold=sys.maxsize)
fps = 60
dim = [640, 360]
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim, 0, 32)
pg.display.set_caption('Title')
sdf.fill((255,255,255))

def text(text,height=12,pos=(0,0)):
  font=pg.font.Font('freesansbold.ttf',height).render(f'{text}',True,(255,255,255),(0,0,0))
  sdf.blit(font,pos)
data = [['train','t10k'],['images.idx3','labels.idx1']]
resh = [[60000,10000],[(28,28),(1,)]]
def load(a, b):
  ret = np.fromfile(f'../datasets/mnist/{data[0][a]}-{data[1][b]}-ubyte', np.uint8)
  return ret[16-8*b:].reshape(resh[0][a],*resh[1][b])
x = np.array([i.T for i in load(0,0)])/256
y = load(0, 1)
p = 0
tr = pg.transform
di = pg.Surface((28,28))
norm = lambda a: (a-a.min())/(a.max()-a.min())
put = lambda x:pg.surfarray.blit_array(di, 255*np.stack((x,x,x),2))
pg.surfarray.blit_array(di, 256 * np.stack((x,x,x),3).mean(0) / .547)
sdf.blit(tr.scale(di, (112, 112)), (120, 0))
pg.key.set_repeat(200,50)
while True:
  put(x[p])
  sdf.blit(tr.scale(di, (112, 112)), (0, 0))
  put(x[p]**4)
  sdf.blit(tr.scale(di, (112, 112)), (0, 120))
  put(norm(x[p]*(1-x[p])))
  sdf.blit(tr.scale(di, (112, 112)), (120, 120))
  t = 4 * x[p]*(1-x[p])
  put(norm(t-t*t))
  sdf.blit(tr.scale(di, (112, 112)), (120, 240))
  put(x[p])
  sdf.blit(tr.scale(tr.smoothscale(tr.smoothscale(di, (64, 64)),(28,28)), (112, 112)), (240, 0))
  put((x[p]>.488).astype(int)-(np.bitwise_and(x[p]>.488,x[p]<.686))/2)
  sdf.blit(tr.scale(tr.smoothscale(di, (28, 28)),(112, 112)), (240, 120))
  text(y[p][0])
  for eve in pg.event.get():
    if eve.type==pg.QUIT:
      pg.quit()
      sys.exit()
    if eve.type==pg.K_KEYDOWN:
      if eve.key in {pg.K_RIGHT,pg.K_LEFT}:
        p = p+(551-2*eve.key)
  pg.display.update()
  fpsClock.tick(fps)
