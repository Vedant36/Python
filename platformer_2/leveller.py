import json
import numpy as np

with open('levels/map3.json','r') as l:
  asd=json.load(l)
dim=[asd['height'],asd['width']]
l=np.array(asd['layers'][0]['data']).reshape(dim).astype(np.uint8)
print(l.shape)
map_list=[6,2,7,3,10,14,11,15,5,1,8,4,9,13,12,16]
d_l=l.copy()
for i in range(l.shape[0]):
  for j in range(l.shape[1]):
    pol=np.array([6 if j==0          else l[i,j-1],
                  6 if i==l.shape[0]-1 else l[i+1,j],
                  6 if j==l.shape[1]-1 else l[i,j+1],
                  '6' if i==0          else l[i-1,j]])//6
    if bool(d_l[i,j]):d_l[i,j]=map_list[15-int(np.poly1d(pol)(2))]
asd['layers'][0]['data']=np.ravel(d_l).tolist()
with open('levels/map4.json','w') as l:
  json.dump(asd,l)
print('lolz forever')
