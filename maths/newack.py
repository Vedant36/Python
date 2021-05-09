import numpy as np
import sys
np.set_printoptions(linewidth=224,threshold=sys.maxsize)

qwe = np.zeros((40,40),int)

def ack(m,n):
	if n==0:
		return m
	elif m==0:
		return ack(m+1,n-1)
	else:
		return ack(m-1,ack(m-1,n-1))

# faster implementation of ack
def qack(m,n):
  global qwe
  if n==0:
    return m
  elif m==0:
    return ack(m+1,n-1)
  else:
    return qwe[m-1,qwe[m-1,n-1]] # ack(m-1,ack(m-1,n-1))

for i in range(qwe.shape[0]):
  for j in range(qwe.shape[1]):
    qwe[i,j] = qack(i,j)
print(qwe)
