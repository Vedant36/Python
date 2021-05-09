import noise
import numpy as np
from PIL import Image

# w, h = 512, 512
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()

shape = (400,400)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
scale=40
seed = np.random.randint(0,100)

def terrain(ae):
  if   ae<500:
    return (  0, 69,183) 
  elif ae<510:
    return (239,228,176)
  elif ae<650:
    return ( 34,177, 76)
  # elif ae<670:
  #   return (185,122, 87)
  elif ae<700:
    return (195,195,195)
  else:
    return (242,242,242)

def terrain2(ae):
    return (ae*255,ae*255,ae*255)
    return int(255*ae)
    return (ret//65536,ret//256,ret%256)

def circular(iuy,r=200):
    return 1
    return (2/(1+m.exp((iuy-r)/50)))

def bye():
  # print(min(why),max(why))
  pg.quit()
  sys.exit()

def noi(i,j):
    # return 1
    return (noise.pnoise2(i/scale, j/scale, octaves=octaves, persistence=persistence, \
            lacunarity=lacunarity, repeatx=1024, repeaty=1024, base=seed)+1)/2

world = np.zeros((*shape,3),dtype=np.uint8)
print(world.shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        ae = int(1000*noi(i, j))#*circular(m.hypot(i-shape[0]/2,j-shape[1]/2))/2
        world[i][j] = np.array(terrain(ae),dtype=np.uint8)

print(world.shape)

# im = Image.open("Scientist.png")
# np_im = np.array(im)
# print(np_im.shape)
# for i in range(np_im.shape[0]):
# 	print(list(np_im[i]))

gen=Image.fromarray(world,'RGB')
gen.save('world.png')
gen.show()
print('dudu')